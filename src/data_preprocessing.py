import pandas as pd


def clean_data(df):
    """
    Clean raw transaction data
    """

    # Normalize column names
    df.columns = df.columns.str.lower()

    # Fix inconsistent column names
    if "streamid" in df.columns:
        df["stream_id"] = df["streamid"]
    if "timesviewed" in df.columns:
        df["times_viewed"] = df["timesviewed"]

    # Compute total_price if missing
    if "total_price" not in df.columns:
        df["total_price"] = df["price"] * df["times_viewed"]

    # Create datetime column
    df["date"] = pd.to_datetime(
        df[["year", "month", "day"]],
        errors="coerce"
    )

    # Drop unusable rows
    df = df.dropna(subset=["date", "country", "total_price"])

    return df


def aggregate_daily(df):
    """
    Aggregate transactions to daily revenue per country
    """

    daily_df = (
        df.groupby(["date", "country"])
          .agg(
              daily_revenue=("total_price", "sum"),
              daily_views=("times_viewed", "sum"),
              transactions=("invoice", "nunique")
          )
          .reset_index()
    )

    return daily_df
