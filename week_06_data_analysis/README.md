# Week 6: CSV Data Analysis

**Difficulty:** Intermediate → Advanced

## Learning Goals
- Read and process CSV files with `pandas`
- Compute descriptive statistics
- Filter and sort DataFrames
- Generate summary reports and basic plots

## Project Description
Analyse a sales dataset (bundled as `sales_data.csv`).  Compute totals per
product category, find the best-selling product, identify monthly trends, and
produce a text summary report.

## Concepts Covered
- `pandas.read_csv()` and DataFrame operations
- `groupby()`, `agg()`, `sort_values()`
- Date parsing and period extraction
- Writing results to a new CSV
- Optional: matplotlib bar chart

## Setup
```bash
pip install pandas matplotlib
```

## How to Run
```bash
python main.py
```

## Sample Output
```
=== Sales Report ===
Total revenue: $124,530.00
Best-selling product: Laptop (350 units)

Revenue by category:
  Electronics  $78,200
  Clothing     $30,100
  Books        $16,230

Monthly trend (top 3 months):
  2024-03   $18,400
  2024-11   $15,200
  2024-07   $12,950

Report saved to sales_report.csv
```

## Challenges
1. Add a matplotlib bar chart saved as `revenue_by_category.png`.
2. Detect and handle missing or malformed data rows.
3. Accept the CSV filename as a command-line argument.
