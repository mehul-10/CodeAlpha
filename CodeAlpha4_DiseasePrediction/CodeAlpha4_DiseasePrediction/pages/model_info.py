import streamlit as st

from utils.styles import inject_css, render_footer


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Model & Dataset | MediPredict",
    page_icon="🧠",
    layout="wide"
)

inject_css()


# ============================================================
# HEADER
# ============================================================

st.markdown(
    """
    <div class="page-header">
        <div class="eyebrow">TECHNICAL DETAILS</div>
        <h1>Model & Dataset</h1>
        <p>
            Understand the dataset, features, preprocessing pipeline,
            and machine learning algorithms used by MediPredict.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# DATASET
# ============================================================

st.markdown("### 📁 Dataset")

st.markdown(
    """
    <div class="info-card">
        <h3>Pima Indians Diabetes Dataset</h3>
        <p>
            The project uses a dataset containing medical measurements
            used to predict whether a patient has diabetes.
        </p>
    </div>
    """,
    unsafe_allow_html=True
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

    st.markdown(
        f"""
        <div class="feature-row">
            <strong>{feature}</strong>
            <span>{description}</span>
        </div>
        """,
        unsafe_allow_html=True
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

    st.markdown(
        f"""
        <div class="workflow-step">
            <div class="workflow-number">{number}</div>
            <div>
                <strong>{title}</strong>
                <p>{description}</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
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

    st.markdown(
        f"""
        <div class="info-card">
            <h3>{name}</h3>
            <p>{description}</p>
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# SELECTED MODEL
# ============================================================

st.markdown("### 🏆 Final Model")

st.markdown(
    """
    <div class="hero-card">
        <div class="eyebrow">SELECTED MODEL</div>
        <h2>Random Forest Classifier</h2>
        <p>
            Random Forest achieved the best F1 score among the tested
            models and was selected as the final prediction model.
        </p>
    </div>
    """,
    unsafe_allow_html=True
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

    st.markdown(
        f"""
        <div class="feature-row">
            <strong>{metric}</strong>
            <span>{description}</span>
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# DISCLAIMER
# ============================================================

st.markdown(
    """
    <div class="disclaimer">
        <strong>⚠️ Important</strong><br>
        MediPredict is an educational machine learning project.
        It is not intended for medical diagnosis, treatment decisions,
        or clinical use.
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# FOOTER
# ============================================================

render_footer()