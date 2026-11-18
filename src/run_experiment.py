"""Run the framing experiment on a free local model served by Ollama.

Run from the project folder, with your virtual environment active:

    python src/run_experiment.py --model llama3.2:3b --pilot   # 4 runs per cell, quick check
    python src/run_experiment.py --model llama3.2:3b           # full run, 30 runs per cell
    python src/run_experiment.py --model qwen2.5:3b            # second model

Every answer is saved to results/raw_<model>.csv as it arrives. If you stop the
script (Ctrl+C) and start it again, finished trials are skipped.

--mock is for TESTING THE CODE ONLY. It invents answers, writes them to a file
starting with MOCK_, and must never be reported as a result.
"""
import argparse
import csv
import os
import random
import re
import time
from datetime import datetime

from scenarios import SCENARIOS, build_prompt

SCENARIO_IDS = list(SCENARIOS.keys())
FRAMES = ["gain", "loss"]
CONDITIONS = ["baseline", "debias"]
TEMPERATURE = 0.8  # Ollama's default. Some randomness is needed, or every run is identical.
SEED = 2026        # fixes the trial order so the run can be repeated exactly
FIELDS = ["trial_id", "model", "scenario", "domain", "frame", "condition", "run", "certain_first",
          "certain_label", "choice", "chose_certain", "raw_response", "timestamp"]
ANSWER_RE = re.compile(r"Answer:\s*\**\s*([12])", re.IGNORECASE)


def parse_choice(text):
    """Return 1 or 2 from the LAST 'Answer: 1/2' in the reply, or None if there isn't one.
    Unreadable replies are kept in the file and counted, but left out of the analysis
    (a rule fixed before running)."""
    matches = ANSWER_RE.findall(text or "")
    return int(matches[-1]) if matches else None


def make_trials(model, runs):
    """Build every trial. Within each cell (scenario x frame x condition), half the runs
    show the certain option first and half show it second, in a shuffled order."""
    rng = random.Random(SEED)
    trials = []
    for scenario in SCENARIO_IDS:
        for frame in FRAMES:
            for condition in CONDITIONS:
                flags = [True] * (runs // 2) + [False] * (runs - runs // 2)
                rng.shuffle(flags)
                for i, certain_first in enumerate(flags):
                    trials.append({
                        "trial_id": f"{model}|{scenario}|{frame}|{condition}|{i}",
                        "model": model, "scenario": scenario,
                        "domain": SCENARIOS[scenario]["domain"], "frame": frame,
                        "condition": condition, "run": i, "certain_first": certain_first,
                    })
    rng.shuffle(trials)  # mixed order, so time effects can't line up with one condition
    return trials


def ask_model(model, prompt, condition):
    import ollama  # imported here so --mock works without Ollama installed
    resp = ollama.chat(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        options={"temperature": TEMPERATURE,
                 "num_predict": 20 if condition == "baseline" else 900},  # raised from 500 after the pilot
    )
    return resp["message"]["content"]


def mock_answer(frame, condition, certain_label, rng):
    """FAKE answers for checking the code works. Not data."""
    p_certain = {"gain": 0.75, "loss": 0.35}[frame]
    if condition == "debias":
        p_certain = 0.55
    choice = certain_label if rng.random() < p_certain else 3 - certain_label
    return f"(mock) Answer: {choice}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="llama3.2:3b")
    ap.add_argument("--runs", type=int, default=30, help="runs per cell")
    ap.add_argument("--pilot", action="store_true", help="4 runs per cell, saved separately")
    ap.add_argument("--mock", action="store_true", help="fake answers, for testing code only")
    args = ap.parse_args()

    runs = 4 if args.pilot else args.runs
    safe = args.model.replace(":", "-").replace("/", "-")
    prefix = "MOCK_" if args.mock else ("pilot_" if args.pilot else "raw_")
    os.makedirs("results", exist_ok=True)
    path = os.path.join("results", f"{prefix}{safe}.csv")

    done = set()
    if os.path.exists(path):
        with open(path, newline="", encoding="utf-8") as f:
            done = {row["trial_id"] for row in csv.DictReader(f)}

    trials = [t for t in make_trials(args.model, runs) if t["trial_id"] not in done]
    print(f"{len(done)} trials already done, {len(trials)} to run. Saving to {path}")
    rng = random.Random(SEED + 1)
    start = time.time()

    new_file = not os.path.exists(path)
    with open(path, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        if new_file:
            writer.writeheader()
        for n, t in enumerate(trials, 1):
            prompt, certain_label = build_prompt(t["scenario"], t["frame"], t["condition"],
                                                 t["certain_first"])
            if args.mock:
                text = mock_answer(t["frame"], t["condition"], certain_label, rng)
            else:
                text = ask_model(args.model, prompt, t["condition"])
            choice = parse_choice(text)
            writer.writerow({
                **t, "certain_label": certain_label, "choice": choice or "",
                "chose_certain": "" if choice is None else int(choice == certain_label),
                "raw_response": text, "timestamp": datetime.now().isoformat(timespec="seconds"),
            })
            f.flush()  # save every answer straight away
            if n % 20 == 0 or n == len(trials):
                left = (time.time() - start) / n * (len(trials) - n) / 60
                print(f"  {n}/{len(trials)} done, about {left:.0f} min left")
    print("Done.")


if __name__ == "__main__":
    main()
