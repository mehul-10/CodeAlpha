import os
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix,
    ConfusionMatrixDisplay,
    classification_report,
    roc_curve,
    auc
)


# ============================================================
# CONFIGURATION
# ============================================================

MODEL_PATH = "models/disease_prediction_model.pkl"
COMPARISON_PATH = "models/model_comparison.csv"
TEST_DATA_PATH = "models/test_data.csv"

EVALUATION_DIR = "models/evaluation"

os.makedirs(EVALUATION_DIR, exist_ok=True)


FEATURE_COLUMNS = [
    "Pregnancies",
    "Glucose",
    "BloodPressure",
    "SkinThickness",
    "Insulin",
    "BMI",
    "DiabetesPedigreeFunction",
    "Age"
]


# ============================================================
# LOAD DATA AND MODEL
# ============================================================

print("\n" + "=" * 65)
print("DISEASE PREDICTION MODEL EVALUATION")
print("=" * 65)

model = joblib.load(MODEL_PATH)

test_data = pd.read_csv(
    TEST_DATA_PATH
)

X_test = test_data[FEATURE_COLUMNS]
y_test = test_data["Outcome"]


# ============================================================
# PREDICTIONS
# ============================================================

y_pred = model.predict(X_test)

y_probability = model.predict_proba(
    X_test
)[:, 1]


# ============================================================
# METRICS
# ============================================================

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


print(f"\nAccuracy : {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall   : {recall:.4f}")
print(f"F1 Score : {f1:.4f}")
print(f"ROC-AUC  : {roc_auc:.4f}")


# ============================================================
# CLASSIFICATION REPORT
# ============================================================

report = classification_report(
    y_test,
    y_pred,
    target_names=[
        "No Diabetes",
        "Diabetes"
    ],
    zero_division=0
)

print("\nClassification Report:")
print(report)

with open(
    os.path.join(
        EVALUATION_DIR,
        "classification_report.txt"
    ),
    "w"
) as file:

    file.write(report)


# ============================================================
# CONFUSION MATRIX
# ============================================================

cm = confusion_matrix(
    y_test,
    y_pred
)

fig, ax = plt.subplots(
    figsize=(7, 6)
)

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=[
        "No Diabetes",
        "Diabetes"
    ]
)

disp.plot(
    ax=ax,
    values_format="d"
)

ax.set_title(
    "Diabetes Prediction — Confusion Matrix"
)

plt.tight_layout()

plt.savefig(
    os.path.join(
        EVALUATION_DIR,
        "confusion_matrix.png"
    ),
    dpi=150
)

plt.close()


# ============================================================
# ROC CURVE
# ============================================================

fpr, tpr, _ = roc_curve(
    y_test,
    y_probability
)

roc_score = auc(
    fpr,
    tpr
)

fig, ax = plt.subplots(
    figsize=(8, 6)
)

ax.plot(
    fpr,
    tpr,
    label=f"Random Forest (AUC = {roc_score:.3f})"
)

ax.plot(
    [0, 1],
    [0, 1],
    linestyle="--",
    label="Random Classifier"
)

ax.set_xlabel(
    "False Positive Rate"
)

ax.set_ylabel(
    "True Positive Rate"
)

ax.set_title(
    "ROC Curve"
)

ax.legend()

plt.tight_layout()

plt.savefig(
    os.path.join(
        EVALUATION_DIR,
        "roc_curve.png"
    ),
    dpi=150
)

plt.close()


# ============================================================
# MODEL COMPARISON
# ============================================================

comparison = pd.read_csv(
    COMPARISON_PATH
)

fig, ax = plt.subplots(
    figsize=(10, 6)
)

comparison.plot(
    x="Model",
    y=[
        "Accuracy",
        "Precision",
        "Recall",
        "F1 Score",
        "ROC-AUC"
    ],
    kind="bar",
    ax=ax
)

ax.set_ylabel(
    "Score"
)

ax.set_ylim(
    0,
    1
)

ax.set_title(
    "Model Performance Comparison"
)

ax.legend(
    loc="lower right"
)

plt.xticks(
    rotation=0
)

plt.tight_layout()

plt.savefig(
    os.path.join(
        EVALUATION_DIR,
        "model_comparison.png"
    ),
    dpi=150
)

plt.close()


# ============================================================
# FEATURE IMPORTANCE
# ============================================================

random_forest = model.named_steps["model"]

importance = random_forest.feature_importances_

importance_df = pd.DataFrame({
    "Feature": FEATURE_COLUMNS,
    "Importance": importance
})

importance_df = importance_df.sort_values(
    by="Importance",
    ascending=False
)

importance_df.to_csv(
    os.path.join(
        EVALUATION_DIR,
        "feature_importance.csv"
    ),
    index=False
)


fig, ax = plt.subplots(
    figsize=(9, 6)
)

ax.barh(
    importance_df["Feature"],
    importance_df["Importance"]
)

ax.invert_yaxis()

ax.set_xlabel(
    "Importance"
)

ax.set_title(
    "Random Forest Feature Importance"
)

plt.tight_layout()

plt.savefig(
    os.path.join(
        EVALUATION_DIR,
        "feature_importance.png"
    ),
    dpi=150
)

plt.close()


# ============================================================
# SAVE METRICS
# ============================================================

metrics = {
    "accuracy": accuracy,
    "precision": precision,
    "recall": recall,
    "f1_score": f1,
    "roc_auc": roc_auc
}

np.savez(
    os.path.join(
        EVALUATION_DIR,
        "evaluation_metrics.npz"
    ),
    **metrics
)


# ============================================================
# FINAL OUTPUT
# ============================================================

print("\n" + "=" * 65)
print("EVALUATION COMPLETED SUCCESSFULLY!")
print("=" * 65)

print(
    f"\nEvaluation files saved in: {EVALUATION_DIR}"
)