import joblib
import pandas as pd

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

MODEL_DATA = joblib.load(
    BASE_DIR /
    "ml-model" /
    "artifacts" /
    "loan_model.pkl"
)

model = MODEL_DATA["model"]
expected_features = MODEL_DATA["features"]


def predict_loan(request_data):
    df = pd.DataFrame([request_data])

    df = pd.get_dummies(
        df,
        drop_first=True
    )

    df = df.reindex(
        columns=expected_features,
        fill_value=0
    )

    prediction = model.predict(df)[0]

    probability = model.predict_proba(df)[0][1]

    return prediction, probability
