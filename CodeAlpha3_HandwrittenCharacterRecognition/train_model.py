import os
import numpy as np
import tensorflow as tf

from tensorflow.keras import layers, models
from tensorflow.keras.callbacks import (
    EarlyStopping,
    ReduceLROnPlateau,
    ModelCheckpoint
)


# ============================================================
# CONFIGURATION
# ============================================================

DATA_PATH = "dataset/mnist_data.npz"
MODEL_DIR = "models"
MODEL_PATH = os.path.join(MODEL_DIR, "mnist_cnn.keras")

BATCH_SIZE = 128
EPOCHS = 20


# ============================================================
# LOAD DATA
# ============================================================

print("=" * 60)
print("Loading processed MNIST dataset")
print("=" * 60)

data = np.load(DATA_PATH)

X_train = data["X_train"]
y_train = data["y_train"]

X_test = data["X_test"]
y_test = data["y_test"]

print("Training data:", X_train.shape)
print("Test data    :", X_test.shape)


# ============================================================
# BUILD CNN MODEL
# ============================================================

print("\n" + "=" * 60)
print("Building CNN model")
print("=" * 60)

model = models.Sequential([
    
    layers.Input(shape=(28, 28, 1)),

    # --------------------------------------------------------
    # Convolution Block 1
    # --------------------------------------------------------
    layers.Conv2D(
        32,
        (3, 3),
        activation="relu",
        padding="same"
    ),
    layers.BatchNormalization(),
    layers.MaxPooling2D((2, 2)),
    layers.Dropout(0.25),

    # --------------------------------------------------------
    # Convolution Block 2
    # --------------------------------------------------------
    layers.Conv2D(
        64,
        (3, 3),
        activation="relu",
        padding="same"
    ),
    layers.BatchNormalization(),
    layers.MaxPooling2D((2, 2)),
    layers.Dropout(0.25),

    # --------------------------------------------------------
    # Convolution Block 3
    # --------------------------------------------------------
    layers.Conv2D(
        128,
        (3, 3),
        activation="relu",
        padding="same"
    ),
    layers.BatchNormalization(),
    layers.Dropout(0.30),

    # --------------------------------------------------------
    # Classification Head
    # --------------------------------------------------------
    layers.Flatten(),

    layers.Dense(
        128,
        activation="relu"
    ),
    layers.BatchNormalization(),
    layers.Dropout(0.40),

    layers.Dense(
        10,
        activation="softmax"
    )
])


# ============================================================
# COMPILE MODEL
# ============================================================

model.compile(
    optimizer=tf.keras.optimizers.Adam(
        learning_rate=0.001
    ),
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)


# ============================================================
# MODEL SUMMARY
# ============================================================

model.summary()


# ============================================================
# CALLBACKS
# ============================================================

os.makedirs(MODEL_DIR, exist_ok=True)

early_stopping = EarlyStopping(
    monitor="val_loss",
    patience=4,
    restore_best_weights=True,
    verbose=1
)

reduce_lr = ReduceLROnPlateau(
    monitor="val_loss",
    factor=0.5,
    patience=2,
    min_lr=1e-6,
    verbose=1
)

checkpoint = ModelCheckpoint(
    MODEL_PATH,
    monitor="val_accuracy",
    save_best_only=True,
    verbose=1
)


# ============================================================
# TRAIN MODEL
# ============================================================

print("\n" + "=" * 60)
print("Starting CNN training")
print("=" * 60)

history = model.fit(
    X_train,
    y_train,

    validation_split=0.1,

    epochs=EPOCHS,
    batch_size=BATCH_SIZE,

    shuffle=True,

    callbacks=[
        early_stopping,
        reduce_lr,
        checkpoint
    ],

    verbose=1
)


# ============================================================
# EVALUATE MODEL
# ============================================================

print("\n" + "=" * 60)
print("Evaluating model on test dataset")
print("=" * 60)

test_loss, test_accuracy = model.evaluate(
    X_test,
    y_test,
    verbose=1
)

print(f"\nTest Loss     : {test_loss:.4f}")
print(f"Test Accuracy : {test_accuracy:.4%}")


# ============================================================
# SAVE FINAL MODEL
# ============================================================

model.save(MODEL_PATH)

print("\n" + "=" * 60)
print("Training completed successfully!")
print("=" * 60)

print(f"Model saved to: {MODEL_PATH}")
print(f"Final test accuracy: {test_accuracy:.4%}")