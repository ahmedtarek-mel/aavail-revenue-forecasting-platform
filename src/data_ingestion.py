import json
import pandas as pd
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


def load_json_data(relative_path):
    """
    Load all JSON files from a directory into a single DataFrame
    """
    data_dir = BASE_DIR / relative_path
    records = []

    json_files = list(data_dir.glob("*.json"))

    print(f"Reading from: {data_dir}")
    print(f"Found {len(json_files)} JSON files")

    for file in json_files:
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)
            records.extend(data)

    return pd.DataFrame(records)


if __name__ == "__main__":
    train_df = load_json_data("data/cs-train")
    prod_df = load_json_data("cs-production")

    print("Train shape:", train_df.shape)
    print("Production shape:", prod_df.shape)

    print(train_df.head())
