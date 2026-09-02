import os
import numpy as np
import tensorflow as tf

from sklearn.preprocessing import LabelEncoder
from sklearn.utils.class_weight import compute_class_weight

from tensorflow.keras import layers, models
from tensorflow.keras.callbacks import (
    EarlyStopping,
    ReduceLROnPlateau,
    ModelCheckpoint
)


# ============================================================
# CONFIGURATION
# ============================================================

DATA_PATH = "dataset/processed_data.npz"
MODEL_DIR = "models"

MODEL_PATH = os.path.join(
    MODEL_DIR,
    "speech_emotion_crnn.keras"
)

LABEL_PATH = os.path.join(
    MODEL_DIR,
    "emotion_labels.npy"
)

NORMALIZATION_PATH = os.path.join(
    MODEL_DIR,
    "normalization.npz"
)

HISTORY_PATH = os.path.join(
    MODEL_DIR,
    "training_history.npz"
)


os.makedirs(MODEL_DIR, exist_ok=True)


# ============================================================
# LOAD DATA
# ============================================================

print("=" * 60)
print("SPEECH EMOTION CRNN TRAINING")
print("=" * 60)

data = np.load(DATA_PATH)

X = data["X"].astype(np.float32)
y = data["y"]
actors = data["actors"]

print("\nDataset:")
print("Features:", X.shape)
print("Labels:", y.shape)
print("Actors:", actors.shape)


# ============================================================
# LABEL ENCODING
# ============================================================

label_encoder = LabelEncoder()

y_encoded = label_encoder.fit_transform(y)

class_names = label_encoder.classes_

print("\nEmotion classes:")

for i, name in enumerate(class_names):
    print(f"{i}: {name}")


# ============================================================
# ACTOR-INDEPENDENT SPLIT
# ============================================================

# Actors 01-18 -> Training
# Actors 19-20 -> Validation
# Actors 21-24 -> Testing

train_mask = np.isin(
    actors,
    np.arange(1, 19)
)

val_mask = np.isin(
    actors,
    np.arange(19, 21)
)

test_mask = np.isin(
    actors,
    np.arange(21, 25)
)


X_train = X[train_mask]
y_train = y_encoded[train_mask]

X_val = X[val_mask]
y_val = y_encoded[val_mask]

X_test = X[test_mask]
y_test = y_encoded[test_mask]


print("\nActor-independent split:")
print("Training:", X_train.shape)
print("Validation:", X_val.shape)
print("Testing:", X_test.shape)


# ============================================================
# SHUFFLE TRAINING DATA
# ============================================================

rng = np.random.default_rng(42)

indices = rng.permutation(len(X_train))

X_train = X_train[indices]
y_train = y_train[indices]


# ============================================================
# NORMALIZATION
# ============================================================

# Calculate normalization values ONLY from training data

mean = X_train.mean(
    axis=(0, 1, 2),
    keepdims=True
)

std = X_train.std(
    axis=(0, 1, 2),
    keepdims=True
)

std = np.maximum(std, 1e-6)


X_train = (X_train - mean) / std
X_val = (X_val - mean) / std
X_test = (X_test - mean) / std


# Save normalization values

np.savez(
    NORMALIZATION_PATH,
    mean=mean,
    std=std
)


# ============================================================
# ADD CHANNEL DIMENSION IF NECESSARY
# ============================================================

# Expected shape:
# (samples, 40, 174, 4)

print("\nFinal input shape:")
print(X_train.shape)


# ============================================================
# CLASS WEIGHTS
# ============================================================

classes = np.unique(y_train)

weights = compute_class_weight(
    class_weight="balanced",
    classes=classes,
    y=y_train
)

class_weights = dict(
    zip(classes, weights)
)

print("\nClass weights:")

for key, value in class_weights.items():
    print(
        f"{class_names[key]:10s}: "
        f"{value:.4f}"
    )


# ============================================================
# BUILD CRNN MODEL
# ============================================================

input_shape = X_train.shape[1:]

inputs = layers.Input(
    shape=input_shape
)


# ------------------------------------------------------------
# Feature-level noise
# ------------------------------------------------------------

x = layers.GaussianNoise(
    0.03
)(inputs)


# ============================================================
# CNN BLOCK 1
# ============================================================

x = layers.Conv2D(
    32,
    (3, 3),
    padding="same",
    activation="relu"
)(x)

x = layers.BatchNormalization()(x)

x = layers.MaxPooling2D(
    pool_size=(2, 2)
)(x)

x = layers.Dropout(
    0.20
)(x)


# ============================================================
# CNN BLOCK 2
# ============================================================

x = layers.Conv2D(
    64,
    (3, 3),
    padding="same",
    activation="relu"
)(x)

x = layers.BatchNormalization()(x)

x = layers.MaxPooling2D(
    pool_size=(2, 2)
)(x)

x = layers.Dropout(
    0.25
)(x)


# ============================================================
# CNN BLOCK 3
# ============================================================

x = layers.Conv2D(
    128,
    (3, 3),
    padding="same",
    activation="relu"
)(x)

x = layers.BatchNormalization()(x)

x = layers.MaxPooling2D(
    pool_size=(2, 2)
)(x)

x = layers.Dropout(
    0.30
)(x)


# ============================================================
# CONVERT CNN FEATURES INTO SEQUENCE
# ============================================================

# After pooling:
#
# 40 -> 20 -> 10 -> 5
# 174 -> 87 -> 43 -> 21
#
# Shape:
# (5, 21, 128)
#
# We treat the 21 time steps as a sequence.

x = layers.Permute(
    (2, 1, 3)
)(x)


# Shape:
# (21, 5, 128)

x = layers.Reshape(
    (21, 5 * 128)
)(x)


# ============================================================
# BIDIRECTIONAL LSTM
# ============================================================

x = layers.Bidirectional(
    layers.LSTM(
        96,
        return_sequences=False
    )
)(x)

x = layers.Dropout(
    0.35
)(x)


# ============================================================
# CLASSIFICATION HEAD
# ============================================================

x = layers.Dense(
    128,
    activation="relu"
)(x)

x = layers.BatchNormalization()(x)

x = layers.Dropout(
    0.40
)(x)


outputs = layers.Dense(
    len(class_names),
    activation="softmax"
)(x)


# ============================================================
# CREATE MODEL
# ============================================================

model = models.Model(
    inputs=inputs,
    outputs=outputs
)


# ============================================================
# COMPILE
# ============================================================

model.compile(
    optimizer=tf.keras.optimizers.Adam(
        learning_rate=0.0005
    ),
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)


# ============================================================
# MODEL SUMMARY
# ============================================================

print("\n")
model.summary()


# ============================================================
# CALLBACKS
# ============================================================

early_stopping = EarlyStopping(
    monitor="val_loss",
    patience=10,
    restore_best_weights=True,
    verbose=1
)


reduce_lr = ReduceLROnPlateau(
    monitor="val_loss",
    factor=0.5,
    patience=4,
    min_lr=1e-6,
    verbose=1
)


checkpoint = ModelCheckpoint(
    MODEL_PATH,
    monitor="val_loss",
    save_best_only=True,
    verbose=1
)


# ============================================================
# TRAIN
# ============================================================

print("\n")
print("=" * 60)
print("STARTING TRAINING")
print("=" * 60)


history = model.fit(
    X_train,
    y_train,

    validation_data=(
        X_val,
        y_val
    ),

    epochs=60,
    batch_size=32,

    class_weight=class_weights,

    callbacks=[
        early_stopping,
        reduce_lr,
        checkpoint
    ],

    verbose=1
)


# ============================================================
# SAVE TRAINING HISTORY
# ============================================================

np.savez(
    HISTORY_PATH,
    loss=history.history["loss"],
    accuracy=history.history["accuracy"],
    val_loss=history.history["val_loss"],
    val_accuracy=history.history["val_accuracy"]
)


# ============================================================
# SAVE LABELS
# ============================================================

np.save(
    LABEL_PATH,
    class_names
)


# ============================================================
# FINAL TEST EVALUATION
# ============================================================

print("\n")
print("=" * 60)
print("FINAL TEST EVALUATION")
print("=" * 60)


test_loss, test_accuracy = model.evaluate(
    X_test,
    y_test,
    verbose=0
)


print(
    f"\nTest Loss: "
    f"{test_loss:.4f}"
)

print(
    f"Test Accuracy: "
    f"{test_accuracy * 100:.2f}%"
)


# ============================================================
# COMPLETE
# ============================================================

print("\n")
print("=" * 60)
print("TRAINING COMPLETE")
print("=" * 60)

print(
    f"\nModel saved to:\n"
    f"{MODEL_PATH}"
)

print(
    f"\nLabels saved to:\n"
    f"{LABEL_PATH}"
)

print(
    f"\nNormalization saved to:\n"
    f"{NORMALIZATION_PATH}"
)

print(
    f"\nTraining history saved to:\n"
    f"{HISTORY_PATH}"
)