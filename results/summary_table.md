## Headline: all nine scenarios pooled

Share choosing the certain option. Gap = gain minus loss, in percentage points (pp). A positive gap is the human pattern.

| Who | Prompt | Gain wording | Loss wording | Gap (pp) | 95% interval | p (z-test) |
|---|---|---|---|---|---|---|
| People (Tversky & Kahneman, 1981) | n/a | 72% | 22% | +50 | | |
| llama3.2:3b | baseline | 29% | 25% | +5 | -3 to +12 | 0.216 |
| llama3.2:3b | debias | 37% | 39% | -3 | -12 to +6 | 0.526 |
| qwen2.5:3b | baseline | 11% | 4% | +7 | +3 to +12 | 0.001 |
| qwen2.5:3b | debias | 59% | 44% | +15 | +7 to +23 | <0.001 |

## H2: does the debiasing prompt reduce the gap?

| Model | Baseline gap (pp) | Debias gap (pp) | Reduction (pp) | 95% interval | Supports H2? |
|---|---|---|---|---|---|
| llama3.2:3b | +5 | -3 | +8 | -3 to +19 | No clear reduction |
| qwen2.5:3b | +7 | +15 | -7 | -17 to +2 | No clear reduction |

## Exploratory: by sector (not pre-registered as a prediction)

| Model | Prompt | Sector | Gain wording | Loss wording | Gap (pp) |
|---|---|---|---|---|---|
| llama3.2:3b | baseline | consulting | 24% | 19% | +6 |
| llama3.2:3b | baseline | finance | 34% | 18% | +16 |
| llama3.2:3b | baseline | technology | 30% | 38% | -8 |
| llama3.2:3b | debias | consulting | 33% | 42% | -9 |
| llama3.2:3b | debias | finance | 40% | 35% | +5 |
| llama3.2:3b | debias | technology | 36% | 41% | -5 |
| qwen2.5:3b | baseline | consulting | 3% | 0% | +3 |
| qwen2.5:3b | baseline | finance | 13% | 0% | +13 |
| qwen2.5:3b | baseline | technology | 18% | 12% | +6 |
| qwen2.5:3b | debias | consulting | 59% | 47% | +12 |
| qwen2.5:3b | debias | finance | 61% | 42% | +20 |
| qwen2.5:3b | debias | technology | 57% | 43% | +13 |

## H1: framing effect in each scenario

| Model | Prompt | Scenario | Gain wording | Loss wording | Gap (pp) | p (z-test) | Note |
|---|---|---|---|---|---|---|---|
| llama3.2:3b | baseline | Keeping staff after a merger | 33% (10/30) | 20% (6/30) | +13 | 0.243 |  |
| llama3.2:3b | baseline | Restructuring after a lost contract | 23% (7/30) | 20% (6/30) | +3 | 0.754 |  |
| llama3.2:3b | baseline | Supply chain disruption | 17% (5/30) | 17% (5/30) | +0 | 1.000 |  |
| llama3.2:3b | baseline | Fraud on customer accounts | 40% (12/30) | 13% (4/30) | +27 | 0.020 |  |
| llama3.2:3b | baseline | A fund hit by a market shock | 30% (9/30) | 10% (3/30) | +20 | 0.053 |  |
| llama3.2:3b | baseline | Loan defaults in a downturn | 32% (9/28) | 30% (9/30) | +2 | 0.860 |  |
| llama3.2:3b | baseline | Reskilling during an AI rollout | 33% (10/30) | 37% (11/30) | -3 | 0.787 |  |
| llama3.2:3b | baseline | Customer churn after an outage | 23% (7/30) | 37% (10/27) | -14 | 0.259 |  |
| llama3.2:3b | baseline | Response to a security breach | 33% (10/30) | 40% (12/30) | -7 | 0.592 |  |
| llama3.2:3b | debias | Keeping staff after a merger | 20% (6/30) | 34% (10/29) | -14 | 0.211 |  |
| llama3.2:3b | debias | Restructuring after a lost contract | 30% (7/23) | 48% (13/27) | -18 | 0.203 |  |
| llama3.2:3b | debias | Supply chain disruption | 52% (13/25) | 44% (11/25) | +8 | 0.571 |  |
| llama3.2:3b | debias | Fraud on customer accounts | 52% (14/27) | 36% (10/28) | +16 | 0.228 |  |
| llama3.2:3b | debias | A fund hit by a market shock | 24% (6/25) | 36% (9/25) | -12 | 0.355 |  |
| llama3.2:3b | debias | Loan defaults in a downturn | 43% (12/28) | 33% (9/27) | +10 | 0.467 |  |
| llama3.2:3b | debias | Reskilling during an AI rollout | 29% (7/24) | 40% (10/25) | -11 | 0.426 |  |
| llama3.2:3b | debias | Customer churn after an outage | 40% (10/25) | 33% (9/27) | +7 | 0.618 |  |
| llama3.2:3b | debias | Response to a security breach | 39% (11/28) | 50% (14/28) | -11 | 0.420 |  |
| qwen2.5:3b | baseline | Keeping staff after a merger | 3% (1/30) | 0% (0/30) | +3 | 0.313 |  |
| qwen2.5:3b | baseline | Restructuring after a lost contract | 3% (1/30) | 0% (0/30) | +3 | 0.313 |  |
| qwen2.5:3b | baseline | Supply chain disruption | 3% (1/30) | 0% (0/30) | +3 | 0.313 |  |
| qwen2.5:3b | baseline | Fraud on customer accounts | 0% (0/30) | 0% (0/30) | +0 | n/a | Same answer every time |
| qwen2.5:3b | baseline | A fund hit by a market shock | 0% (0/30) | 0% (0/30) | +0 | n/a | Same answer every time |
| qwen2.5:3b | baseline | Loan defaults in a downturn | 40% (12/30) | 0% (0/30) | +40 | <0.001 |  |
| qwen2.5:3b | baseline | Reskilling during an AI rollout | 43% (13/30) | 30% (9/30) | +13 | 0.284 |  |
| qwen2.5:3b | baseline | Customer churn after an outage | 10% (3/30) | 7% (2/30) | +3 | 0.640 |  |
| qwen2.5:3b | baseline | Response to a security breach | 0% (0/30) | 0% (0/30) | +0 | n/a | Same answer every time |
| qwen2.5:3b | debias | Keeping staff after a merger | 57% (17/30) | 47% (14/30) | +10 | 0.438 |  |
| qwen2.5:3b | debias | Restructuring after a lost contract | 60% (18/30) | 41% (12/29) | +19 | 0.153 |  |
| qwen2.5:3b | debias | Supply chain disruption | 60% (18/30) | 53% (16/30) | +7 | 0.602 |  |
| qwen2.5:3b | debias | Fraud on customer accounts | 67% (20/30) | 27% (8/30) | +40 | 0.002 |  |
| qwen2.5:3b | debias | A fund hit by a market shock | 60% (18/30) | 57% (17/30) | +3 | 0.793 |  |
| qwen2.5:3b | debias | Loan defaults in a downturn | 57% (17/30) | 41% (12/29) | +15 | 0.240 |  |
| qwen2.5:3b | debias | Reskilling during an AI rollout | 57% (17/30) | 53% (16/30) | +3 | 0.795 |  |
| qwen2.5:3b | debias | Customer churn after an outage | 53% (16/30) | 30% (9/30) | +23 | 0.067 |  |
| qwen2.5:3b | debias | Response to a security breach | 60% (18/30) | 47% (14/30) | +13 | 0.301 |  |

**Consistency across scenarios** (scenarios with a significant gap in the human direction, p < 0.05):

- llama3.2:3b, baseline: 1 of 9
- llama3.2:3b, debias: 0 of 9
- qwen2.5:3b, baseline: 1 of 9
- qwen2.5:3b, debias: 1 of 9

## Exploratory: does the position of an option matter?

If a model prefers whichever option is listed first, it chooses the certain option more often when it is Option 1. Position was balanced in every cell, so this cannot create a framing gap, but it shows how much answers depend on layout. The position effect is tested the same way as the framing effect (two-proportion z-test).

| Model | Prompt | Chose Option 1 | Safe option chosen when listed first | Safe option chosen when listed second | Position effect (pp) | 95% interval | p |
|---|---|---|---|---|---|---|---|
| llama3.2:3b | baseline | 58% | 35% (94/267) | 19% (51/268) | +16 | +9 to +24 | <0.001 |
| llama3.2:3b | debias | 78% | 66% (157/238) | 10% (24/238) | +56 | +49 to +63 | <0.001 |
| qwen2.5:3b | baseline | 53% | 11% (30/270) | 4% (12/270) | +7 | +2 to +11 | 0.004 |
| qwen2.5:3b | debias | 77% | 79% (211/268) | 24% (66/270) | +54 | +47 to +61 | <0.001 |

## Exploratory: wording and position in one model (logistic regression)

For each model and prompt, a logistic regression predicts choosing the safe option from the wording (gain vs loss) and the position (listed first vs second), with scenario fixed effects. Odds ratios above 1 mean the safe option became more likely. Scenarios where every answer was the same are left out, because they carry no information about either effect.

| Model | Prompt | Wording: gain vs loss (odds ratio) | 95% CI | p | Position: first vs second (odds ratio) | 95% CI | p | Trials used | Scenarios left out |
|---|---|---|---|---|---|---|---|---|---|
| llama3.2:3b | baseline | 1.30 | 0.88 to 1.92 | 0.194 | 2.37 | 1.59 to 3.54 | <0.001 | 535 | 0 |
| llama3.2:3b | debias | 0.88 | 0.55 to 1.39 | 0.571 | 18.84 | 11.26 to 31.52 | <0.001 | 476 | 0 |
| qwen2.5:3b | baseline | 4.42 | 1.94 to 10.08 | <0.001 | 3.81 | 1.69 to 8.56 | 0.001 | 360 | 3 |
| qwen2.5:3b | debias | 2.38 | 1.56 to 3.64 | <0.001 | 13.17 | 8.58 to 20.22 | <0.001 | 538 | 0 |

## Unreadable replies (left out of the analysis)

| Model | Prompt | Unreadable | Total |
|---|---|---|---|
| llama3.2:3b | baseline | 5 | 540 |
| llama3.2:3b | debias | 64 | 540 |
| qwen2.5:3b | baseline | 0 | 540 |
| qwen2.5:3b | debias | 2 | 540 |

Nine scenarios are tested per model and prompt, so about one in twenty could reach p < 0.05 by chance alone. The pooled results and the consistency count matter more than any single p-value.
