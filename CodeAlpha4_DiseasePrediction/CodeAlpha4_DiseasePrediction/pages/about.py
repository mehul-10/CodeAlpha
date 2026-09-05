import streamlit as st

from utils.styles import inject_css, render_footer


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="About | MediPredict",
    page_icon="ℹ️",
    layout="wide"
)

inject_css()


# ============================================================
# HEADER
# ============================================================

st.markdown(
    """
    <div class="page-header">
        <div class="eyebrow">ABOUT THE PROJECT</div>
        <h1>About MediPredict</h1>
        <p>
            A machine learning project for exploring diabetes risk
            prediction using patient medical measurements.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# PROJECT OVERVIEW
# ============================================================

st.markdown("### 💡 Project Overview")

st.markdown(
    """
    <div class="info-card">
        <p>
            MediPredict is an educational machine learning application
            developed as part of the CodeAlpha Machine Learning Internship.
        </p>

        <p>
            The application uses patient medical measurements and a
            trained Random Forest classifier to estimate the likelihood
            of diabetes.
        </p>

        <p>
            The project demonstrates the complete machine learning
            workflow — from data preprocessing and model training to
            evaluation and deployment through Streamlit.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# TECHNOLOGY STACK
# ============================================================

st.markdown("### 🛠️ Technology Stack")

technologies = [
    ("Python", "Core programming language"),
    ("Pandas", "Data manipulation and analysis"),
    ("NumPy", "Numerical computing"),
    ("Scikit-learn", "Machine learning and preprocessing"),
    ("Matplotlib", "Data visualization"),
    ("Seaborn", "Statistical visualization"),
    ("Joblib", "Model serialization"),
    ("Streamlit", "Interactive web application")
]

for technology, description in technologies:

    st.markdown(
        f"""
        <div class="feature-row">
            <strong>{technology}</strong>
            <span>{description}</span>
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# PROJECT WORKFLOW
# ============================================================

st.markdown("### 🔄 Machine Learning Workflow")

workflow = [
    ("01", "Data Collection", "Load the diabetes dataset."),
    ("02", "Data Exploration", "Analyze distributions, missing values and correlations."),
    ("03", "Preprocessing", "Handle invalid values and scale features."),
    ("04", "Model Training", "Train Logistic Regression, Random Forest and SVM."),
    ("05", "Evaluation", "Compare models using classification metrics and ROC-AUC."),
    ("06", "Deployment", "Build an interactive Streamlit prediction application.")
]

for number, title, description in workflow:

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
# DEVELOPER
# ============================================================

st.markdown("### 👨‍💻 Developer")

st.markdown(
    """
    <div class="hero-card">
        <div class="eyebrow">DEVELOPED BY</div>
        <h2>Mehul Gupta</h2>
        <p>
            B.Tech Computer Science & Engineering student and
            aspiring software & machine learning developer.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# LINKS
# ============================================================

st.markdown("### 🔗 Connect")

col1, col2 = st.columns(2)

with col1:
    st.link_button(
        "GitHub",
        "https://github.com/mehul-10"
    )

with col2:
    st.link_button(
        "LinkedIn",
        "https://www.linkedin.com/in/mehulgupta-developer/"
    )


# ============================================================
# DISCLAIMER
# ============================================================

st.markdown(
    """
    <div class="disclaimer">
        <strong>⚠️ Medical Disclaimer</strong><br>
        This application is created strictly for educational and
        demonstration purposes. Predictions should not be interpreted
        as medical diagnoses or used to make healthcare decisions.
        Always consult a qualified healthcare professional for medical advice.
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# FOOTER
# ============================================================

render_footer()