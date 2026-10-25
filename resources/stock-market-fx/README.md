# Cross-currency purchase cost worksheet

Convert a hypothetical purchase using an explicit exchange-rate direction, then add the supplied commission.

Associated with [stock-market.ch](https://stock-market.ch/), with an explicit affiliation. This is a practical resource, not an independent endorsement.

## Downloads

- [Workbook](modele.xlsx) — entry log, instructions, fictional inputs and computed example.
- [CSV entry template](trame.csv).
- [Fictional JSON scenario](exemple-fictif.json) and [computed output](resultat-exemple.json).

The workbook contains no automatic calculation formulas. For recalculation, download the full project, edit a private copy of the JSON scenario and run from the project directory:

```text
python -X utf8 run.py fx_cost resources/stock-market-fx/exemple-fictif.json
```

## What to record

- Instrument reference.
- Quantity.
- Unit price in quote currency.
- Home units per quote unit.
- Commission in home currency.
- Source and timestamp.
- Other excluded costs.

## Method and limits

The `fx_cost` calculation is implemented in [calculations.py](../../calculations.py) and covered by [automated tests](../../test_calculations.py). The supplied example was executed when the package was built; no actual client or product test results are included.

No market quote or FX rate is fetched. Taxes, spread and future returns are excluded unless included explicitly in the inputs.

Numeric results use floating-point arithmetic rounded to six decimal places, not an accounting ledger. All amounts must use consistent units and currencies. Keep real customer, financial and other private information outside this public repository.
