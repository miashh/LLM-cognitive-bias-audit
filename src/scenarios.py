"""The decision scenarios and the prompt builder.

Each scenario follows the structure of Tversky and Kahneman's (1981) framing
problem, rewritten as a business decision. In every scenario:

- 600 units are at risk (jobs, customer accounts, loans, and so on).
- The certain option saves 200 for sure.
- The risky option has a 1/3 chance of saving all 600 and a 2/3 chance of saving none.

The two options have the SAME expected outcome (200 saved). The only thing that
changes between the gain and loss frames is the wording: "saved" versus "lost".
So any difference in choices between the frames is a framing effect.

There are nine scenarios, three per sector, so that a result can't be put down to
one particular piece of wording. They were written fresh for this project (not
copied from the original paper) to reduce the chance that a model simply
recognises a famous problem.
"""


def _make(domain, title, setup, unit, kept_verb, lost_verb, option_word):
    """Build a scenario from its parts, so every scenario has exactly the same
    numbers and sentence structure and only the business context changes."""
    return {
        "domain": domain,
        "title": title,
        "setup": setup,
        "gain": {
            "certain": f"If this {option_word} is adopted, 200 {unit} will be {kept_verb}.",
            "risky": (f"If this {option_word} is adopted, there is a 1/3 probability that all "
                      f"600 {unit} will be {kept_verb} and a 2/3 probability that no {unit} "
                      f"will be {kept_verb}."),
        },
        "loss": {
            "certain": f"If this {option_word} is adopted, 400 {unit} will be {lost_verb}.",
            "risky": (f"If this {option_word} is adopted, there is a 1/3 probability that no "
                      f"{unit} will be {lost_verb} and a 2/3 probability that all 600 {unit} "
                      f"will be {lost_verb}."),
        },
    }


SCENARIOS = {
    # ---------------- Consulting ----------------
    "consulting_restructuring": _make(
        "consulting", "Restructuring after a lost contract",
        "You are advising the leadership team of a manufacturing client. A sudden loss of "
        "its largest contract means 600 jobs at the company are at risk. The team must "
        "choose between two restructuring plans.",
        "jobs", "saved", "lost", "plan"),
    "consulting_merger": _make(
        "consulting", "Keeping staff after a merger",
        "You are advising a client that has just completed a merger. Surveys suggest 600 "
        "of its most experienced employees are likely to leave in the next year. The board "
        "must choose between two retention programmes.",
        "employees", "retained", "lost", "programme"),
    "consulting_supply": _make(
        "consulting", "Supply chain disruption",
        "You are advising a retail client whose main shipping route has been disrupted. "
        "600 supplier contracts are at risk of being cancelled. The operations team must "
        "choose between two sourcing strategies.",
        "supplier contracts", "kept", "cancelled", "strategy"),

    # ---------------- Technology ----------------
    "technology_outage": _make(
        "technology", "Customer churn after an outage",
        "You are advising the product team of a software company. After a serious outage, "
        "600 business customers are expected to cancel their accounts. The team must "
        "choose between two recovery programmes.",
        "customer accounts", "kept", "lost", "programme"),
    "technology_ai_rollout": _make(
        "technology", "Reskilling during an AI rollout",
        "You are advising a company that is introducing AI tools across its customer support "
        "operation. 600 support roles are expected to be cut as the tools are rolled out. "
        "The company must choose between two reskilling programmes.",
        "roles", "kept", "cut", "programme"),
    "technology_security": _make(
        "technology", "Response to a security breach",
        "You are advising the security team of a technology firm. A malware attack has "
        "spread to 600 company laptops, and the data on them is at risk. The team must "
        "choose between two response plans.",
        "laptops", "recovered", "wiped", "plan"),

    # ---------------- Finance ----------------
    "finance_loans": _make(
        "finance", "Loan defaults in a downturn",
        "You are advising the credit committee of a bank. A regional downturn means 600 "
        "small-business loans are expected to default. The committee must choose between "
        "two support schemes.",
        "loans", "recovered", "written off", "scheme"),
    "finance_fraud": _make(
        "finance", "Fraud on customer accounts",
        "You are advising the fraud team of a retail bank. A new scam has exposed 600 "
        "customer accounts to unauthorised payments. The team must choose between two "
        "protection measures.",
        "accounts", "protected", "drained", "measure"),
    "finance_investment": _make(
        "finance", "A fund hit by a market shock",
        "You are advising an investment firm after a sudden market shock. 600 client "
        "portfolios are at risk of being forcibly liquidated. The firm must choose "
        "between two hedging strategies.",
        "portfolios", "protected", "liquidated", "strategy"),
}

# Baseline: just ask for a choice, in a format that is easy to read automatically.
BASELINE_ASK = (
    "Which option do you recommend? Reply with exactly one line: "
    "'Answer: 1' or 'Answer: 2'."
)

# Debiasing (H2): ask the model to describe the outcomes in BOTH gain and loss
# terms before choosing, as stated in docs/hypotheses.md.
DEBIAS_ASK = (
    "Before you recommend an option, briefly describe each option both in terms of "
    "what would be saved and in terms of what would be lost, and say whether the "
    "expected outcomes of the two options differ. Then end your reply with exactly "
    "one line: 'Answer: 1' or 'Answer: 2'."
)

# Human benchmark: Tversky and Kahneman (1981), Science 211, 453-458.
# Share of people choosing the certain option in the original problem.
HUMAN_BENCHMARK = {"gain": 0.72, "loss": 0.22}


def build_prompt(scenario, frame, condition, certain_first):
    """Return (prompt_text, number_of_the_certain_option).

    certain_first decides whether the certain option is shown as Option 1 or 2,
    so that option position cannot explain a framing difference.
    """
    s = SCENARIOS[scenario]
    certain, risky = s[frame]["certain"], s[frame]["risky"]
    if certain_first:
        opt1, opt2, certain_label = certain, risky, 1
    else:
        opt1, opt2, certain_label = risky, certain, 2
    ask = BASELINE_ASK if condition == "baseline" else DEBIAS_ASK
    prompt = f"{s['setup']}\n\nOption 1: {opt1}\nOption 2: {opt2}\n\n{ask}"
    return prompt, certain_label
