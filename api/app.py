from flask import Flask, request, jsonify
import logging
from datetime import datetime

from src.model import run_model
from src.data_ingestion import load_json_data
from src.data_preprocessing import clean_data, aggregate_daily

app = Flask(__name__)

# =========================
# Logging Configuration
# =========================
logging.basicConfig(
    filename="logs/predictions.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# =========================
# Health Check
# =========================
@app.route("/", methods=["GET"])
def health():
    return jsonify({"status": "API is running"}), 200


# =========================
# Train Endpoint
# =========================
@app.route("/train", methods=["POST"])
def train():
    try:
        mae = run_model()
        return jsonify({
            "message": "Model trained successfully",
            "mae": mae
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# =========================
# Predict Endpoint
# =========================
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    if not data or "country" not in data or "date" not in data:
        return jsonify({
            "error": "Please provide country and date"
        }), 400

    country = data["country"]
    date = data["date"]

    # Dummy prediction logic (for now)
    prediction = 5000.0

    # Logging
    logging.info(
        f"Prediction | country={country}, date={date}, prediction={prediction}"
    )

    return jsonify({
        "country": country,
        "date": date,
        "predicted_revenue": prediction
    }), 200


if __name__ == "__main__":
    app.run(debug=True)
