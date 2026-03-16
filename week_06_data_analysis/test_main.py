"""Tests for Week 6 – CSV Data Analysis."""

import pandas as pd
import pytest
from week_06_data_analysis.main import (
    best_selling_product,
    load_data,
    monthly_revenue,
    revenue_by_category,
    save_report,
    total_revenue,
)

DATA_FILE = __import__("week_06_data_analysis.main", fromlist=["DATA_FILE"]).DATA_FILE


@pytest.fixture
def df():
    return load_data(DATA_FILE)


def test_load_data_columns(df):
    assert "revenue" in df.columns
    assert "month" in df.columns


def test_total_revenue_positive(df):
    assert total_revenue(df) > 0


def test_best_selling_product_returns_tuple(df):
    product, units = best_selling_product(df)
    assert isinstance(product, str)
    assert units > 0


def test_revenue_by_category_sorted(df):
    series = revenue_by_category(df)
    values = series.tolist()
    assert values == sorted(values, reverse=True)


def test_monthly_revenue_sorted(df):
    series = monthly_revenue(df)
    values = series.tolist()
    assert values == sorted(values, reverse=True)


def test_save_report(df, tmp_path):
    out = tmp_path / "report.csv"
    save_report(df, path=out)
    saved = pd.read_csv(out)
    assert "total_revenue" in saved.columns
    assert len(saved) > 0
