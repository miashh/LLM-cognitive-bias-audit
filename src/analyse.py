"""Analyse the results and write the tables and charts for the README.

Run from the project folder after the full runs:

    python src/analyse.py            # real results (results/raw_*.csv)
    python src/analyse.py --pilot    # pilot results, to check the prompts work
    python src/analyse.py --mock     # fake data, for testing the code only

Outputs (in results/):
    summary_table.md       - the tables to paste into the README
    framing_chart.png      - headline chart: models vs the human benchmark
    robustness_chart.png   - the framing gap in every scenario, with 95% intervals

Tests follow docs/hypotheses.md:
    H1: for each scenario, compare the share of certain choices in the gain frame
        and the loss frame, using a two-proportion z-test.
    H2: check whether the gain-minus-loss gap is smaller with the debiasing prompt,
        with a bootstrap 95% confidence interval for the reduction.
    Exploratory: differences between sectors and between models.
"""
import argparse
import glob
import os
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import norm

sys.path.insert(0, os.path.dirname(__file__))
from scenarios import HUMAN_BENCHMARK, SCENARIOS  # noqa: E402

BOOT = 5000
rng = np.random.default_rng(2026)
GAIN_C, LOSS_C, HUMAN_C = "#2f6db5", "#d08a2c", "#8a8a8a"


def two_prop_z(k1, n1, k2, n2):
    """Two-proportion z-test. Returns (z, two-sided p), or (None, None) if every
    answer was identical so no test is possible."""
    if min(n1, n2) == 0:
        return None, None
    pooled = (k1 + k2) / (n1 + n2)
    se = np.sqrt(pooled * (1 - pooled) * (1 / n1 + 1 / n2))
    if se == 0:
        return None, None
    z = (k1 / n1 - k2 / n2) / se
    return z, 2 * norm.sf(abs(z))


def gap_ci(g, l):
    """Gain-minus-loss gap with a 95% interval (normal approximation)."""
    pg, pl = g.mean(), l.mean()
    se = np.sqrt(pg * (1 - pg) / len(g) + pl * (1 - pl) / len(l))
    d = pg - pl
    return d, d - 1.96 * se, d + 1.96 * se


def split(df):
    return df[df.frame == "gain"].chose_certain, df[df.frame == "loss"].chose_certain


def boot_reduction(base, deb):
    """Bootstrap 95% CI for (baseline gap - debias gap), resampling within each
    scenario x frame cell so every scenario keeps its weight."""
    cells = {}
    for name, sub in (("b", base), ("d", deb)):
        for (sc, fr), d in sub.groupby(["scenario", "frame"]):
            cells[(name, sc, fr)] = d.chose_certain.to_numpy()
    out = []
    for _ in range(BOOT):
        m = {k: rng.choice(v, size=len(v), replace=True) for k, v in cells.items()}
        def g(name):
            gain = np.concatenate([v for (n, s, f), v in m.items() if n == name and f == "gain"])
            loss = np.concatenate([v for (n, s, f), v in m.items() if n == name and f == "loss"])
            return gain.mean() - loss.mean()
        out.append(g("b") - g("d"))
    return np.percentile(out, [2.5, 97.5])


def fmt_p(p):
    if p is None:
        return "n/a"
    return "<0.001" if p < 0.001 else f"{p:.3f}"


def pct(s):
    return f"{s.mean():.0%} ({int(s.sum())}/{len(s)})"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pilot", action="store_true")
    ap.add_argument("--mock", action="store_true")
    args = ap.parse_args()
    prefix = "MOCK_" if args.mock else ("pilot_" if args.pilot else "raw_")
    tag = "MOCK_" if args.mock else ("pilot_" if args.pilot else "")
    files = sorted(glob.glob(os.path.join("results", f"{prefix}*.csv")))
    if not files:
        raise SystemExit(f"No results/{prefix}*.csv files found. Run the experiment first.")
    raw = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)

    # Unreadable replies: counted and reported, then left out (rule fixed in advance).
    df = raw.dropna(subset=["chose_certain"]).copy()
    df["chose_certain"] = df.chose_certain.astype(int)
    titles = {k: v["title"] for k, v in SCENARIOS.items()}

    L = []
    if args.mock:
        L.append("> **MOCK DATA: invented answers for testing the code. Not results.**\n")
    if args.pilot:
        L.append("> **PILOT: 4 runs per cell, for checking the prompts only. Not results.**\n")

    # ---- Headline: pooled across all nine scenarios, with the human benchmark ----
    L.append("## Headline: all nine scenarios pooled\n")
    L.append("Share choosing the certain option. Gap = gain minus loss, in percentage points "
             "(pp). A positive gap is the human pattern.\n")
    L.append("| Who | Prompt | Gain wording | Loss wording | Gap (pp) | 95% interval | p (z-test) |")
    L.append("|---|---|---|---|---|---|---|")
    L.append(f"| People (Tversky & Kahneman, 1981) | n/a | {HUMAN_BENCHMARK['gain']:.0%} | "
             f"{HUMAN_BENCHMARK['loss']:.0%} | "
             f"{100*(HUMAN_BENCHMARK['gain']-HUMAN_BENCHMARK['loss']):+.0f} | | |")
    for (m, c), sub in df.groupby(["model", "condition"]):
        g, l = split(sub)
        d, lo, hi = gap_ci(g, l)
        _, p = two_prop_z(g.sum(), len(g), l.sum(), len(l))
        L.append(f"| {m} | {c} | {g.mean():.0%} | {l.mean():.0%} | {100*d:+.0f} | "
                 f"{100*lo:+.0f} to {100*hi:+.0f} | {fmt_p(p)} |")

    # ---- H2 ----
    L.append("\n## H2: does the debiasing prompt reduce the gap?\n")
    L.append("| Model | Baseline gap (pp) | Debias gap (pp) | Reduction (pp) | 95% interval | Supports H2? |")
    L.append("|---|---|---|---|---|---|")
    for m, sub in df.groupby("model"):
        base, deb = sub[sub.condition == "baseline"], sub[sub.condition == "debias"]
        if base.empty or deb.empty:
            continue
        gb = gap_ci(*split(base))[0]
        gd = gap_ci(*split(deb))[0]
        lo, hi = boot_reduction(base, deb)
        verdict = "Yes" if lo > 0 else ("Gap grew" if hi < 0 else "No clear reduction")
        L.append(f"| {m} | {100*gb:+.0f} | {100*gd:+.0f} | {100*(gb-gd):+.0f} | "
                 f"{100*lo:+.0f} to {100*hi:+.0f} | {verdict} |")

    # ---- Exploratory: by sector ----
    L.append("\n## Exploratory: by sector (not pre-registered as a prediction)\n")
    L.append("| Model | Prompt | Sector | Gain wording | Loss wording | Gap (pp) |")
    L.append("|---|---|---|---|---|---|")
    for (m, c, dom), sub in df.groupby(["model", "condition", "domain"]):
        g, l = split(sub)
        L.append(f"| {m} | {c} | {dom} | {g.mean():.0%} | {l.mean():.0%} | "
                 f"{100*(g.mean()-l.mean()):+.0f} |")

    # ---- H1: every scenario ----
    L.append("\n## H1: framing effect in each scenario\n")
    L.append("| Model | Prompt | Scenario | Gain wording | Loss wording | Gap (pp) | p (z-test) | Note |")
    L.append("|---|---|---|---|---|---|---|---|")
    forest = []
    n_sig = {}
    for (m, c, sc), sub in df.groupby(["model", "condition", "scenario"]):
        g, l = split(sub)
        _, p = two_prop_z(g.sum(), len(g), l.sum(), len(l))
        d, lo, hi = gap_ci(g, l)
        forest.append(dict(model=m, condition=c, scenario=sc, gap=d, lo=lo, hi=hi))
        if p is not None and p < 0.05 and d > 0:
            n_sig[(m, c)] = n_sig.get((m, c), 0) + 1
        note = ""
        if g.mean() in (0, 1) and l.mean() == g.mean():
            note = "Same answer every time"
        L.append(f"| {m} | {c} | {titles.get(sc, sc)} | {pct(g)} | {pct(l)} | "
                 f"{100*d:+.0f} | {fmt_p(p)} | {note} |")

    L.append("\n**Consistency across scenarios** (scenarios with a significant gap in the "
             "human direction, p < 0.05):\n")
    for (m, c), sub in df.groupby(["model", "condition"]):
        L.append(f"- {m}, {c}: {n_sig.get((m, c), 0)} of {sub.scenario.nunique()}")

    # ---- Unreadable replies ----
    L.append("\n## Unreadable replies (left out of the analysis)\n")
    L.append("| Model | Prompt | Unreadable | Total |\n|---|---|---|---|")
    for (m, c), sub in raw.groupby(["model", "condition"]):
        L.append(f"| {m} | {c} | {int(sub.chose_certain.isna().sum())} | {len(sub)} |")
    L.append("\nNine scenarios are tested per model and prompt, so about one in twenty "
             "could reach p < 0.05 by chance alone. The pooled results and the consistency "
             "count matter more than any single p-value.")

    out_md = os.path.join("results", f"{tag}summary_table.md")
    with open(out_md, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")

    banner = "MOCK DATA, NOT RESULTS" if args.mock else ("PILOT ONLY, NOT RESULTS" if args.pilot else None)
    models = sorted(df.model.unique())

    # ---- Chart 1: headline bars, people vs each model ----
    groups = [("People\n(1981 study)", HUMAN_BENCHMARK["gain"], HUMAN_BENCHMARK["loss"], True)]
    for m in models:
        for c in ["baseline", "debias"]:
            s = df[(df.model == m) & (df.condition == c)]
            if s.empty:
                continue
            g, l = split(s)
            groups.append((f"{m}\n{'baseline' if c == 'baseline' else 'debiasing'} prompt",
                           g.mean(), l.mean(), False))
    fig, ax = plt.subplots(figsize=(2.0 * len(groups) + 1.5, 4.6))
    x = np.arange(len(groups))
    for i, (lab, gv, lv, human) in enumerate(groups):
        ax.bar(i - 0.19, gv * 100, 0.38, color=GAIN_C, alpha=0.45 if human else 1,
               label="Gain wording ('saved')" if i == 1 else None)
        ax.bar(i + 0.19, lv * 100, 0.38, color=LOSS_C, alpha=0.45 if human else 1,
               label="Loss wording ('lost')" if i == 1 else None)
        ax.text(i - 0.19, gv * 100 + 1.5, f"{gv:.0%}", ha="center", fontsize=9)
        ax.text(i + 0.19, lv * 100 + 1.5, f"{lv:.0%}", ha="center", fontsize=9)
    ax.set_xticks(x, [g[0] for g in groups], fontsize=9)
    ax.set_ylim(0, 112)
    ax.set_ylabel("% choosing the certain option")
    ax.spines[["top", "right"]].set_visible(False)
    ax.legend(frameon=False, fontsize=9, loc="upper right", ncol=2)
    ax.set_title(banner or "Same outcomes, different wording: how often the certain option is chosen",
                 fontsize=11)
    fig.tight_layout()
    fig.savefig(os.path.join("results", f"{tag}framing_chart.png"), dpi=150)

    # ---- Chart 2: robustness, the gap in every scenario with 95% intervals ----
    fr = pd.DataFrame(forest)
    order = [k for k in SCENARIOS if k in set(fr.scenario)]
    fig, axes = plt.subplots(1, len(models), figsize=(5.2 * len(models) + 1.8, 0.42 * len(order) + 1.8),
                             squeeze=False, sharey=True)
    for ax, m in zip(axes[0], models):
        for c, col, off in (("baseline", "#1f1f1f", -0.15), ("debias", "#3a9a6b", 0.15)):
            s = fr[(fr.model == m) & (fr.condition == c)].set_index("scenario").reindex(order)
            y = np.arange(len(order)) + off
            ax.errorbar(s.gap * 100, y, xerr=[(s.gap - s.lo) * 100, (s.hi - s.gap) * 100],
                        fmt="o", color=col, ms=5, capsize=2, lw=1,
                        label="Baseline prompt" if c == "baseline" else "Debiasing prompt")
        ax.axvline(0, color="#999999", lw=1)
        ax.axvline(100 * (HUMAN_BENCHMARK["gain"] - HUMAN_BENCHMARK["loss"]), color=HUMAN_C,
                   lw=1, ls="--", label="People (1981): +50 pp")
        ax.set_yticks(np.arange(len(order)),
                      [f"{SCENARIOS[k]['domain'].title()}: {titles[k]}" for k in order], fontsize=9)
        ax.set_xlim(-100, 100)
        ax.set_xlabel("Framing gap: gain minus loss (percentage points)")
        ax.set_title(m, fontsize=10)
        ax.spines[["top", "right"]].set_visible(False)
    axes[0][0].invert_yaxis()  # shared axis: flip once so the first scenario is on top
    handles, labels = axes[0][0].get_legend_handles_labels()
    fig.legend(handles, labels, frameon=False, fontsize=9, loc="lower center", ncol=3)
    fig.suptitle(banner or "Robustness: the framing gap in each of the nine scenarios", fontsize=11)
    fig.tight_layout(rect=(0, 0.07, 1, 1))
    fig.savefig(os.path.join("results", f"{tag}robustness_chart.png"), dpi=150)

    print("\n".join(L))
    print(f"\nUnreadable replies left out: {int(raw.chose_certain.isna().sum())} of {len(raw)}")
    print(f"Saved {out_md}, {tag}framing_chart.png and {tag}robustness_chart.png in results/")


if __name__ == "__main__":
    main()
