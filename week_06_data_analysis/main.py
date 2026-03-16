"""
Week 6 – CSV Data Analysis
----------------------------
Analyses a sales CSV file and produces a human-readable report plus a
summary CSV.

Requirements:
    pip install pandas
"""

from pathlib import Path

import pandas as pd

DATA_FILE = Path(__file__).parent / "sales_data.csv"
REPORT_FILE = Path(__file__).parent / "sales_report.csv"


def load_data(path: Path = DATA_FILE) -> pd.DataFrame:
    """Load the sales CSV and add derived columns."""
    df = pd.read_csv(path, parse_dates=["date"])
    df["revenue"] = df["quantity"] * df["unit_price"]
    df["month"] = df["date"].dt.to_period("M")
    return df


def total_revenue(df: pd.DataFrame) -> float:
    return df["revenue"].sum()


def best_selling_product(df: pd.DataFrame) -> tuple[str, int]:
    """Return (product_name, total_units_sold) for the top product."""
    grouped = df.groupby("product")["quantity"].sum()
    product = grouped.idxmax()
    return product, int(grouped[product])


def revenue_by_category(df: pd.DataFrame) -> pd.Series:
    """Return a Series of total revenue indexed by category, sorted desc."""
    return df.groupby("category")["revenue"].sum().sort_values(ascending=False)


def monthly_revenue(df: pd.DataFrame) -> pd.Series:
    """Return a Series of total revenue indexed by month string, sorted desc."""
    return (
        df.groupby("month")["revenue"]
        .sum()
        .sort_values(ascending=False)
    )


def save_report(df: pd.DataFrame, path: Path = REPORT_FILE) -> None:
    """Save a per-product summary to *path*."""
    summary = (
        df.groupby(["category", "product"])
        .agg(total_units=("quantity", "sum"), total_revenue=("revenue", "sum"))
        .sort_values("total_revenue", ascending=False)
        .reset_index()
    )
    summary.to_csv(path, index=False)


def print_report(df: pd.DataFrame) -> None:
    print("=== Sales Report ===")
    print(f"Total revenue: ${total_revenue(df):,.2f}")

    product, units = best_selling_product(df)
    print(f"Best-selling product: {product} ({units} units)\n")

    print("Revenue by category:")
    for cat, rev in revenue_by_category(df).items():
        print(f"  {cat:<15} ${rev:,.0f}")

    print("\nMonthly trend (top 5 months):")
    for month, rev in monthly_revenue(df).head(5).items():
        print(f"  {month}   ${rev:,.0f}")

    save_report(df)
    print(f"\nDetailed report saved to {REPORT_FILE}")


def main() -> None:
    df = load_data()
    print_report(df)


if __name__ == "__main__":
    main()
