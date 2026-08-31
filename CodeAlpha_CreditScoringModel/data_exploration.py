import pandas as pd

# ============================================================
# LOAD DATASET
# ============================================================

DATA_PATH = "dataset/german_data/german.data"

df = pd.read_csv(
    DATA_PATH,
    sep=r"\s+",
    header=None,
    encoding="latin-1"
)

# ============================================================
# DISPLAY BASIC INFORMATION
# ============================================================

print("\n" + "=" * 60)
print("CREDIT SCORING DATASET")
print("=" * 60)

print("\nDataset Shape:")
print(df.shape)

print("\nFirst 5 Rows:")
print(df.head())

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nTarget Distribution:")
print(df.iloc[:, -1].value_counts())

print("\n" + "=" * 60)