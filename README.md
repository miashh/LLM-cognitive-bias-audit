# Do large language models show human cognitive biases in business decisions, and can prompting reduce them?

**Status: in progress.**

## Question
Large language models are increasingly used to support business decisions. People make predictable errors in judgement, such as being swayed by how a choice is framed (Tversky and Kahneman, 1981). This project tests whether language models show the same framing effect in consulting, technology, and finance scenarios, and whether adding a debiasing instruction to the prompt reduces it. For each scenario, I compare how often the model chooses the certain option when identical outcomes are described as gains versus losses.

## Method
(Scenarios, how prompts differ between conditions, number of runs, models used, how answers were recorded.)

## Results
(Fill in only from real runs: one table and one chart, plus two sentences on what they show.)

## Limitations
(Be specific. For example: classic bias problems may appear in model training data; results depend on model version; small number of scenarios.)

## How to run
1. `pip install -r requirements.txt`
2. Copy `.env.example` to `.env` and add your API key
3. `python src/test_call.py`
