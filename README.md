# Financial Fraud Detection Pipeline & Application

## Overview
This repository contains an end-to-end Machine Learning solution for detecting fraudulent financial transactions. Designed with a focus on clear technical delivery, the project features a robust scikit-learn classification pipeline and an interactive Streamlit web application for real-time inference. 

## Repository Structure
* **`fraud_detection.ipynb`**: The core research notebook. Contains the data exploration, feature engineering, pipeline construction, model training, and performance evaluation.
* **`fraud_detection_pipeline.pkl`**: The serialized machine learning pipeline. This object encapsulates both the preprocessing steps and the trained classification model to ensure consistent data handling between training and production.
* **`fraud_detection.py`**: The Streamlit frontend application. Provides a clean, user-friendly interface to input transaction details and receive immediate fraud predictions.

## Model Architecture & Pipeline
The predictive model handles both numeric and categorical data through a unified `sklearn.compose.ColumnTransformer`:
* **Numeric Features** (`amount`, `oldbalanceOrg`, `newbalanceOrig`, `oldbalanceDest`, `newbalanceDest`): Standardized using `StandardScaler` to ensure zero mean and unit variance.
* **Categorical Features** (`type`): Encoded using `OneHotEncoder` to process various transaction types (PAYMENT, TRANSFER, CASH_OUT, DEPOSIT).

### Performance Metrics
The model was rigorously evaluated on a holdout test set, prioritizing the identification of actual fraudulent behavior (Recall). 
* **Overall Accuracy:** ~94.7%
* **Confusion Matrix Insights:** The model successfully identified **2,324 true positive** fraud cases against only 140 false negatives, demonstrating a highly effective recall rate for anomalous transactions.

## Installation & Setup
To run the web application locally, ensure you have Python installed and the necessary dependencies configured.

1. **Install dependencies:**
   ```bash
   pip install pandas scikit-learn streamlit joblib

2.**Run the Streamlit App**
 ```bash
   streamlit run fraud_detection.py
