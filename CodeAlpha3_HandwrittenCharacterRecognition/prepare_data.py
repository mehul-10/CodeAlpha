import os
import numpy as np
from tensorflow.keras.datasets import mnist


# ============================================================
# CONFIGURATION
# ============================================================

DATASET_DIR = "dataset"
OUTPUT_PATH = os.path.join(DATASET_DIR, "mnist_data.npz")


# ============================================================
# LOAD DATASET
# ============================================================

print("=" * 60)
print("Loading MNIST Dataset")
print("=" * 60)

(X_train, y_train), (X_test, y_test) = mnist.load_data()

print(f"Training images : {X_train.shape}")
print(f"Training labels : {y_train.shape}")
print(f"Test images     : {X_test.shape}")
print(f"Test labels     : {y_test.shape}")


# ============================================================
# PREPROCESSING
# ============================================================

print("\nPreprocessing images...")

# Convert pixel values from 0–255 to 0–1
X_train = X_train.astype("float32") / 255.0
X_test = X_test.astype("float32") / 255.0

# Add channel dimension
# (60000, 28, 28) -> (60000, 28, 28, 1)
X_train = np.expand_dims(X_train, axis=-1)
X_test = np.expand_dims(X_test, axis=-1)


# ============================================================
# DATASET INFORMATION
# ============================================================

print(f"Processed training shape : {X_train.shape}")
print(f"Processed test shape     : {X_test.shape}")

print("\nNumber of classes:", len(np.unique(y_train)))
print("Classes:", np.unique(y_train))

print("\nClass distribution:")

for digit in range(10):
    count = np.sum(y_train == digit)
    print(f"Digit {digit}: {count}")


# ============================================================
# SAVE DATA
# ============================================================

os.makedirs(DATASET_DIR, exist_ok=True)

np.savez_compressed(
    OUTPUT_PATH,
    X_train=X_train,
    y_train=y_train,
    X_test=X_test,
    y_test=y_test
)

print("\n" + "=" * 60)
print("Dataset preprocessing completed successfully!")
print(f"Saved to: {OUTPUT_PATH}")
print("=" * 60)