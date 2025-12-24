import pandas as pd
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

from src.data_ingestion import load_json_data
from src.data_preprocessing import clean_data, aggregate_daily


def create_features(df):
    """
    Create lag features for time-series regression
    """
    df = df.sort_values("date")

    df["lag_1"] = df["daily_revenue"].shift(1)
    df["lag_7"] = df["daily_revenue"].shift(7)

    df["day"] = df["date"].dt.day
    df["month"] = df["date"].dt.month

    return df.dropna()


def run_model(data_path="data/cs-train"):
    # 1️ Load + preprocess
    df = load_json_data(data_path)
    df = clean_data(df)
    daily_df = aggregate_daily(df)

    # 2️ Aggregate over all countries
    company_daily = (
        daily_df
        .groupby("date")
        .agg({
            "daily_revenue": "sum",
            "daily_views": "sum",
            "transactions": "sum"
        })
        .reset_index()
    )

    # 3️ Feature engineering
    company_daily = create_features(company_daily)

    FEATURES = ["lag_1", "lag_7", "daily_views", "transactions", "day", "month"]
    TARGET = "daily_revenue"

    X = company_daily[FEATURES]
    y = company_daily[TARGET]

    # 4️ Train / Test split (time-based)
    split_idx = int(len(company_daily) * 0.8)
    X_train, X_test = X.iloc[:split_idx], X.iloc[split_idx:]
    y_train, y_test = y.iloc[:split_idx], y.iloc[split_idx:]

    # 5️ Train model
    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )
    model.fit(X_train, y_train)

    # 6️ Predict
    preds = model.predict(X_test)

    # 7️ Evaluation
    mae = mean_absolute_error(y_test, preds)
    print(f" MAE: {mae:.2f}")

    # 8️ Plot comparison
    plt.figure(figsize=(12, 6))
    plt.plot(y_test.values, label="Actual Revenue")
    plt.plot(preds, label="ML Prediction")
    plt.title("ML Model vs Actual Revenue")
    plt.xlabel("Time")
    plt.ylabel("Revenue")
    plt.legend()
    plt.tight_layout()

    plt.savefig("images/model_vs_actual.png")
    plt.close()

    print(" ML model finished")
    print(" Plot saved to images/model_vs_actual.png")

    return mae


if __name__ == "__main__":
    run_model()
