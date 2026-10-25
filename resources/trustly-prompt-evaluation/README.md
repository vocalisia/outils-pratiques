# Prompt-pack acceptance test log

Evaluate a prompt pack against explicit fixtures, edge cases and reproducible acceptance criteria.

Associated with [trustly-ai.com](https://trustly-ai.com/), with an explicit affiliation. This is a practical resource, not an independent endorsement.

## Downloads

- [Workbook](modele.xlsx) — entry log, instructions, fictional inputs and computed example.
- [CSV entry template](trame.csv).
- [Fictional JSON scenario](exemple-fictif.json) and [computed output](resultat-exemple.json).

The workbook contains no automatic calculation formulas. For recalculation, download the full project, edit a private copy of the JSON scenario and run from the project directory:

```text
python -X utf8 run.py test_summary resources/trustly-prompt-evaluation/exemple-fictif.json
```

## What to record

- Prompt identifier.
- Input fixture.
- Model and version used.
- Acceptance criterion.
- Observed output reference.
- Status PASS / FAIL / NOT_RUN.
- Reproduction steps.

## Method and limits

The `test_summary` calculation is implemented in [calculations.py](../../calculations.py) and covered by [automated tests](../../test_calculations.py). The supplied example was executed when the package was built; no actual client or product test results are included.

The example statuses are fictional. No income, savings or paid-model performance is claimed, and this tool calls no model API.

Numeric results use floating-point arithmetic rounded to six decimal places, not an accounting ledger. All amounts must use consistent units and currencies. Keep real customer, financial and other private information outside this public repository.
