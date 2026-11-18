# Hypotheses
(Written before running any experiments)

## Research question
Do large language models show human cognitive biases in business decisions, and can prompting reduce them?

## H1: framing effect
The model will choose the certain option more often when outcomes are described as gains than when the same outcomes are described as losses. This is the pattern people show (Tversky and Kahneman, 1981), so a difference would mean the model is also influenced by how a choice is worded.

## H2: debiasing
Adding an instruction to consider the outcomes in both gain and loss terms before answering will reduce the difference between the two conditions.

## How I will measure it
- For each scenario, I will compare the share of runs that choose the certain option in the gain frame and in the loss frame.
- Around 30 runs per condition, with the order of options randomised.
- I will compare the two shares using a test for a difference in proportions.

## What would count against H1
- No difference between the gain and loss conditions.
- A difference in the opposite direction.
- The model giving the same answer every time whatever the wording. This would suggest the scenario is too easy, so I would redesign it and not report it as a result.

## Exploratory (not predicted)
Differences between sectors (consulting, technology, finance) and between models. These will be reported as exploratory only.

## Amendment (November 2026, before any experiment was run)
To test whether any framing effect holds across different business contexts, rather than depending on one piece of wording, I added two more scenarios per sector, giving nine in total (three each for consulting, technology and finance). Every scenario uses the same numbers and sentence structure; only the business context changes.

Nothing else changes: H1 and H2 are exactly as above, there are still around 30 runs per condition in each scenario, and sector differences remain exploratory. I also added two summaries: the result pooled across all nine scenarios, and a count of how many scenarios show a significant effect in the human direction. Results are compared with the original human result (Tversky and Kahneman, 1981: 72% chose the certain option with gain wording and 22% with loss wording).

## Amendment 2 (November 2026, after the pilot and before the full runs)
A pilot (4 runs per cell, 288 replies, not included in the results) showed two things:

1. Some replies to the debiasing prompt were cut off before the final "Answer" line, because they hit the reply length limit. I raised the limit from 500 to 900 tokens for that prompt.
2. With the debiasing prompt, both models chose whichever option was listed first much more often than the other. Option order was already balanced in every cell, so this cannot create a framing gap, but I added an exploratory table that reports it.

The scenarios, the prompts, the hypotheses, the number of runs and the rule for unreadable replies are unchanged. I did not change anything to make a framing effect more likely to appear.
