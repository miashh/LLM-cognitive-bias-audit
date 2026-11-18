> **PILOT: 4 runs per cell, for checking the prompts only. Not results.**

## Headline: all nine scenarios pooled

Share choosing the certain option. Gap = gain minus loss, in percentage points (pp). A positive gap is the human pattern.

| Who | Prompt | Gain wording | Loss wording | Gap (pp) | 95% interval | p (z-test) |
|---|---|---|---|---|---|---|
| People (Tversky & Kahneman, 1981) | n/a | 72% | 22% | +50 | | |
| llama3.2:3b | baseline | 32% | 36% | -4 | -26 to +18 | 0.741 |
| llama3.2:3b | debias | 37% | 43% | -6 | -30 to +18 | 0.612 |
| qwen2.5:3b | baseline | 11% | 3% | +8 | -3 to +20 | 0.164 |
| qwen2.5:3b | debias | 56% | 29% | +26 | +4 to +49 | 0.027 |

## H2: does the debiasing prompt reduce the gap?

| Model | Baseline gap (pp) | Debias gap (pp) | Reduction (pp) | 95% interval | Supports H2? |
|---|---|---|---|---|---|
| llama3.2:3b | -4 | -6 | +2 | -26 to +30 | No clear reduction |
| qwen2.5:3b | +8 | +26 | -18 | -41 to +5 | No clear reduction |

## Exploratory: by sector (not pre-registered as a prediction)

| Model | Prompt | Sector | Gain wording | Loss wording | Gap (pp) |
|---|---|---|---|---|---|
| llama3.2:3b | baseline | consulting | 17% | 33% | -17 |
| llama3.2:3b | baseline | finance | 42% | 25% | +17 |
| llama3.2:3b | baseline | technology | 40% | 50% | -10 |
| llama3.2:3b | debias | consulting | 40% | 42% | -2 |
| llama3.2:3b | debias | finance | 33% | 27% | +6 |
| llama3.2:3b | debias | technology | 36% | 58% | -22 |
| qwen2.5:3b | baseline | consulting | 8% | 0% | +8 |
| qwen2.5:3b | baseline | finance | 8% | 0% | +8 |
| qwen2.5:3b | baseline | technology | 17% | 8% | +8 |
| qwen2.5:3b | debias | consulting | 73% | 18% | +55 |
| qwen2.5:3b | debias | finance | 45% | 45% | +0 |
| qwen2.5:3b | debias | technology | 50% | 25% | +25 |

## H1: framing effect in each scenario

| Model | Prompt | Scenario | Gain wording | Loss wording | Gap (pp) | p (z-test) | Note |
|---|---|---|---|---|---|---|---|
| llama3.2:3b | baseline | Keeping staff after a merger | 50% (2/4) | 50% (2/4) | +0 | 1.000 |  |
| llama3.2:3b | baseline | Restructuring after a lost contract | 0% (0/4) | 50% (2/4) | -50 | 0.102 |  |
| llama3.2:3b | baseline | Supply chain disruption | 0% (0/4) | 0% (0/4) | +0 | n/a | Same answer every time |
| llama3.2:3b | baseline | Fraud on customer accounts | 50% (2/4) | 25% (1/4) | +25 | 0.465 |  |
| llama3.2:3b | baseline | A fund hit by a market shock | 25% (1/4) | 50% (2/4) | -25 | 0.465 |  |
| llama3.2:3b | baseline | Loan defaults in a downturn | 50% (2/4) | 0% (0/4) | +50 | 0.102 |  |
| llama3.2:3b | baseline | Reskilling during an AI rollout | 25% (1/4) | 100% (4/4) | -75 | 0.028 |  |
| llama3.2:3b | baseline | Customer churn after an outage | 50% (1/2) | 50% (2/4) | +0 | 1.000 |  |
| llama3.2:3b | baseline | Response to a security breach | 50% (2/4) | 0% (0/4) | +50 | 0.102 |  |
| llama3.2:3b | debias | Keeping staff after a merger | 50% (2/4) | 50% (2/4) | +0 | 1.000 |  |
| llama3.2:3b | debias | Restructuring after a lost contract | 33% (1/3) | 50% (2/4) | -17 | 0.659 |  |
| llama3.2:3b | debias | Supply chain disruption | 33% (1/3) | 25% (1/4) | +8 | 0.809 |  |
| llama3.2:3b | debias | Fraud on customer accounts | 67% (2/3) | 33% (1/3) | +33 | 0.414 |  |
| llama3.2:3b | debias | A fund hit by a market shock | 0% (0/3) | 50% (2/4) | -50 | 0.147 |  |
| llama3.2:3b | debias | Loan defaults in a downturn | 33% (1/3) | 0% (0/4) | +33 | 0.212 |  |
| llama3.2:3b | debias | Reskilling during an AI rollout | 0% (0/3) | 50% (2/4) | -50 | 0.147 |  |
| llama3.2:3b | debias | Customer churn after an outage | 50% (2/4) | 50% (2/4) | +0 | 1.000 |  |
| llama3.2:3b | debias | Response to a security breach | 50% (2/4) | 75% (3/4) | -25 | 0.465 |  |
| qwen2.5:3b | baseline | Keeping staff after a merger | 0% (0/4) | 0% (0/4) | +0 | n/a | Same answer every time |
| qwen2.5:3b | baseline | Restructuring after a lost contract | 0% (0/4) | 0% (0/4) | +0 | n/a | Same answer every time |
| qwen2.5:3b | baseline | Supply chain disruption | 25% (1/4) | 0% (0/4) | +25 | 0.285 |  |
| qwen2.5:3b | baseline | Fraud on customer accounts | 0% (0/4) | 0% (0/4) | +0 | n/a | Same answer every time |
| qwen2.5:3b | baseline | A fund hit by a market shock | 0% (0/4) | 0% (0/4) | +0 | n/a | Same answer every time |
| qwen2.5:3b | baseline | Loan defaults in a downturn | 25% (1/4) | 0% (0/4) | +25 | 0.285 |  |
| qwen2.5:3b | baseline | Reskilling during an AI rollout | 50% (2/4) | 0% (0/4) | +50 | 0.102 |  |
| qwen2.5:3b | baseline | Customer churn after an outage | 0% (0/4) | 25% (1/4) | -25 | 0.285 |  |
| qwen2.5:3b | baseline | Response to a security breach | 0% (0/4) | 0% (0/4) | +0 | n/a | Same answer every time |
| qwen2.5:3b | debias | Keeping staff after a merger | 67% (2/3) | 0% (0/4) | +67 | 0.053 |  |
| qwen2.5:3b | debias | Restructuring after a lost contract | 75% (3/4) | 67% (2/3) | +8 | 0.809 |  |
| qwen2.5:3b | debias | Supply chain disruption | 75% (3/4) | 0% (0/4) | +75 | 0.028 |  |
| qwen2.5:3b | debias | Fraud on customer accounts | 50% (2/4) | 50% (2/4) | +0 | 1.000 |  |
| qwen2.5:3b | debias | A fund hit by a market shock | 50% (2/4) | 25% (1/4) | +25 | 0.465 |  |
| qwen2.5:3b | debias | Loan defaults in a downturn | 33% (1/3) | 67% (2/3) | -33 | 0.414 |  |
| qwen2.5:3b | debias | Reskilling during an AI rollout | 50% (2/4) | 25% (1/4) | +25 | 0.465 |  |
| qwen2.5:3b | debias | Customer churn after an outage | 50% (2/4) | 25% (1/4) | +25 | 0.465 |  |
| qwen2.5:3b | debias | Response to a security breach | 50% (2/4) | 25% (1/4) | +25 | 0.465 |  |

**Consistency across scenarios** (scenarios with a significant gap in the human direction, p < 0.05):

- llama3.2:3b, baseline: 0 of 9
- llama3.2:3b, debias: 0 of 9
- qwen2.5:3b, baseline: 0 of 9
- qwen2.5:3b, debias: 1 of 9

## Unreadable replies (left out of the analysis)

| Model | Prompt | Unreadable | Total |
|---|---|---|---|
| llama3.2:3b | baseline | 2 | 72 |
| llama3.2:3b | debias | 7 | 72 |
| qwen2.5:3b | baseline | 0 | 72 |
| qwen2.5:3b | debias | 4 | 72 |

Nine scenarios are tested per model and prompt, so about one in twenty could reach p < 0.05 by chance alone. The pooled results and the consistency count matter more than any single p-value.
