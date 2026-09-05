import os
import joblib
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    classification_report,
    confusion_matrix
)


# ============================================================
# CONFIGURATION
# ============================================================

DATA_PATH = "dataset/diabetes.csv"
MODEL_DIR = "models"

os.makedirs(MODEL_DIR, exist_ok=True)


COLUMNS = [
    "Pregnancies",
    "Glucose",
    "BloodPressure",
    "SkinThickness",
    "Insulin",
    "BMI",
    "DiabetesPedigreeFunction",
    "Age",
    "Outcome"
]


# ============================================================
# LOAD DATA
# ============================================================

print("\n" + "=" * 65)
print("DISEASE PREDICTION MODEL TRAINING")
print("=" * 65)

df = pd.read_csv(
    DATA_PATH,
    header=None,
    names=COLUMNS
)

print(f"\nDataset shape: {df.shape}")


# ============================================================
# HANDLE INVALID ZERO VALUES
# ============================================================

invalid_zero_columns = [
    "Glucose",
    "BloodPressure",
    "SkinThickness",
    "Insulin",
    "BMI"
]

df[invalid_zero_columns] = df[invalid_zero_columns].replace(
    0,
    np.nan
)

print("\nInvalid zero values replaced with NaN.")


# ============================================================
# FEATURES AND TARGET
# ============================================================

X = df.drop("Outcome", axis=1)
y = df["Outcome"]


# ============================================================
# TRAIN / TEST SPLIT
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print(f"\nTraining samples: {len(X_train)}")
print(f"Testing samples:  {len(X_test)}")


# ============================================================
# PREPROCESSING PIPELINE
# ============================================================

numeric_features = X.columns.tolist()

preprocessor = ColumnTransformer(
    transformers=[
        (
            "numeric",
            Pipeline([
                (
                    "imputer",
                    SimpleImputer(strategy="median")
                ),
                (
                    "scaler",
                    StandardScaler()
                )
            ]),
            numeric_features
        )
    ]
)


# ============================================================
# MODELS
# ============================================================

models = {

    "Logistic Regression": LogisticRegression(
        max_iter=1000,
        random_state=42
    ),

    "Random Forest": RandomForestClassifier(
        n_estimators=300,
        max_depth=10,
        min_samples_split=5,
        random_state=42,
        class_weight="balanced"
    ),

    "SVM": SVC(
        kernel="rbf",
        probability=True,
        random_state=42,
        class_weight="balanced"
    )
}


# ============================================================
# TRAIN AND EVALUATE
# ============================================================

results = []
trained_models = {}

best_model_name = None
best_model = None
best_f1 = -1


for name, model in models.items():

    print("\n" + "-" * 65)
    print(f"Training: {name}")
    print("-" * 65)

    pipeline = Pipeline([
        ("preprocessor", preprocessor),
        ("model", model)
    ])

    pipeline.fit(
        X_train,
        y_train
    )

    y_pred = pipeline.predict(X_test)

    y_probability = pipeline.predict_proba(
        X_test
    )[:, 1]

    accuracy = accuracy_score(
        y_test,
        y_pred
    )

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

    print(f"Accuracy : {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall   : {recall:.4f}")
    print(f"F1 Score : {f1:.4f}")
    print(f"ROC-AUC  : {roc_auc:.4f}")

    print("\nClassification Report:")
    print(
        classification_report(
            y_test,
            y_pred,
            target_names=[
                "No Diabetes",
                "Diabetes"
            ],
            zero_division=0
        )
    )

    results.append({
        "Model": name,
        "Accuracy": accuracy,
        "Precision": precision,
        "Recall": recall,
        "F1 Score": f1,
        "ROC-AUC": roc_auc
    })

    trained_models[name] = pipeline

    if f1 > best_f1:
        best_f1 = f1
        best_model_name = name
        best_model = pipeline


# ============================================================
# MODEL COMPARISON
# ============================================================

results_df = pd.DataFrame(results)

results_df = results_df.sort_values(
    by="F1 Score",
    ascending=False
)

print("\n" + "=" * 65)
print("MODEL COMPARISON")
print("=" * 65)

print(
    results_df.to_string(
        index=False,
        float_format=lambda x: f"{x:.4f}"
    )
)


# ============================================================
# BEST MODEL
# ============================================================

print("\n" + "=" * 65)
print(f"BEST MODEL: {best_model_name}")
print("=" * 65)

best_predictions = best_model.predict(X_test)

print("\nConfusion Matrix:")
print(
    confusion_matrix(
        y_test,
        best_predictions
    )
)

print("\nBest Model Classification Report:")
print(
    classification_report(
        y_test,
        best_predictions,
        target_names=[
            "No Diabetes",
            "Diabetes"
        ],
        zero_division=0
    )
)


# ============================================================
# SAVE BEST MODEL
# ============================================================

model_path = os.path.join(
    MODEL_DIR,
    "disease_prediction_model.pkl"
)

joblib.dump(
    best_model,
    model_path
)

print(f"\nBest model saved to:")
print(model_path)


# ============================================================
# SAVE MODEL COMPARISON
# ============================================================

results_path = os.path.join(
    MODEL_DIR,
    "model_comparison.csv"
)

results_df.to_csv(
    results_path,
    index=False
)

print(f"Model comparison saved to:")
print(results_path)


# ============================================================
# SAVE TEST DATA
# ============================================================

test_data = X_test.copy()
test_data["Outcome"] = y_test.values

test_data_path = os.path.join(
    MODEL_DIR,
    "test_data.csv"
)

test_data.to_csv(
    test_data_path,
    index=False
)

print(f"Test data saved to:")
print(test_data_path)


print("\n" + "=" * 65)
print("MODEL TRAINING COMPLETED SUCCESSFULLY!")
print("=" * 65)