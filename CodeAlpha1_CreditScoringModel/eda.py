import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ============================================================
# LOAD DATA
# ============================================================

DATA_PATH = "dataset/credit_data.csv"

df = pd.read_csv(DATA_PATH)

print("=" * 60)
print("EXPLORATORY DATA ANALYSIS")
print("=" * 60)

# ============================================================
# BASIC INFORMATION
# ============================================================

print("\nDataset Shape:")
print(df.shape)

print("\nDataset Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

# ============================================================
# TARGET DISTRIBUTION
# ============================================================

print("\nCredit Risk Distribution:")
print(df["credit_risk"].value_counts())

plt.figure(figsize=(7, 5))

sns.countplot(
    data=df,
    x="credit_risk"
)

plt.title("Credit Risk Distribution")
plt.xlabel("Credit Risk")
plt.ylabel("Number of Applicants")

plt.tight_layout()
plt.show()

# ============================================================
# NUMERICAL FEATURES
# ============================================================

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
# NUMERICAL DISTRIBUTIONS
# ============================================================

df[numerical_features].hist(
    figsize=(12, 10),
    bins=20
)

plt.suptitle("Numerical Feature Distributions")

plt.tight_layout()
plt.show()

# ============================================================
# CREDIT AMOUNT VS CREDIT RISK
# ============================================================

plt.figure(figsize=(8, 5))

sns.boxplot(
    data=df,
    x="credit_risk",
    y="credit_amount"
)

plt.title("Credit Amount by Credit Risk")
plt.xlabel("Credit Risk")
plt.ylabel("Credit Amount")

plt.tight_layout()
plt.show()

# ============================================================
# AGE VS CREDIT RISK
# ============================================================

plt.figure(figsize=(8, 5))

sns.boxplot(
    data=df,
    x="credit_risk",
    y="age"
)

plt.title("Age Distribution by Credit Risk")
plt.xlabel("Credit Risk")
plt.ylabel("Age")

plt.tight_layout()
plt.show()

# ============================================================
# LOAN DURATION VS CREDIT RISK
# ============================================================

plt.figure(figsize=(8, 5))

sns.boxplot(
    data=df,
    x="credit_risk",
    y="duration_months"
)

plt.title("Loan Duration by Credit Risk")
plt.xlabel("Credit Risk")
plt.ylabel("Duration (Months)")

plt.tight_layout()
plt.show()

# ============================================================
# CORRELATION MATRIX
# ============================================================

plt.figure(figsize=(10, 7))

correlation = df[numerical_features].corr()

sns.heatmap(
    correlation,
    annot=True,
    fmt=".2f",
    cmap="coolwarm"
)

plt.title("Correlation Matrix")

plt.tight_layout()
plt.show()

# ============================================================
# CREDIT RISK BY CHECKING ACCOUNT
# ============================================================

plt.figure(figsize=(9, 5))

sns.countplot(
    data=df,
    x="checking_account",
    hue="credit_risk"
)

plt.title("Credit Risk by Checking Account Status")
plt.xlabel("Checking Account")
plt.ylabel("Number of Applicants")

plt.tight_layout()
plt.show()

# ============================================================
# CREDIT RISK BY SAVINGS ACCOUNT
# ============================================================

plt.figure(figsize=(9, 5))

sns.countplot(
    data=df,
    x="savings_account",
    hue="credit_risk"
)

plt.title("Credit Risk by Savings Account")
plt.xlabel("Savings Account")
plt.ylabel("Number of Applicants")

plt.tight_layout()
plt.show()

print("\n" + "=" * 60)
print("EDA COMPLETED")
print("=" * 60)