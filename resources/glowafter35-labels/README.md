# Cosmetic label and ingredient evidence register

Keep the exact label wording and its source separate from a marketing interpretation.

Associated with [woman-cute.com](https://woman-cute.com/), with an explicit affiliation. This is a practical resource, not an independent endorsement.

## Downloads

- [Workbook](modele.xlsx) — entry log, instructions, fictional inputs and computed example.
- [CSV entry template](trame.csv).
- [Fictional JSON scenario](exemple-fictif.json) and [computed output](resultat-exemple.json).

The workbook contains no automatic calculation formulas. For recalculation, download the full project, edit a private copy of the JSON scenario and run from the project directory:

```text
python -X utf8 run.py evidence_summary resources/glowafter35-labels/exemple-fictif.json
```

## What to record

- Product reference.
- Exact label wording.
- Ingredient name as printed.
- Manufacturer source.
- Market concerned.
- Checked date.
- State VERIFIED / MISSING / OUTDATED.
- Unresolved question.

## Method and limits

The `evidence_summary` calculation is implemented in [calculations.py](../../calculations.py) and covered by [automated tests](../../test_calculations.py). The supplied example was executed when the package was built; no actual client or product test results are included.

No ingredient list, efficacy, medical benefit or safety assessment is supplied. Ingredient naming requirements depend on the market.

Numeric results use floating-point arithmetic rounded to six decimal places, not an accounting ledger. All amounts must use consistent units and currencies. Keep real customer, financial and other private information outside this public repository.

## Reference

[Source reference](https://www.fda.gov/cosmetics/cosmetics-labeling/cosmetic-ingredient-names)
