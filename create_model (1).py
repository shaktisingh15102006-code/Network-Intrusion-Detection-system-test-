# create_model.py

import pandas as pd
import joblib
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.pipeline import Pipeline

# Load dataset
df = pd.read_csv("KDDTrain+.txt")

# Rename columns
df.columns = [f"col_{i}" for i in range(len(df.columns))]

X = df.iloc[:, :-1]
y = df.iloc[:, -1]

# Encode categorical columns
for col in X.select_dtypes(include=['object']).columns:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col])

# Encode target
y = LabelEncoder().fit_transform(y)

# Create pipeline (VERY IMPORTANT)
pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", XGBClassifier(use_label_encoder=False, eval_metric='mlogloss'))
])

# Train
pipeline.fit(X, y)

# Save pipeline (NOT model)
joblib.dump(pipeline, "pipeline.pkl")

print("✅ Pipeline saved successfully!")
print("👉 Feature count:", X.shape[1])
