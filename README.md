<p align="center">
  <img src="images/AAVAIL Banner.png" width="100%">
</p>

# 🟦 AAVAIL Revenue Forecasting Platform  

[![Python](https://img.shields.io/badge/Python-3.10-blue.svg)]()
[![Model](https://img.shields.io/badge/Model-RandomForest-success)]()
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Build](https://img.shields.io/badge/Build-Passing-brightgreen)
![Tests](https://img.shields.io/badge/Tests-PyTest-success)
![Deployment](https://img.shields.io/badge/API-Flask-informational)

---

## 📈 Project Overview  
This project implements a **production-oriented machine learning system** designed to forecast daily revenue for **AAVAIL**, a global digital streaming platform operating across multiple countries.

The system reflects a **real enterprise AI workflow**, covering the full lifecycle:
from raw transactional data ingestion to model deployment, monitoring, and testing.

**Primary Objective:**  
➡️ Predict **daily revenue** at the country level using historical transaction data  
➡️ Enable data-driven planning, budgeting, and operational decision-making

---

## 🧠 Business Context  
Accurate revenue forecasting is a critical component for:
- Financial planning  
- Resource allocation  
- Market performance monitoring  
- Strategic expansion decisions  

This project focuses on transforming raw transactional data into actionable revenue forecasts using time-series regression techniques.

---

## 📂 Repository Structure  

```
AAVAIL Revenue Forecasting/
│
├── data/
│ ├── cs-train/ # Historical transaction JSON files
│ └── cs-production/ # Production-style JSON samples
│
├── src/
│ ├── data_ingestion.py # Automated data ingestion
│ ├── data_preprocessing.py # Cleaning & daily aggregation
│ ├── eda.py # Exploratory data analysis
│ ├── baseline.py # Baseline forecasting model
│ └── model.py # Machine learning model
│
├── api/
│ └── app.py # Flask-based REST API
│
├── tests/
│ ├── test_data.py # Data pipeline tests
│ ├── test_model.py # Model tests
│ └── test_api.py # API endpoint tests
│
├── images/
│ ├── revenue_timeseries.png
│ ├── top_countries.png
│ ├── baseline_vs_actual.png
│ └── model_vs_actual.png
│
├── logs/
│ └── predictions.log # Prediction audit logs
│
├── Dockerfile
├── requirements.txt
└── README.md

```

---

## 📊 Dataset  
**Source:** Transaction-level JSON data  
**Granularity:** Individual purchases  
**Final Modeling Level:** Daily aggregation per country  

Key engineered fields:
- Daily revenue  
- Transaction count  
- Engagement metrics (views)  
- Date-based features  

---

## 🔧 Methodology  

### 1️⃣ Data Ingestion
- Automated ingestion of monthly JSON files
- Schema normalization and error handling
- Robust handling of inconsistent column naming

### 2️⃣ Data Preprocessing
- Revenue calculation
- Date parsing and normalization
- Aggregation to daily country-level metrics

### 3️⃣ Exploratory Data Analysis
EDA was conducted to:
- Identify revenue trends and seasonality
- Compare country-level revenue contributions
- Understand temporal patterns in transactions

Key observations:
- Strong seasonal revenue spikes toward year-end
- Revenue concentration in a small number of countries
- High correlation between transactions and revenue

All visual outputs are stored in the `images/` directory.

---

## 🤖 Modeling Strategy  

### Baseline Model
A simple historical-average baseline model was implemented to establish a reference performance benchmark.

### Machine Learning Model
- Algorithm: **Random Forest Regressor**
- Input: Engineered daily features
- Evaluation Metric: **Mean Absolute Error (MAE)**

**Final ML Model Performance:**
- **MAE ≈ 2756**

> This is a regression problem; therefore, model performance is evaluated using MAE rather than accuracy.

---

## 📉 Model Evaluation
Visual comparisons were created to assess:
- Actual vs baseline predictions
- Actual vs ML predictions
- Error behavior during seasonal peaks

These comparisons provide transparency into model strengths and limitations.

---

## 🌐 API Service  

A RESTful API was developed using **Flask** to simulate a production deployment environment.

### Available Endpoints
- `GET /` — Health check  
- `POST /train` — Train the forecasting model  
- `POST /predict` — Generate revenue predictions for a given country and date  

All prediction requests are logged for monitoring and traceability.

---

## 🧪 Testing & Reliability

The project includes **automated unit tests** designed to ensure correctness, stability, and long-term reliability across the entire pipeline.

### ✔️ Test Coverage
Unit tests validate the following components:
- **Data ingestion & preprocessing logic**
- **Model training and execution**
- **API endpoints and request handling**

### ▶️ Running Tests
All tests can be executed using a single command:

```bash
python -m pytest

```
- Running tests before deployment ensures reproducibility, early error detection, and protection against unintended regressions.

###  🐳 Containerization

- The application is fully containerized using Docker, enabling consistent execution across different environments.

### ✔️ Benefits

- Environment consistency across development and production

- Portability across operating systems and cloud platforms

- Simplified deployment and scalability

- A production-ready Dockerfile is included in the project root for seamless container builds.

### 🧰 Technology Stack

The project is built using a modern, production-oriented technology stack:

- Python

- Pandas, NumPy

- Scikit-learn

- Matplotlib

- Flask

- Pytest

- Docker

### 🧾 Final Notes

- This project demonstrates a real-world, production-style AI workflow, with a strong emphasis on:

- Modular architecture

- Reproducibility

- Testing & reliability

- Monitoring readiness

- Deployment-first design

- The implementation intentionally prioritizes engineering best practices and system robustness over purely academic modeling results — reflecting how machine learning systems are built and maintained in real production environments.