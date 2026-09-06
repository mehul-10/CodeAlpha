import textwrap

import streamlit as st

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
    page_title="Home | MediPredict",
    page_icon="🏠",
    layout="wide"
)

apply_custom_css()


# ============================================================
# HERO
# ============================================================

md(
    """
    <div class="hero">
        <div class="hero-badge">
            CODEALPHA · MACHINE LEARNING TASK 4
        </div>
        <div class="hero-title">
            Diabetes Risk Prediction
        </div>
        <div class="hero-subtitle">
            An interactive machine learning application
            that estimates diabetes risk from commonly
            used medical measurements using a trained
            Random Forest classifier.
        </div>
    </div>
    """
)


# ============================================================
# CTA
# ============================================================

if st.button(
    "🩺 Try Disease Prediction",
    use_container_width=False
):

    st.switch_page(
        "pages/prediction.py"
    )


st.markdown("")


# ============================================================
# STATISTICS
# ============================================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    md(
        """
        <div class="stat-card">
            <div class="stat-value">768</div>
            <div class="stat-label">Patient Records</div>
        </div>
        """
    )

with col2:
    md(
        """
        <div class="stat-card">
            <div class="stat-value">8</div>
            <div class="stat-label">Medical Features</div>
        </div>
        """
    )

with col3:
    md(
        """
        <div class="stat-card">
            <div class="stat-value">73.38%</div>
            <div class="stat-label">Test Accuracy</div>
        </div>
        """
    )

with col4:
    md(
        """
        <div class="stat-card">
            <div class="stat-value">82.41%</div>
            <div class="stat-label">ROC-AUC</div>
        </div>
        """
    )


# ============================================================
# ABOUT
# ============================================================

st.markdown("##")

md(
    """
    <div class="content-card">
        <div class="card-title">
            About the Project
        </div>
        <div class="card-text">
            This project demonstrates a complete machine
            learning workflow for binary disease prediction.
            The system performs preprocessing, handles
            missing medical values, compares multiple
            classification algorithms and uses the best
            performing model for prediction.
        </div>
    </div>
    """
)


# ============================================================
# WORKFLOW
# ============================================================

st.markdown("### How It Works")

steps = [
    (
        "01",
        "Enter Medical Data",
        "Provide the patient's medical measurements."
    ),
    (
        "02",
        "Preprocess",
        "Missing and invalid values are handled automatically."
    ),
    (
        "03",
        "Predict",
        "The trained Random Forest model analyzes the inputs."
    ),
    (
        "04",
        "View Result",
        "Receive the predicted class and probability."
    )
]

for number, title, description in steps:

    md(
        f"""
        <div class="workflow-step">
            <div class="workflow-number">
                {number}
            </div>
            <div>
                <strong>{title}</strong><br>
                <span>{description}</span>
            </div>
        </div>
        """
    )


# ============================================================
# DISCLAIMER
# ============================================================

md(
    """
    <div class="disclaimer">
        <strong>Educational Disclaimer:</strong>
        This application is an educational machine learning
        project and should not be used as the sole basis for
        medical diagnosis or treatment decisions. Always
        consult a qualified healthcare professional for
        medical advice.
    </div>
    """
)


render_footer()