# Scripts

Two runnable example scripts demonstrating the data-pipeline shape of the original operating system. Both use only fictional data. Nothing personal.

## What is here

| Script | Pattern demonstrated |
|---|---|
| [expense_pipeline_example.py](expense_pipeline_example.py) | Multi-CSV input, taxonomy classification with override rules, multi-sheet Excel output. The original (`build_ssot.py`) is around 1,500 lines and handles refund pairing, multi-currency normalisation, duplicate detection across overlapping statements, recurring-vendor patterns, and per-account reconciliation. |
| [net_worth_dashboard_example.py](net_worth_dashboard_example.py) | Holdings, allocation, FIRE projection, tabbed HTML dashboard. The original (`generate_nw_dashboard.py`) is around 1,000 lines and handles real multi-account, multi-currency, multi-asset-class data with full historical projections and scenario modelling. |

## Sample data

`sample_data/bank.csv` and `sample_data/cards.csv` contain around 75 fictional transactions across three months. Merchant names are generic ("Coffee Shop A", "Online Shop C") so the pipeline's classification logic is observable without exposing any real spending pattern.

## How to run

```
cd scripts
python3 expense_pipeline_example.py
python3 net_worth_dashboard_example.py
```

Outputs in the current directory:

- `output_example.xlsx`: three sheets (Transactions, Summary, Monthly Breakdown).
- `example_dashboard.html`: open in any browser.

Both output files are gitignored.

## Requirements

The expense pipeline needs pandas and openpyxl:

```
pip install pandas openpyxl
```

The dashboard script uses only the Python standard library.

## Why the originals are not in this repo

The originals contain personal financial data, account structure, and account-specific quirks (statement formats, currency handling, vendor patterns). The point of these examples is to show the pattern, not the data. If you want to build your own version, the shape is here. The taxonomy, the override rules, and the holdings are yours to define.

## What to adapt first

Open `expense_pipeline_example.py` and change:

1. The `TAXONOMY` dictionary to match your own spending categories.
2. The `OVERRIDES` dictionary to fix any merchants the taxonomy mislabels.
3. Drop your own bank or card CSVs into `sample_data/`. The pipeline reads every `.csv` in that folder.

Open `net_worth_dashboard_example.py` and change:

1. The `HOLDINGS` list to your real positions.
2. `MONTHLY_CONTRIBUTION`, `ANNUAL_GROWTH_RATE`, `TARGET_CORPUS` to your own projection inputs.
3. `CURRENCY_SYMBOL` to your local currency.

That gets you a working personal dashboard. Everything beyond that (loan amortisation, multi-currency, scenario modelling) is incremental.
