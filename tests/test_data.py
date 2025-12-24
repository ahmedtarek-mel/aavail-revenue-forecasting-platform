import pandas as pd
from src.data_ingestion import load_json_data
from src.data_preprocessing import clean_data, aggregate_daily


def test_data_ingestion():
    df = load_json_data("data/cs-train")
    assert not df.empty
    assert "country" in df.columns


def test_preprocessing():
    df = load_json_data("data/cs-train")
    df = clean_data(df)
    daily = aggregate_daily(df)

    assert not daily.empty
    assert "daily_revenue" in daily.columns
