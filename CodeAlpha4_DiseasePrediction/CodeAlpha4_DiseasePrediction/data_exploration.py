import os
import pandas as pd


# ============================================================
# CONFIGURATION
# ============================================================

DATA_PATH = "dataset/diabetes.csv"

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

if not os.path.exists(DATA_PATH):
    raise FileNotFoundError(
        f"Dataset not found at: {DATA_PATH}"
    )

df = pd.read_csv(
    DATA_PATH,
    header=None,
    names=COLUMNS
)


# ============================================================
# BASIC INFORMATION
# ============================================================

print("\n" + "=" * 60)
print("DISEASE PREDICTION DATA EXPLORATION")
print("=" * 60)

print("\nDataset shape:")
print(df.shape)

print("\nColumn names:")
print(list(df.columns))

print("\nFirst 5 rows:")
print(df.head())


# ============================================================
# DATA TYPES
# ============================================================

print("\nData types:")
print(df.dtypes)


# ============================================================
# MISSING VALUES
# ============================================================

print("\nMissing values:")
print(df.isnull().sum())


# ============================================================
# DUPLICATES
# ============================================================

print("\nDuplicate rows:")
print(df.duplicated().sum())


# ============================================================
# TARGET DISTRIBUTION
# ============================================================

print("\nTarget distribution:")
print(df["Outcome"].value_counts())

print("\nTarget percentages:")
print(
    df["Outcome"]
    .value_counts(normalize=True)
    .mul(100)
    .round(2)
)


# ============================================================
# STATISTICAL SUMMARY
# ============================================================

print("\nStatistical summary:")
print(df.describe().round(2))


# ============================================================
# ZERO VALUES
# ============================================================

medical_columns = [
    "Glucose",
    "BloodPressure",
    "SkinThickness",
    "Insulin",
    "BMI"
]

print("\nPotential invalid zero values:")
print(
    (df[medical_columns] == 0).sum()
)


# ============================================================
# CORRELATION WITH TARGET
# ============================================================

print("\nCorrelation with Outcome:")
print(
    df.corr(numeric_only=True)["Outcome"]
    .sort_values(ascending=False)
    .round(3)
)


print("\n" + "=" * 60)
print("DATA EXPLORATION COMPLETED")
print("=" * 60)