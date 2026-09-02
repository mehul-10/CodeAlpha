import os

import numpy as np
import streamlit as st
import tensorflow as tf


MODEL_PATH = "models/speech_emotion_crnn.keras"
LABEL_PATH = "models/emotion_labels.npy"
NORMALIZATION_PATH = "models/normalization.npz"


EMOTION_EMOJIS = {
    "angry": "😠",
    "calm": "😌",
    "disgust": "🤢",
    "fearful": "😨",
    "happy": "😊",
    "neutral": "😐",
    "sad": "😢",
    "surprised": "😲",
}


@st.cache_resource
def load_emotion_model():

    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(
            f"Model not found: {MODEL_PATH}"
        )

    return tf.keras.models.load_model(
        MODEL_PATH
    )


@st.cache_resource
def load_labels():

    if not os.path.exists(LABEL_PATH):
        raise FileNotFoundError(
            f"Labels not found: {LABEL_PATH}"
        )

    return np.load(
        LABEL_PATH,
        allow_pickle=True
    )


@st.cache_resource
def load_normalization():

    if not os.path.exists(NORMALIZATION_PATH):
        raise FileNotFoundError(
            f"Normalization file not found: "
            f"{NORMALIZATION_PATH}"
        )

    data = np.load(
        NORMALIZATION_PATH
    )

    return data["mean"], data["std"]


def predict_emotion(features):

    model = load_emotion_model()
    labels = load_labels()
    mean, std = load_normalization()

    # Apply training normalization
    features = (
        features - mean
    ) / std

    # Add batch dimension only when necessary
    if features.ndim == 3:
        features = np.expand_dims(
            features,
            axis=0
        )

    probabilities = model.predict(
        features,
        verbose=0
    )[0]

    predicted_index = int(
        np.argmax(probabilities)
    )

    emotion = str(
        labels[predicted_index]
    )

    confidence = float(
        probabilities[predicted_index]
    )

    return (
        emotion,
        confidence,
        probabilities
    )