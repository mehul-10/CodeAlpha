import pandas as pd

# ============================================================
# CONFIGURATION
# ============================================================

INPUT_PATH = "dataset/german_data/german.data"
OUTPUT_PATH = "dataset/credit_data.csv"


# ============================================================
# COLUMN NAMES
# ============================================================

column_names = [
    "checking_account",
    "duration_months",
    "credit_history",
    "purpose",
    "credit_amount",
    "savings_account",
    "employment_duration",
    "installment_rate",
    "personal_status_sex",
    "other_debtors",
    "residence_since",
    "property",
    "age",
    "other_installment_plans",
    "housing",
    "existing_credits",
    "job",
    "dependents",
    "telephone",
    "foreign_worker",
    "credit_risk"
]


# ============================================================
# LOAD RAW DATA
# ============================================================

df = pd.read_csv(
    INPUT_PATH,
    sep=r"\s+",
    header=None,
    encoding="latin-1"
)

print("=" * 60)
print("RAW DATA LOADED")
print("=" * 60)

print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")


# ============================================================
# ASSIGN COLUMN NAMES
# ============================================================

df.columns = column_names


# ============================================================
# CONVERT TARGET
# ============================================================

# Original dataset:
# 1 = Good credit risk
# 2 = Bad credit risk

df["credit_risk"] = df["credit_risk"].map({
    1: "Good",
    2: "Bad"
})


# ============================================================
# SAVE CLEAN DATASET
# ============================================================

df.to_csv(
    OUTPUT_PATH,
    index=False
)


# ============================================================
# DISPLAY INFORMATION
# ============================================================

print("\n" + "=" * 60)
print("CLEAN DATASET")
print("=" * 60)

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nTarget Distribution:")
print(df["credit_risk"].value_counts())

print("\nFirst 5 Rows:")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())

print("\n" + "=" * 60)
print(f"Saved successfully to: {OUTPUT_PATH}")
print("=" * 60)