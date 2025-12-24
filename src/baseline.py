import pandas as pd
import matplotlib.pyplot as plt

from src.data_ingestion import load_json_data
from src.data_preprocessing import clean_data, aggregate_daily


def run_baseline(data_path="data/cs-train"):
    """
    Baseline model:
    Predict next day's revenue using previous day's revenue
    """

    # 1️ Load + clean data
    df = load_json_data(data_path)
    df = clean_data(df)
    daily_df = aggregate_daily(df)

    # 2️ Aggregate over ALL countries (company-level revenue)
    company_daily = (
        daily_df
        .groupby("date")["daily_revenue"]
        .sum()
        .reset_index()
        .sort_values("date")
    )

    # 3️ Baseline prediction = previous day's revenue
    company_daily["baseline_prediction"] = company_daily["daily_revenue"].shift(1)

    # Drop first row (no previous day)
    company_daily = company_daily.dropna()

    # 4️ Plot comparison
    plt.figure(figsize=(12, 6))
    plt.plot(company_daily["date"], company_daily["daily_revenue"], label="Actual Revenue")
    plt.plot(company_daily["date"], company_daily["baseline_prediction"], label="Baseline Prediction")
    plt.title("Baseline Model vs Actual Revenue")
    plt.xlabel("Date")
    plt.ylabel("Revenue")
    plt.legend()
    plt.tight_layout()

    # 5️ Save figure
    plt.savefig("images/baseline_vs_actual.png")
    plt.close()

    print(" Baseline model finished")
    print(" Plot saved to images/baseline_vs_actual.png")

    return company_daily


if __name__ == "__main__":
    run_baseline()
