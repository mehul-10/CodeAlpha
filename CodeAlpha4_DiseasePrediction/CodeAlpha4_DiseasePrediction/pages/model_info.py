import textwrap

import streamlit as st

from app_utils.styles import apply_custom_css, render_footer


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


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Model & Dataset | MediPredict",
    page_icon="🧠",
    layout="wide"
)

apply_custom_css()


# ============================================================
# HEADER
# ============================================================

md(
    """
    <div class="page-header">
        <div class="eyebrow">TECHNICAL DETAILS</div>
        <h1>Model & Dataset</h1>
        <p>
            Understand the dataset, features, preprocessing pipeline,
            and machine learning algorithms used by MediPredict.
        </p>
    </div>
    """
)


# ============================================================
# DATASET
# ============================================================

st.markdown("### 📁 Dataset")

md(
    """
    <div class="info-card">
        <h3>Pima Indians Diabetes Dataset</h3>
        <p>
            The project uses a dataset containing medical measurements
            used to predict whether a patient has diabetes.
        </p>
    </div>
    """
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Records", "768")

with col2:
    st.metric("Input Features", "8")

with col3:
    st.metric("Target Classes", "2")


# ============================================================
# FEATURES
# ============================================================

st.markdown("### 🧬 Input Features")

features = {
    "Pregnancies": "Number of pregnancies",
    "Glucose": "Plasma glucose concentration",
    "BloodPressure": "Diastolic blood pressure",
    "SkinThickness": "Triceps skin fold thickness",
    "Insulin": "Serum insulin level",
    "BMI": "Body Mass Index",
    "DiabetesPedigreeFunction": "Diabetes pedigree function",
    "Age": "Age of the patient"
}

for feature, description in features.items():

    md(
        f"""
        <div class="feature-row">
            <strong>{feature}</strong>
            <span>{description}</span>
        </div>
        """
    )


# ============================================================
# PREPROCESSING
# ============================================================

st.markdown("### ⚙️ Data Preprocessing")

steps = [
    ("01", "Load Dataset", "Read the diabetes dataset into a Pandas DataFrame."),
    ("02", "Handle Missing Values", "Replace invalid zero values with missing values where appropriate."),
    ("03", "Median Imputation", "Fill missing numerical values using the median."),
    ("04", "Feature Scaling", "Standardize numerical features using StandardScaler."),
    ("05", "Train/Test Split", "Use an 80/20 stratified split for training and testing.")
]

for number, title, description in steps:

    md(
        f"""
        <div class="workflow-step">
            <div class="workflow-number">{number}</div>
            <div>
                <strong>{title}</strong>
                <p>{description}</p>
            </div>
        </div>
        """
    )


# ============================================================
# MODELS
# ============================================================

st.markdown("### 🤖 Machine Learning Models")

models = [
    (
        "Logistic Regression",
        "A linear classification algorithm used as a baseline model."
    ),
    (
        "Random Forest",
        "An ensemble of decision trees capable of learning non-linear relationships."
    ),
    (
        "Support Vector Machine",
        "A classification algorithm that finds an optimal decision boundary."
    )
]

for name, description in models:

    md(
        f"""
        <div class="info-card">
            <h3>{name}</h3>
            <p>{description}</p>
        </div>
        """
    )


# ============================================================
# SELECTED MODEL
# ============================================================

st.markdown("### 🏆 Final Model")

md(
    """
    <div class="hero-card">
        <div class="eyebrow">SELECTED MODEL</div>
        <h2>Random Forest Classifier</h2>
        <p>
            Random Forest achieved the best F1 score among the tested
            models and was selected as the final prediction model.
        </p>
    </div>
    """
)


# ============================================================
# EVALUATION METRICS
# ============================================================

st.markdown("### 📊 Evaluation Metrics")

metric_descriptions = {
    "Accuracy": "Percentage of all predictions that were correct.",
    "Precision": "Percentage of predicted positive cases that were actually positive.",
    "Recall": "Percentage of actual positive cases correctly detected.",
    "F1 Score": "Harmonic mean of precision and recall.",
    "ROC-AUC": "Measures how effectively the model separates the two classes."
}

for metric, description in metric_descriptions.items():

    md(
        f"""
        <div class="feature-row">
            <strong>{metric}</strong>
            <span>{description}</span>
        </div>
        """
    )


# ============================================================
# DISCLAIMER
# ============================================================

md(
    """
    <div class="disclaimer">
        <strong>⚠️ Important</strong><br>
        MediPredict is an educational machine learning project.
        It is not intended for medical diagnosis, treatment decisions,
        or clinical use.
    </div>
    """
)


# ============================================================
# FOOTER
# ============================================================

render_footer()