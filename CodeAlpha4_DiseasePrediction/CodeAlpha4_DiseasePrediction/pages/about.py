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
    page_title="About | MediPredict",
    page_icon="ℹ️",
    layout="wide"
)

apply_custom_css()


# ============================================================
# HEADER
# ============================================================

md(
    """
    <div class="page-header">
        <div class="eyebrow">ABOUT THE PROJECT</div>
        <h1>About MediPredict</h1>
        <p>
            A machine learning project for exploring diabetes risk
            prediction using patient medical measurements.
        </p>
    </div>
    """
)


# ============================================================
# PROJECT OVERVIEW
# ============================================================

st.markdown("### 💡 Project Overview")

md(
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
    """
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

    md(
        f"""
        <div class="feature-row">
            <strong>{technology}</strong>
            <span>{description}</span>
        </div>
        """
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
# DEVELOPER
# ============================================================

st.markdown("### 👨‍💻 Developer")

md(
    """
    <div class="hero-card">
        <div class="eyebrow">DEVELOPED BY</div>
        <h2>Mehul Gupta</h2>
        <p>
            B.Tech Computer Science & Engineering student and
            aspiring software & machine learning developer.
        </p>
    </div>
    """
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

md(
    """
    <div class="disclaimer">
        <strong>⚠️ Medical Disclaimer</strong><br>
        This application is created strictly for educational and
        demonstration purposes. Predictions should not be interpreted
        as medical diagnoses or used to make healthcare decisions.
        Always consult a qualified healthcare professional for medical advice.
    </div>
    """
)


# ============================================================
# FOOTER
# ============================================================

render_footer()