import pandas as pd
import joblib
import matplotlib.pyplot as plt


# ============================================================
# CONFIGURATION
# ============================================================

MODEL_PATH = "models/credit_model.pkl"


# ============================================================
# LOAD MODEL
# ============================================================

model = joblib.load(MODEL_PATH)

print("=" * 60)
print("FEATURE IMPORTANCE ANALYSIS")
print("=" * 60)


# ============================================================
# GET PREPROCESSOR AND MODEL
# ============================================================

preprocessor = model.named_steps["preprocessor"]
rf_model = model.named_steps["model"]


# ============================================================
# GET FEATURE NAMES
# ============================================================

feature_names = preprocessor.get_feature_names_out()


# ============================================================
# GET FEATURE IMPORTANCE
# ============================================================

importance = rf_model.feature_importances_


importance_df = pd.DataFrame({
    "Feature": feature_names,
    "Importance": importance
})


# ============================================================
# CLEAN FEATURE NAMES
# ============================================================

importance_df["Feature"] = (
    importance_df["Feature"]
    .str.replace("numerical__", "", regex=False)
    .str.replace("categorical__", "", regex=False)
)


# ============================================================
# SORT FEATURES
# ============================================================

importance_df = importance_df.sort_values(
    by="Importance",
    ascending=False
)


# ============================================================
# DISPLAY TOP 15
# ============================================================

print("\nTop 15 Most Important Features:\n")

print(
    importance_df.head(15).to_string(
        index=False
    )
)


# ============================================================
# SAVE FEATURE IMPORTANCE
# ============================================================

importance_df.to_csv(
    "feature_importance.csv",
    index=False
)


# ============================================================
# VISUALIZATION
# ============================================================

top_features = importance_df.head(15)

plt.figure(figsize=(10, 7))

plt.barh(
    top_features["Feature"][::-1],
    top_features["Importance"][::-1]
)

plt.xlabel("Importance")
plt.ylabel("Feature")
plt.title("Top 15 Feature Importances")

plt.tight_layout()

plt.savefig(
    "feature_importance.png",
    dpi=300
)

plt.show()


print("\nFeature importance saved to:")
print("feature_importance.csv")

print("\nChart saved to:")
print("feature_importance.png")

print("\n" + "=" * 60)