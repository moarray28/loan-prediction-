import pandas as pd
import joblib

from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

BASE_DIR = Path(__file__).resolve().parents[2]

data_path = BASE_DIR.parent / "data" / "loan_data.csv"

df = pd.read_csv(data_path)

# Drop Loan ID
df = df.drop("Loan_ID", axis=1)

# Fill missing values
df.fillna(df.mode().iloc[0], inplace=True)

# Convert categorical columns
df = pd.get_dummies(df, drop_first=True)

# Target column
y = df["Loan_Status_Y"]

# Features
X = df.drop("Loan_Status_Y", axis=1)
feature_names = X.columns.tolist()

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

accuracy = accuracy_score(
    y_test,
    predictions
)

print(f"Accuracy: {accuracy:.4f}")

artifact_path = (
    BASE_DIR
    / "ml-model"
    / "artifacts"
    / "loan_model.pkl"
)

joblib.dump(
    {
        "model": model,
        "features": feature_names
    },
    artifact_path
)

print(f"Model saved to {artifact_path}")
