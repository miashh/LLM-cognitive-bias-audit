# Hypotheses
(Written before running any experiments).

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
