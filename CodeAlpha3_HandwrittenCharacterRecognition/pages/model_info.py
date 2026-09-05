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
    page_title="Model & Dataset",
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
        <div class="section-label">MODEL & DATASET</div>
        <h1>Inside DigitAI</h1>
        <p>
            Explore the dataset, neural network architecture,
            training process, and performance of the handwritten
            digit recognition model.
        </p>
    </div>
    """
)


# ============================================================
# DATASET OVERVIEW
# ============================================================

md(
    """
    <div class="content-card">
        <div class="card-title">📚 MNIST Dataset</div>
        <div class="card-text">
            DigitAI is trained using the MNIST handwritten digit dataset.
            MNIST contains grayscale images of handwritten digits from
            0 through 9 and is one of the most widely used benchmark
            datasets for image classification.
        </div>
    </div>
    """
)


# ============================================================
# DATASET STATS
# ============================================================

st.markdown("### Dataset Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Training Images", "60,000")

with col2:
    st.metric("Test Images", "10,000")

with col3:
    st.metric("Image Size", "28 × 28")

with col4:
    st.metric("Classes", "10")


# ============================================================
# DATASET DETAILS
# ============================================================

st.markdown("### Dataset Details")

col1, col2 = st.columns(2)

with col1:
    md(
        """
        <div class="content-card">
            <div class="card-title">Image Properties</div>
            <div class="card-text">
                • Grayscale images<br>
                • Resolution: 28 × 28 pixels<br>
                • Single image channel<br>
                • Pixel values normalized to 0–1<br>
                • Ten digit classes: 0–9
            </div>
        </div>
        """
    )

with col2:
    md(
        """
        <div class="content-card">
            <div class="card-title">Preprocessing</div>
            <div class="card-text">
                • Convert image to grayscale<br>
                • Detect the handwritten region<br>
                • Crop unnecessary background<br>
                • Resize digit while preserving proportions<br>
                • Center digit on a 28 × 28 canvas<br>
                • Normalize pixel values
            </div>
        </div>
        """
    )


# ============================================================
# MODEL ARCHITECTURE
# ============================================================

st.markdown("### 🧠 CNN Architecture")

md(
    """
    <div class="content-card">
        <div class="card-title">Convolutional Neural Network</div>
        <div class="card-text">
            The recognition model uses a Convolutional Neural Network
            designed to learn visual patterns from handwritten digits.
            Convolutional layers identify features such as edges,
            curves, shapes, and increasingly complex digit structures.
        </div>
    </div>
    """
)


# Architecture steps

architecture = [
    ("01", "Input Layer", "28 × 28 × 1 grayscale image"),
    ("02", "Conv2D", "32 filters + Batch Normalization"),
    ("03", "MaxPooling", "Spatial downsampling + Dropout"),
    ("04", "Conv2D", "64 filters + Batch Normalization"),
    ("05", "MaxPooling", "Spatial downsampling + Dropout"),
    ("06", "Conv2D", "128 filters + Batch Normalization"),
    ("07", "Flatten", "Convert learned features into a vector"),
    ("08", "Dense", "128 neurons + Batch Normalization"),
    ("09", "Output", "10-class Softmax prediction"),
]

for number, title, description in architecture:
    md(
        f"""
        <div class="workflow-step">
            <div class="workflow-number">{number}</div>
            <div>
                <strong>{title}</strong><br>
                <span>{description}</span>
            </div>
        </div>
        """
    )


# ============================================================
# TRAINING CONFIGURATION
# ============================================================

st.markdown("### ⚙️ Training Configuration")

training_data = {
    "Parameter": [
        "Optimizer",
        "Learning Rate",
        "Loss Function",
        "Batch Size",
        "Maximum Epochs",
        "Validation Split",
        "Early Stopping",
        "Learning Rate Reduction",
    ],
    "Value": [
        "Adam",
        "0.001",
        "Sparse Categorical Crossentropy",
        "128",
        "20",
        "10%",
        "Enabled",
        "Enabled",
    ],
}

st.dataframe(
    training_data,
    use_container_width=True,
    hide_index=True
)


# ============================================================
# PERFORMANCE
# ============================================================

st.markdown("### 📈 Model Performance")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Test Accuracy",
        "99.50%"
    )

with col2:
    st.metric(
        "Test Loss",
        "0.0169"
    )

with col3:
    st.metric(
        "Number of Classes",
        "10"
    )


# ============================================================
# WHY CNN?
# ============================================================

md(
    """
    <div class="content-card">
        <div class="card-title">Why a CNN?</div>
        <div class="card-text">
            CNNs are particularly effective for image classification
            because they preserve spatial relationships between pixels.
            Instead of treating every pixel independently, convolutional
            filters learn local visual patterns and combine them into
            higher-level features.
            <br><br>
            For handwritten digits, this allows the model to learn
            patterns such as strokes, curves, intersections, and loops
            that distinguish one digit from another.
        </div>
    </div>
    """
)


# ============================================================
# MODEL LIMITATIONS
# ============================================================

st.markdown("### ⚠️ Model Limitations")

md(
    """
    <div class="disclaimer">
        <strong>Important:</strong><br><br>
        This model is trained on the MNIST dataset, which contains
        relatively clean 28 × 28 handwritten digit images.
        Real-world handwriting can differ significantly in size,
        thickness, orientation, background, lighting, and writing style.
        Therefore, the reported 99.5% test accuracy should not be
        interpreted as guaranteed performance on arbitrary real-world
        images.
    </div>
    """
)


# ============================================================
# FOOTER
# ============================================================

render_footer()