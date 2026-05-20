#!/usr/bin/env python3
"""
expense_pipeline_example.py

Demonstrates the multi-CSV expense pipeline pattern used by the original
operating system. Reads bank and card CSVs from sample_data/, classifies
each transaction via a taxonomy plus override rules, aggregates by
category and by month, and writes a multi-sheet Excel workbook.

The original at the source operating system runs to roughly 1,500 lines
and handles many more edge cases: refund pairing, multi-currency
normalisation, duplicate detection across overlapping statements,
recurring-vendor patterns, expense versus investment splits, and per
account reconciliation. This file demonstrates the shape only.

Run:
    python3 expense_pipeline_example.py

Requires:
    pandas, openpyxl

Output:
    output_example.xlsx in the current directory.
"""
import sys
from pathlib import Path

try:
    import pandas as pd
except ImportError:
    print("This script requires pandas. Install with: pip install pandas openpyxl", file=sys.stderr)
    sys.exit(1)


SCRIPT_DIR = Path(__file__).resolve().parent
SAMPLE_DATA = SCRIPT_DIR / "sample_data"
OUTPUT_FILE = SCRIPT_DIR / "output_example.xlsx"


# Taxonomy: category to list of lowercase substring keywords matched against description.
TAXONOMY = {
    "Food & Drink":      ["coffee", "cafe", "restaurant", "diner"],
    "Groceries":         ["grocery", "supermarket", "farmer"],
    "Transport":         ["uber", "taxi", "metro", "fuel", "petrol"],
    "Bills & Utilities": ["electric", "water", "gas", "internet", "telecom"],
    "Entertainment":     ["cinema", "streaming", "concert", "club"],
    "Shopping":          ["shop", "store", "retail", "online"],
    "Income":            ["salary", "deposit", "refund"],
    "Transfer":          ["transfer", "rtgs", "neft"],
}

# Overrides beat the taxonomy. Use these for merchants the taxonomy mislabels.
# Example: "Coffee Shop X" would match "shop" and be tagged Shopping; the override fixes it.
OVERRIDES = {
    "Coffee Shop X":  "Food & Drink",
    "Vendor A":       "Bills & Utilities",
    "Subscription B": "Entertainment",
}


def load_transactions(folder: Path) -> pd.DataFrame:
    """Read every CSV in `folder` into one DataFrame, tagging the source."""
    frames = []
    for csv_path in sorted(folder.glob("*.csv")):
        df = pd.read_csv(csv_path)
        df["source"] = csv_path.stem
        frames.append(df)
    if not frames:
        raise FileNotFoundError(f"No CSV files found in {folder}")
    combined = pd.concat(frames, ignore_index=True)
    combined["date"] = pd.to_datetime(combined["date"])
    return combined


def classify(description: str) -> str:
    """Map a description to a category. Overrides beat the taxonomy."""
    if description in OVERRIDES:
        return OVERRIDES[description]
    lowered = description.lower()
    for category, keywords in TAXONOMY.items():
        if any(keyword in lowered for keyword in keywords):
            return category
    return "Uncategorised"


def enrich(df: pd.DataFrame) -> pd.DataFrame:
    df["category"] = df["description"].apply(classify)
    df["month"] = df["date"].dt.to_period("M").astype(str)
    return df


def summarise(df: pd.DataFrame) -> pd.DataFrame:
    spend = df[df["type"] == "debit"]
    summary = (
        spend.groupby("category")["amount"]
        .agg(["sum", "count"])
        .reset_index()
        .rename(columns={"sum": "total_spend", "count": "transaction_count"})
        .sort_values("total_spend", ascending=False)
    )
    return summary


def monthly_breakdown(df: pd.DataFrame) -> pd.DataFrame:
    spend = df[df["type"] == "debit"]
    pivot = spend.pivot_table(
        index="category",
        columns="month",
        values="amount",
        aggfunc="sum",
        fill_value=0,
    )
    pivot["total"] = pivot.sum(axis=1)
    return pivot.sort_values("total", ascending=False).reset_index()


def write_workbook(transactions, summary, monthly, output_path):
    with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
        transactions.to_excel(writer, sheet_name="Transactions", index=False)
        summary.to_excel(writer, sheet_name="Summary", index=False)
        monthly.to_excel(writer, sheet_name="Monthly Breakdown", index=False)


def main():
    print(f"Reading sample data from {SAMPLE_DATA}")
    transactions = load_transactions(SAMPLE_DATA)
    print(f"Loaded {len(transactions)} transactions across {transactions['source'].nunique()} sources.")

    transactions = enrich(transactions)
    summary = summarise(transactions)
    monthly = monthly_breakdown(transactions)

    write_workbook(transactions, summary, monthly, OUTPUT_FILE)
    print(f"Wrote {OUTPUT_FILE}")

    print("\nTop categories by spend:")
    for _, row in summary.head(5).iterrows():
        print(f"  {row['category']:<20} {row['total_spend']:>10,.2f}  ({row['transaction_count']} txns)")


if __name__ == "__main__":
    main()
