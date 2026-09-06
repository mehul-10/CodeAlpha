import os
import joblib
import pandas as pd
import streamlit as st


MODEL_PATH = "models/disease_prediction_model.pkl"


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