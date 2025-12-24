import matplotlib.pyplot as plt
from src.data_ingestion import load_json_data
from src.data_preprocessing import clean_data, aggregate_daily


def run_eda():
    df = load_json_data("data/cs-train")
    df = clean_data(df)
    daily_df = aggregate_daily(df)

    # Revenue over time
    plt.figure(figsize=(12, 5))
    daily_df.groupby("date")["daily_revenue"].sum().plot()
    plt.title("Total Daily Revenue Over Time")
    plt.ylabel("Revenue")
    plt.xlabel("Date")
    plt.tight_layout()
    plt.savefig("images/revenue_timeseries.png")
    plt.close()

    # Top 10 countries by revenue
    top_countries = (
        daily_df.groupby("country")["daily_revenue"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    plt.figure(figsize=(10, 5))
    top_countries.plot(kind="bar")
    plt.title("Top 10 Countries by Total Revenue")
    plt.ylabel("Revenue")
    plt.tight_layout()
    plt.savefig("images/top_countries.png")
    plt.close()


if __name__ == "__main__":
    run_eda()
