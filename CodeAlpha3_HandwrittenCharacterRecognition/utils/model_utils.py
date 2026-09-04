import os
import numpy as np
import streamlit as st
import tensorflow as tf


# ============================================================
# CONFIGURATION
# ============================================================

MODEL_PATH = "models/mnist_cnn.keras"

DIGIT_LABELS = [
    "0", "1", "2", "3", "4",
    "5", "6", "7", "8", "9"
]


# ============================================================
# LOAD MODEL
# ============================================================

@st.cache_resource
def load_model():
    """
    Load the trained MNIST CNN model.
    Streamlit caches the model so it isn't reloaded
    every time the user interacts with the application.
    """

    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(
            f"Trained model not found at: {MODEL_PATH}"
        )

    model = tf.keras.models.load_model(MODEL_PATH)

    return model


# ============================================================
# PREDICTION
# ============================================================

def predict_digit(image_array):
    """
    Predict a handwritten digit from a preprocessed
    28x28 grayscale image.

    Expected input:
        (28, 28)
        or
        (28, 28, 1)

    Returns:
        predicted_digit
        confidence
        probabilities
    """

    model = load_model()

    image_array = np.asarray(
        image_array,
        dtype=np.float32
    )

    # --------------------------------------------------------
    # Ensure channel dimension exists
    # --------------------------------------------------------

    if image_array.ndim == 2:
        image_array = np.expand_dims(
            image_array,
            axis=-1
        )

    # --------------------------------------------------------
    # Ensure batch dimension exists
    # --------------------------------------------------------

    if image_array.ndim == 3:
        image_array = np.expand_dims(
            image_array,
            axis=0
        )

    # --------------------------------------------------------
    # Validate final shape
    # --------------------------------------------------------

    if image_array.shape != (1, 28, 28, 1):

        raise ValueError(
            "Expected image shape "
            f"(28, 28, 1), got {image_array.shape}"
        )

    # --------------------------------------------------------
    # Normalize if image is still in 0–255 range
    # --------------------------------------------------------

    if image_array.max() > 1.0:
        image_array = image_array / 255.0

    # --------------------------------------------------------
    # Model prediction
    # --------------------------------------------------------

    probabilities = model.predict(
        image_array,
        verbose=0
    )[0]

    predicted_index = int(
        np.argmax(probabilities)
    )

    predicted_digit = DIGIT_LABELS[
        predicted_index
    ]

    confidence = float(
        probabilities[predicted_index]
    )

    return (
        predicted_digit,
        confidence,
        probabilities
    )