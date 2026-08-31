import pandas as pd
import joblib

from sklearn.model_selection import (
    train_test_split,
    GridSearchCV,
    StratifiedKFold
)

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix,
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

X = df.drop("credit_risk", axis=1)

# Good = 1
# Bad = 0
y = df["credit_risk"].map({
    "Good": 1,
    "Bad": 0
})


# ============================================================
# FEATURE TYPES
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


# ============================================================
# PREPROCESSOR
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
            OneHotEncoder(handle_unknown="ignore"),
            categorical_features
        )
    ]
)


# ============================================================
# CROSS-VALIDATION
# ============================================================

cv = StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=RANDOM_STATE
)


# ============================================================
# LOGISTIC REGRESSION
# ============================================================

logistic_pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        (
            "model",
            LogisticRegression(
                max_iter=2000,
                random_state=RANDOM_STATE
            )
        )
    ]
)

logistic_params = {
    "model__C": [0.01, 0.1, 1, 10, 100],
    "model__class_weight": [None, "balanced"],
    "model__solver": ["liblinear", "lbfgs"]
}


# ============================================================
# RANDOM FOREST
# ============================================================

rf_pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        (
            "model",
            RandomForestClassifier(
                random_state=RANDOM_STATE,
                n_jobs=-1
            )
        )
    ]
)

rf_params = {
    "model__n_estimators": [200, 300],
    "model__max_depth": [5, 10, 15, None],
    "model__min_samples_split": [2, 5, 10],
    "model__min_samples_leaf": [1, 2, 4],
    "model__class_weight": [None, "balanced"]
}


# ============================================================
# HYPERPARAMETER TUNING
# ============================================================

print("=" * 70)
print("MODEL OPTIMIZATION")
print("=" * 70)


print("\nTuning Logistic Regression...")

logistic_search = GridSearchCV(
    logistic_pipeline,
    logistic_params,
    cv=cv,
    scoring="f1_macro",
    n_jobs=-1,
    verbose=1
)

logistic_search.fit(X_train, y_train)

print("\nBest Logistic Regression Parameters:")
print(logistic_search.best_params__)

print(
    f"Best CV Macro F1: "
    f"{logistic_search.best_score_:.4f}"
)


print("\nTuning Random Forest...")

rf_search = GridSearchCV(
    rf_pipeline,
    rf_params,
    cv=cv,
    scoring="f1_macro",
    n_jobs=-1,
    verbose=1
)

rf_search.fit(X_train, y_train)

print("\nBest Random Forest Parameters:")
print(rf_search.best_params__)

print(
    f"Best CV Macro F1: "
    f"{rf_search.best_score_:.4f}"
)


# ============================================================
# EVALUATION FUNCTION
# ============================================================

def evaluate_model(name, model):

    y_pred = model.predict(X_test)

    y_probability = model.predict_proba(X_test)[:, 1]

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

    macro_f1 = f1_score(
        y_test,
        y_pred,
        average="macro",
        zero_division=0
    )

    roc_auc = roc_auc_score(
        y_test,
        y_probability
    )

    # Bad = class 0
    bad_recall = recall_score(
        y_test,
        y_pred,
        pos_label=0,
        zero_division=0
    )

    bad_f1 = f1_score(
        y_test,
        y_pred,
        pos_label=0,
        zero_division=0
    )

    print("\n" + "=" * 70)
    print(name)
    print("=" * 70)

    print(f"Accuracy        : {accuracy:.4f}")
    print(f"Precision       : {precision:.4f}")
    print(f"Recall (Good)   : {recall:.4f}")
    print(f"F1 (Good)       : {f1:.4f}")
    print(f"Macro F1        : {macro_f1:.4f}")
    print(f"ROC-AUC         : {roc_auc:.4f}")
    print(f"Bad Recall      : {bad_recall:.4f}")
    print(f"Bad F1          : {bad_f1:.4f}")

    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

    print("\nClassification Report:")
    print(
        classification_report(
            y_test,
            y_pred,
            target_names=["Bad", "Good"],
            zero_division=0
        )
    )

    return {
        "Accuracy": accuracy,
        "Precision": precision,
        "Recall_Good": recall,
        "F1_Good": f1,
        "Macro_F1": macro_f1,
        "ROC_AUC": roc_auc,
        "Bad_Recall": bad_recall,
        "Bad_F1": bad_f1
    }


# ============================================================
# EVALUATE TUNED MODELS
# ============================================================

logistic_results = evaluate_model(
    "TUNED LOGISTIC REGRESSION",
    logistic_search.best_estimator_
)

rf_results = evaluate_model(
    "TUNED RANDOM FOREST",
    rf_search.best_estimator_
)


# ============================================================
# COMPARISON
# ============================================================

comparison = pd.DataFrame(
    {
        "Tuned Logistic Regression": logistic_results,
        "Tuned Random Forest": rf_results
    }
).T

print("\n" + "=" * 70)
print("TUNED MODEL COMPARISON")
print("=" * 70)

print(comparison.round(4))


# ============================================================
# SELECT FINAL MODEL
# ============================================================

if rf_results["Macro_F1"] > logistic_results["Macro_F1"]:
    final_model = rf_search.best_estimator_
    final_name = "Tuned Random Forest"
else:
    final_model = logistic_search.best_estimator_
    final_name = "Tuned Logistic Regression"


# ============================================================
# SAVE FINAL MODEL
# ============================================================

joblib.dump(
    final_model,
    MODEL_PATH
)

print("\n" + "=" * 70)
print("FINAL MODEL")
print("=" * 70)

print(f"Selected Model: {final_name}")
print(f"Saved to: {MODEL_PATH}")

print("=" * 70)