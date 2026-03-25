import pandas as pd
import joblib

# Load artifacts
model = joblib.load("model/xgb_model.pkl")
label_encoders = joblib.load("model/label_encoders.pkl")
scaler = joblib.load("model/scaler.pkl")
metadata = joblib.load("model/metadata.pkl")   # contains feature names, num_cols

X_columns = metadata["X_columns"]
num_cols  = metadata["num_cols"]

def predict_custom(sample: dict):
    """
    Make prediction on a single new transaction.

    sample = {
        "From Bank": int,
        "To Bank": int,
        "Amount Received": float,
        "Receiving Currency": "US Dollar",
        "Amount Paid": float,
        "Payment Currency": "US Dollar",
        "Payment Format": "ACH"
    }
    """
    # Encode categorical fields
    sample_enc = sample.copy()
    for col, le in label_encoders.items():
        if col in sample_enc:
            sample_enc[col] = int(le.transform([sample_enc[col]])[0])

    # Feature engineering
    sample_enc["Amount Difference"] = abs(sample_enc["Amount Received"] - sample_enc["Amount Paid"])
    sample_enc["Amount Ratio"] = sample_enc["Amount Received"] / (sample_enc["Amount Paid"] + 1e-6)
    sample_enc["Same Currency"] = int(sample_enc["Receiving Currency"] == sample_enc["Payment Currency"])
    # Default to 1 if unseen bank
    sample_enc["From Tx Count"] = 1
    sample_enc["To Tx Count"] = 1

    # Build dataframe with correct column order
    df_in = pd.DataFrame([sample_enc], columns=X_columns)

    # Scale numeric cols
    df_in[num_cols] = scaler.transform(df_in[num_cols])

    # Prediction
    prob = model.predict_proba(df_in)[0, 1]
    label = "Laundering" if prob >= 0.5 else "Not Laundering"

    return {"probability": float(prob), "prediction": int(prob >= 0.5), "label": label}

# Example usage
if __name__ == "__main__":
    sample_input = {
        "From Bank": 135558,
        "To Bank": 16,
        "Amount Received": 24057.68,
        "Receiving Currency": "Canadian Dollar",
        "Amount Paid": 24057.68,
        "Payment Currency": "Canadian Dollar",
        "Payment Format": "Cash"
    }
    print(predict_custom(sample_input))