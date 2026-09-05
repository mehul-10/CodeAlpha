import textwrap

import streamlit as st

from utils.styles import apply_custom_css, render_footer


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
    page_title="Home | Handwritten Digit Recognition",
    page_icon="✍️",
    layout="wide"
)

apply_custom_css()


# ============================================================
# HERO SECTION
# ============================================================

md(
    """
    <div class="hero">
        <div class="hero-badge">
            CODEALPHA · MACHINE LEARNING PROJECT
        </div>
        <div class="hero-title">
            Handwritten Digit<br>
            Recognition with AI
        </div>
        <div class="hero-subtitle">
            A convolutional neural network trained on the MNIST
            dataset to recognize handwritten digits from 0 to 9.
        </div>
    </div>
    """
)


# ============================================================
# START BUTTON
# ============================================================

if st.button(
    "✍️ Try Digit Recognition",
    use_container_width=False
):
    st.switch_page("pages/prediction.py")


# ============================================================
# STATISTICS
# ============================================================

md("<br>")

col1, col2, col3, col4 = st.columns(4)

with col1:

    md(
        """
        <div class="stat-card">
            <div class="stat-value">60K</div>
            <div class="stat-label">Training Images</div>
        </div>
        """
    )

with col2:

    md(
        """
        <div class="stat-card">
            <div class="stat-value">10K</div>
            <div class="stat-label">Test Images</div>
        </div>
        """
    )

with col3:

    md(
        """
        <div class="stat-card">
            <div class="stat-value">10</div>
            <div class="stat-label">Digit Classes</div>
        </div>
        """
    )

with col4:

    md(
        """
        <div class="stat-card">
            <div class="stat-value">99.5%</div>
            <div class="stat-label">Test Accuracy</div>
        </div>
        """
    )


# ============================================================
# ABOUT PROJECT
# ============================================================

md(
    """
    <div class="section-label">
        ABOUT THE PROJECT
    </div>
    <div class="content-card">
        <div class="card-title">
            How does it work?
        </div>
        <div class="card-text">
            The application uses a Convolutional Neural Network
            trained on 60,000 handwritten digit images from the
            MNIST dataset. When you upload an image, it is
            converted to grayscale, cropped, resized and
            normalized before being passed to the CNN.
        </div>
        <br>
        <div class="card-text">
            The model then calculates the probability of each
            digit from <strong>0 to 9</strong> and returns the
            digit with the highest predicted probability.
        </div>
    </div>
    """
)


# ============================================================
# WORKFLOW
# ============================================================

md(
    """
    <div class="section-label">
        WORKFLOW
    </div>
    <div class="content-card">
        <div class="card-title">
            From image to prediction
        </div>
        <div class="card-text">
            The recognition pipeline consists of four main stages.
        </div>
        <br>
        <div class="workflow-step">
            <div class="workflow-number">01</div>
            <div>
                <strong>Upload</strong><br>
                <span>Provide an image containing a handwritten digit.</span>
            </div>
        </div>
        <br>
        <div class="workflow-step">
            <div class="workflow-number">02</div>
            <div>
                <strong>Preprocess</strong><br>
                <span>The image is converted, cropped, resized and normalized.</span>
            </div>
        </div>
        <br>
        <div class="workflow-step">
            <div class="workflow-number">03</div>
            <div>
                <strong>Predict</strong><br>
                <span>The CNN analyzes the processed 28 × 28 image.</span>
            </div>
        </div>
        <br>
        <div class="workflow-step">
            <div class="workflow-number">04</div>
            <div>
                <strong>Result</strong><br>
                <span>The predicted digit and probability distribution are displayed.</span>
            </div>
        </div>
    </div>
    """
)


# ============================================================
# SUPPORTED DIGITS
# ============================================================

md(
    """
    <div class="section-label">
        SUPPORTED DIGITS
    </div>
    """
)

digits = [
    "0", "1", "2", "3", "4",
    "5", "6", "7", "8", "9"
]

digit_cols = st.columns(5)

for index, digit in enumerate(digits):

    with digit_cols[index % 5]:

        md(
            f"""
            <div class="content-card" style="text-align:center;">
                <div style="font-size:42px; font-weight:800; color:#111111;">
                    {digit}
                </div>
                <div style="font-size:13px; color:#777777;">
                    Digit {digit}
                </div>
            </div>
            """
        )


# ============================================================
# MODEL PERFORMANCE
# ============================================================

md(
    """
    <div class="section-label">
        MODEL PERFORMANCE
    </div>
    <div class="content-card">
        <div class="card-title">
            CNN performance
        </div>
        <div class="card-text">
            The trained CNN achieved a <strong>99.50%</strong>
            accuracy on the 10,000-image MNIST test dataset.
            These test images were not used during model training.
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
        <strong>Educational Project</strong><br>
        This application was developed as part of a machine
        learning internship project. The reported 99.50% accuracy
        represents performance on the MNIST test dataset and does
        not guarantee the same performance on arbitrary
        real-world handwritten images.
    </div>
    """
)


# ============================================================
# FOOTER
# ============================================================

render_footer()