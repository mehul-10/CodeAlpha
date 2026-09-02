import os
import numpy as np
import tensorflow as tf

from sklearn.preprocessing import LabelEncoder
from sklearn.utils.class_weight import compute_class_weight
from sklearn.metrics import classification_report

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
    "speech_emotion_cnn.keras"
)

LABEL_PATH = os.path.join(
    MODEL_DIR,
    "emotion_labels.npy"
)

SEED = 42

np.random.seed(SEED)
tf.random.set_seed(SEED)

os.makedirs(MODEL_DIR, exist_ok=True)


# ============================================================
# LOAD DATA
# ============================================================

print("=" * 60)
print("SPEECH EMOTION RECOGNITION")
print("IMPROVED CNN TRAINING")
print("=" * 60)

data = np.load(DATA_PATH)

X = data["X"]
y = data["y"]
actors = data["actors"]

print("\nDataset loaded:")
print(f"Features : {X.shape}")
print(f"Labels   : {y.shape}")
print(f"Actors   : {actors.shape}")


# ============================================================
# LABEL ENCODING
# ============================================================

encoder = LabelEncoder()

y_encoded = encoder.fit_transform(y)

class_names = encoder.classes_

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


print("\n" + "=" * 60)
print("ACTOR-INDEPENDENT DATA SPLIT")
print("=" * 60)

print(f"Training   : {len(X_train)}")
print(f"Validation : {len(X_val)}")
print(f"Testing    : {len(X_test)}")


# ============================================================
# SHUFFLE TRAINING DATA
# ============================================================

indices = np.random.permutation(
    len(X_train)
)

X_train = X_train[indices]
y_train = y_train[indices]


# ============================================================
# NORMALIZATION
# ============================================================

# Calculate statistics only from training data.

mean = np.mean(
    X_train,
    axis=(0, 1, 2),
    keepdims=True
)

std = np.std(
    X_train,
    axis=(0, 1, 2),
    keepdims=True
)

X_train = (
    X_train - mean
) / (
    std + 1e-8
)

X_val = (
    X_val - mean
) / (
    std + 1e-8
)

X_test = (
    X_test - mean
) / (
    std + 1e-8
)


print("\nNormalization complete.")


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

for class_id, weight in class_weights.items():

    print(
        f"{class_names[class_id]:10s}: "
        f"{weight:.3f}"
    )


# ============================================================
# DATA AUGMENTATION
# ============================================================

data_augmentation = tf.keras.Sequential([

    layers.RandomTranslation(
        height_factor=0.08,
        width_factor=0.08,
        fill_mode="nearest"
    ),

    layers.RandomZoom(
        height_factor=0.08,
        width_factor=0.08
    )

], name="feature_augmentation")


# ============================================================
# CNN MODEL
# ============================================================

model = models.Sequential([

    layers.Input(
        shape=X_train.shape[1:]
    ),

    # ========================================================
    # AUGMENTATION
    # ========================================================

    data_augmentation,


    # ========================================================
    # CNN BLOCK 1
    # ========================================================

    layers.Conv2D(
        32,
        (3, 3),
        padding="same",
        activation="relu"
    ),

    layers.BatchNormalization(),

    layers.MaxPooling2D(
        (2, 2)
    ),

    layers.Dropout(0.20),


    # ========================================================
    # CNN BLOCK 2
    # ========================================================

    layers.Conv2D(
        64,
        (3, 3),
        padding="same",
        activation="relu"
    ),

    layers.BatchNormalization(),

    layers.MaxPooling2D(
        (2, 2)
    ),

    layers.Dropout(0.25),


    # ========================================================
    # CNN BLOCK 3
    # ========================================================

    layers.Conv2D(
        128,
        (3, 3),
        padding="same",
        activation="relu"
    ),

    layers.BatchNormalization(),

    layers.MaxPooling2D(
        (2, 2)
    ),

    layers.Dropout(0.30),


    # ========================================================
    # CNN BLOCK 4
    # ========================================================

    layers.Conv2D(
        256,
        (3, 3),
        padding="same",
        activation="relu"
    ),

    layers.BatchNormalization(),

    layers.MaxPooling2D(
        (2, 2)
    ),

    layers.Dropout(0.30),


    # ========================================================
    # GLOBAL POOLING
    # ========================================================

    layers.GlobalAveragePooling2D(),


    # ========================================================
    # CLASSIFIER
    # ========================================================

    layers.Dense(
        128,
        activation="relu"
    ),

    layers.BatchNormalization(),

    layers.Dropout(0.40),

    layers.Dense(
        len(class_names),
        activation="softmax"
    )

])


# ============================================================
# COMPILE
# ============================================================

model.compile(

    optimizer=tf.keras.optimizers.Adam(
        learning_rate=0.0005
    ),

    loss="sparse_categorical_crossentropy",

    metrics=[
        "accuracy"
    ]
)


# ============================================================
# MODEL SUMMARY
# ============================================================

print("\n" + "=" * 60)
print("MODEL ARCHITECTURE")
print("=" * 60)

model.summary()


# ============================================================
# CALLBACKS
# ============================================================

checkpoint = ModelCheckpoint(

    MODEL_PATH,

    monitor="val_accuracy",

    mode="max",

    save_best_only=True,

    verbose=1
)


early_stopping = EarlyStopping(

    monitor="val_accuracy",

    mode="max",

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


# ============================================================
# TRAIN
# ============================================================

print("\n" + "=" * 60)
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
        checkpoint,
        early_stopping,
        reduce_lr
    ],

    verbose=1
)


# ============================================================
# LOAD BEST MODEL
# ============================================================

print("\nLoading best model...")

model = tf.keras.models.load_model(
    MODEL_PATH
)


# ============================================================
# FINAL TEST
# ============================================================

print("\n" + "=" * 60)
print("FINAL TEST RESULTS")
print("=" * 60)

test_loss, test_accuracy = model.evaluate(
    X_test,
    y_test,
    verbose=0
)

print(
    f"\nTest Loss     : {test_loss:.4f}"
)

print(
    f"Test Accuracy : {test_accuracy * 100:.2f}%"
)


# ============================================================
# PREDICTIONS
# ============================================================

probabilities = model.predict(
    X_test,
    verbose=0
)

predictions = np.argmax(
    probabilities,
    axis=1
)


# ============================================================
# CLASSIFICATION REPORT
# ============================================================

print("\n" + "=" * 60)
print("CLASSIFICATION REPORT")
print("=" * 60)

print(
    classification_report(
        y_test,
        predictions,
        target_names=class_names,
        zero_division=0
    )
)


# ============================================================
# SAVE LABELS
# ============================================================

np.save(
    LABEL_PATH,
    class_names
)


# ============================================================
# SAVE NORMALIZATION PARAMETERS
# ============================================================

np.savez(
    os.path.join(
        MODEL_DIR,
        "normalization.npz"
    ),
    mean=mean,
    std=std
)


# ============================================================
# COMPLETE
# ============================================================

print("\n" + "=" * 60)
print("TRAINING COMPLETE")
print("=" * 60)

print(
    f"Model saved to: {MODEL_PATH}"
)

print(
    f"Labels saved to: {LABEL_PATH}"
)

print(
    "Normalization saved to: "
    "models\\normalization.npz"
)