import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    classification_report
)


# ============================================================
# CONFIGURATION
# ============================================================

DATA_PATH = "dataset/credit_data.csv"
MODEL_PATH = "models/credit_model.pkl"

RANDOM_STATE = 42


# ============================================================
# LOAD DATA
# ============================================================

df = pd.read_csv(DATA_PATH)

print("=" * 65)
print("CREDIT SCORING MODEL")
print("=" * 65)

print(f"\nDataset shape: {df.shape}")


# ============================================================
# SEPARATE FEATURES AND TARGET
# ============================================================

X = df.drop("credit_risk", axis=1)

y = df["credit_risk"].map({
    "Good": 1,
    "Bad": 0
})


# ============================================================
# IDENTIFY FEATURE TYPES
# ============================================================

categorical_features = [
    "checking_account",
    "credit_history",
    "purpose",
    "savings_account",
    "employment_duration",
    "personal_status_sex",
    "other_debtors",
    "property",
    "other_installment_plans",
    "housing",
    "job",
    "telephone",
    "foreign_worker"
]

numerical_features = [
    "duration_months",
    "credit_amount",
    "installment_rate",
    "residence_since",
    "age",
    "existing_credits",
    "dependents"
]


# ============================================================
# TRAIN / TEST SPLIT
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=RANDOM_STATE,
    stratify=y
)

print(f"Training samples: {len(X_train)}")
print(f"Testing samples: {len(X_test)}")


# ============================================================
# PREPROCESSING
# ============================================================

preprocessor = ColumnTransformer(
    transformers=[
        (
            "numerical",
            StandardScaler(),
            numerical_features
        ),
        (
            "categorical",
            OneHotEncoder(
                handle_unknown="ignore"
            ),
            categorical_features
        )
    ]
)


# ============================================================
# MODELS
# ============================================================

models = {

    "Logistic Regression":
        LogisticRegression(
            max_iter=1000,
            random_state=RANDOM_STATE
        ),

    "Decision Tree":
        DecisionTreeClassifier(
            max_depth=6,
            random_state=RANDOM_STATE
        ),

    "Random Forest":
        RandomForestClassifier(
            n_estimators=300,
            max_depth=10,
            random_state=RANDOM_STATE,
            class_weight="balanced"
        )
}


# ============================================================
# TRAIN AND EVALUATE
# ============================================================

results = {}

best_model = None
best_model_name = None
best_f1 = -1


for name, model in models.items():

    print("\n" + "=" * 65)
    print(f"TRAINING: {name}")
    print("=" * 65)

    pipeline = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("model", model)
        ]
    )

    pipeline.fit(X_train, y_train)

    # Predictions
    y_pred = pipeline.predict(X_test)

    # Probability for ROC-AUC
    y_probability = pipeline.predict_proba(X_test)[:, 1]

    # Metrics
    accuracy = accuracy_score(y_test, y_pred)

    precision = precision_score(
        y_test,
        y_pred,
        zero_division=0
    )

    recall = recall_score(
        y_test,
        y_pred,
        zero_division=0
    )

    f1 = f1_score(
        y_test,
        y_pred,
        zero_division=0
    )

    roc_auc = roc_auc_score(
        y_test,
        y_probability
    )

    results[name] = {
        "Accuracy": accuracy,
        "Precision": precision,
        "Recall": recall,
        "F1 Score": f1,
        "ROC-AUC": roc_auc
    }

    print(f"\nAccuracy : {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall   : {recall:.4f}")
    print(f"F1 Score : {f1:.4f}")
    print(f"ROC-AUC  : {roc_auc:.4f}")

    print("\nClassification Report:")
    print(
        classification_report(
            y_test,
            y_pred,
            target_names=["Bad", "Good"],
            zero_division=0
        )
    )

    # Select best model using F1 score
    if f1 > best_f1:
        best_f1 = f1
        best_model = pipeline
        best_model_name = name


# ============================================================
# DISPLAY MODEL COMPARISON
# ============================================================

results_df = pd.DataFrame(results).T

print("\n" + "=" * 65)
print("MODEL COMPARISON")
print("=" * 65)

print(results_df.round(4))


# ============================================================
# SAVE BEST MODEL
# ============================================================

import os

os.makedirs("models", exist_ok=True)

joblib.dump(
    best_model,
    MODEL_PATH
)

print("\n" + "=" * 65)
print("BEST MODEL")
print("=" * 65)

print(f"Model: {best_model_name}")
print(f"F1 Score: {best_f1:.4f}")

print(f"\nModel saved to:")
print(MODEL_PATH)

print("=" * 65)