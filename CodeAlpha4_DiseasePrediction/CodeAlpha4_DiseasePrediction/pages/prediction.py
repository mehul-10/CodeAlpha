import textwrap

import streamlit as st

from app_utils.model_utils import predict_disease
from app_utils.styles import (
    apply_custom_css,
    render_footer
)


def md(html: str) -> None:
    """
    st.markdown wrapper that strips leading indentation.

    Markdown treats any line indented with 4+ spaces as a
    preformatted code block. HTML snippets defined inside
    nested Python blocks (with/if/for) pick up that indentation
    from the triple-quoted string and get rendered as literal
    code instead of parsed HTML. Dedenting fixes that.

    IMPORTANT: blank lines *inside* the HTML also break rendering,
    since Markdown treats a blank line as the end of a raw HTML
    block. Never leave a fully empty line between tags in the
    strings passed to this function -- use <br> instead.
    """
    st.markdown(textwrap.dedent(html).strip(), unsafe_allow_html=True)


st.set_page_config(
    page_title="Disease Prediction | MediPredict",
    page_icon="🩺",
    layout="wide"
)

apply_custom_css()


# ============================================================
# HEADER
# ============================================================

md(
    """
    <div class="page-header">
        <div class="section-label">
            MEDICAL RISK ASSESSMENT
        </div>
        <div class="page-title">
            Diabetes Risk Prediction
        </div>
        <div class="page-subtitle">
            Enter the patient's medical measurements below.
            The trained machine learning model will estimate
            the probability of diabetes.
        </div>
    </div>
    """
)


# ============================================================
# INPUT CARD
# ============================================================

md(
    """
    <div class="content-card">
        <div class="card-title">
            Patient Information
        </div>
        <div class="card-text">
            Enter the patient's measurements as accurately
            as possible.
        </div>
    </div>
    """
)


# ============================================================
# INPUTS
# ============================================================

col1, col2 = st.columns(2)


with col1:

    pregnancies = st.number_input(
        "Pregnancies",
        min_value=0,
        max_value=20,
        value=1,
        step=1,
        help="Number of times the patient has been pregnant."
    )

    glucose = st.number_input(
        "Glucose Level",
        min_value=1.0,
        max_value=300.0,
        value=120.0,
        step=1.0,
        help="Plasma glucose concentration."
    )

    blood_pressure = st.number_input(
        "Blood Pressure",
        min_value=1.0,
        max_value=200.0,
        value=70.0,
        step=1.0,
        help="Diastolic blood pressure."
    )

    skin_thickness = st.number_input(
        "Skin Thickness",
        min_value=0.0,
        max_value=100.0,
        value=20.0,
        step=1.0,
        help="Triceps skin fold thickness."
    )


with col2:

    insulin = st.number_input(
        "Insulin",
        min_value=0.0,
        max_value=900.0,
        value=80.0,
        step=1.0,
        help="Two-hour serum insulin."
    )

    bmi = st.number_input(
        "BMI",
        min_value=1.0,
        max_value=70.0,
        value=25.0,
        step=0.1,
        format="%.1f",
        help="Body Mass Index."
    )

    diabetes_pedigree = st.number_input(
        "Diabetes Pedigree Function",
        min_value=0.0,
        max_value=3.0,
        value=0.5,
        step=0.01,
        format="%.2f",
        help="Diabetes pedigree function."
    )

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=120,
        value=30,
        step=1,
        help="Patient's age in years."
    )


# ============================================================
# PREDICTION BUTTON
# ============================================================

st.markdown("")

predict_button = st.button(
    "🩺 Predict Diabetes Risk",
    use_container_width=True
)


# ============================================================
# PREDICTION
# ============================================================

if predict_button:

    values = [
        pregnancies,
        glucose,
        blood_pressure,
        skin_thickness,
        insulin,
        bmi,
        diabetes_pedigree,
        age
    ]

    try:

        prediction, no_diabetes_probability, diabetes_probability = (
            predict_disease(values)
        )

        # ----------------------------------------------------
        # RESULT
        # ----------------------------------------------------

        if prediction == 1:

            result_title = "Higher Diabetes Risk"
            result_icon = "⚠️"

        else:

            result_title = "Lower Diabetes Risk"
            result_icon = "✓"


        md(
            f"""
            <div class="prediction-card">
                <div class="prediction-icon">{result_icon}</div>
                <div class="prediction-title">{result_title}</div>
                <div class="prediction-confidence">
                    Model-estimated probability of diabetes:
                    <strong>{diabetes_probability * 100:.2f}%</strong>
                </div>
            </div>
            """
        )


        # ----------------------------------------------------
        # PROBABILITY METRICS
        # ----------------------------------------------------

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "No Diabetes Probability",
                f"{no_diabetes_probability * 100:.2f}%"
            )

        with col2:

            st.metric(
                "Diabetes Probability",
                f"{diabetes_probability * 100:.2f}%"
            )


        # ----------------------------------------------------
        # PROBABILITY BAR
        # ----------------------------------------------------

        st.markdown("### Risk Probability")

        st.progress(
            diabetes_probability
        )


        # ----------------------------------------------------
        # INTERPRETATION
        # ----------------------------------------------------

        if diabetes_probability >= 0.70:

            message = (
                "The model estimates a relatively high "
                "probability of diabetes based on the "
                "provided measurements."
            )

        elif diabetes_probability >= 0.40:

            message = (
                "The model estimates an intermediate "
                "probability of diabetes based on the "
                "provided measurements."
            )

        else:

            message = (
                "The model estimates a relatively lower "
                "probability of diabetes based on the "
                "provided measurements."
            )


        st.info(message)


        # ----------------------------------------------------
        # INPUT SUMMARY
        # ----------------------------------------------------

        with st.expander(
            "View submitted medical measurements"
        ):

            input_data = {
                "Pregnancies": pregnancies,
                "Glucose": glucose,
                "Blood Pressure": blood_pressure,
                "Skin Thickness": skin_thickness,
                "Insulin": insulin,
                "BMI": bmi,
                "Diabetes Pedigree": diabetes_pedigree,
                "Age": age
            }

            st.dataframe(
                input_data,
                use_container_width=True
            )


    except Exception as error:

        st.error(
            f"Prediction failed: {error}"
        )


# ============================================================
# DISCLAIMER
# ============================================================

md(
    """
    <div class="disclaimer">
        <strong>Important:</strong>
        This prediction is generated by a machine learning
        model for educational purposes only. It is not a
        medical diagnosis and should not replace evaluation
        by a qualified healthcare professional.
    </div>
    """
)


render_footer()