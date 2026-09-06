import os
from pathlib import Path

import joblib
import pandas as pd
import streamlit as st


# app_utils/model_utils.py -> parent is app_utils/, parent.parent is the
# app root. Using an absolute path anchored to this file avoids relying
# on the process's current working directory, which on Streamlit Cloud
# is the repo root rather than this project's subfolder.
BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = str(BASE_DIR / "models" / "disease_prediction_model.pkl")


FEATURES = [
    "Pregnancies",
    "Glucose",
    "BloodPressure",
    "SkinThickness",
    "Insulin",
    "BMI",
    "DiabetesPedigreeFunction",
    "Age"
]


@st.cache_resource
def load_model():

    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(
            f"Model not found at: {MODEL_PATH}"
        )

    return joblib.load(MODEL_PATH)


def predict_disease(values):

    model = load_model()

    data = pd.DataFrame(
        [values],
        columns=FEATURES
    )

    prediction = int(
        model.predict(data)[0]
    )

    probability = model.predict_proba(
        data
    )[0]

    return (
        prediction,
        float(probability[0]),
        float(probability[1])
    )