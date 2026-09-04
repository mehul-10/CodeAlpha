import os
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay
)


# ============================================================
# CONFIGURATION
# ============================================================

DATA_PATH = "dataset/mnist_data.npz"
MODEL_PATH = "models/mnist_cnn.keras"

OUTPUT_DIR = "models/evaluation"

os.makedirs(OUTPUT_DIR, exist_ok=True)


# ============================================================
# LOAD DATA
# ============================================================

print("=" * 60)
print("Loading MNIST test data")
print("=" * 60)

data = np.load(DATA_PATH)

X_test = data["X_test"]
y_test = data["y_test"]

print("Test images :", X_test.shape)
print("Test labels :", y_test.shape)


# ============================================================
# LOAD MODEL
# ============================================================

print("\nLoading trained CNN...")

model = tf.keras.models.load_model(MODEL_PATH)

print("Model loaded successfully!")


# ============================================================
# MODEL EVALUATION
# ============================================================

print("\n" + "=" * 60)
print("Evaluating CNN")
print("=" * 60)

test_loss, test_accuracy = model.evaluate(
    X_test,
    y_test,
    verbose=1
)

print(f"\nTest Loss     : {test_loss:.4f}")
print(f"Test Accuracy : {test_accuracy:.4%}")


# ============================================================
# PREDICTIONS
# ============================================================

print("\nGenerating predictions...")

probabilities = model.predict(
    X_test,
    batch_size=128,
    verbose=1
)

y_pred = np.argmax(probabilities, axis=1)


# ============================================================
# CLASSIFICATION REPORT
# ============================================================

print("\n" + "=" * 60)
print("Classification Report")
print("=" * 60)

report = classification_report(
    y_test,
    y_pred,
    digits=4
)

print(report)

with open(
    os.path.join(
        OUTPUT_DIR,
        "classification_report.txt"
    ),
    "w"
) as file:

    file.write(report)


# ============================================================
# CONFUSION MATRIX
# ============================================================

print("\nGenerating confusion matrix...")

cm = confusion_matrix(
    y_test,
    y_pred
)

fig, ax = plt.subplots(
    figsize=(9, 9)
)

display = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=np.arange(10)
)

display.plot(
    ax=ax,
    values_format="d"
)

ax.set_title(
    "MNIST CNN Confusion Matrix"
)

plt.tight_layout()

confusion_path = os.path.join(
    OUTPUT_DIR,
    "confusion_matrix.png"
)

plt.savefig(
    confusion_path,
    dpi=150,
    bbox_inches="tight"
)

plt.close()

print(
    f"Saved confusion matrix to: {confusion_path}"
)


# ============================================================
# PER-DIGIT ACCURACY
# ============================================================

print("\n" + "=" * 60)
print("Per-Digit Accuracy")
print("=" * 60)

per_digit_accuracy = {}

for digit in range(10):

    mask = y_test == digit

    accuracy = np.mean(
        y_pred[mask] == y_test[mask]
    )

    per_digit_accuracy[digit] = accuracy

    print(
        f"Digit {digit}: "
        f"{accuracy:.4%}"
    )


# ============================================================
# PER-DIGIT ACCURACY GRAPH
# ============================================================

digits = list(
    per_digit_accuracy.keys()
)

accuracies = list(
    per_digit_accuracy.values()
)

fig, ax = plt.subplots(
    figsize=(10, 6)
)

ax.bar(
    digits,
    accuracies
)

ax.set_title(
    "Per-Digit Accuracy"
)

ax.set_xlabel(
    "Digit"
)

ax.set_ylabel(
    "Accuracy"
)

ax.set_ylim(
    0.90,
    1.00
)

ax.set_xticks(
    digits
)

plt.tight_layout()

digit_accuracy_path = os.path.join(
    OUTPUT_DIR,
    "per_digit_accuracy.png"
)

plt.savefig(
    digit_accuracy_path,
    dpi=150,
    bbox_inches="tight"
)

plt.close()

print(
    f"\nSaved per-digit accuracy graph to: "
    f"{digit_accuracy_path}"
)


# ============================================================
# SAVE METRICS
# ============================================================

np.savez(
    os.path.join(
        OUTPUT_DIR,
        "evaluation_metrics.npz"
    ),
    test_loss=test_loss,
    test_accuracy=test_accuracy,
    confusion_matrix=cm,
    y_true=y_test,
    y_pred=y_pred
)


# ============================================================
# COMPLETION
# ============================================================

print("\n" + "=" * 60)
print("MODEL EVALUATION COMPLETED!")
print("=" * 60)

print(
    f"Test Accuracy: {test_accuracy:.4%}"
)

print(
    f"Evaluation files saved in: "
    f"{OUTPUT_DIR}"
)