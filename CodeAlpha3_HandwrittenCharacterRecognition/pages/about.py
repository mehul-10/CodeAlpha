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
    page_title="About | DigitAI",
    page_icon="ℹ️",
    layout="wide",
    initial_sidebar_state="expanded"
)

apply_custom_css()


# ============================================================
# HEADER
# ============================================================

md(
    """
    <div class="page-header">
        <div class="section-label">
            ABOUT THE PROJECT
        </div>
        <h1>
            DigitAI
        </h1>
        <p>
            A deep learning application for recognizing handwritten
            digits using a Convolutional Neural Network trained on
            the MNIST dataset.
        </p>
    </div>
    """
)


# ============================================================
# PROJECT INTRODUCTION
# ============================================================

md(
    """
    <div class="content-card">
        <div class="card-title">
            ✍️ What is DigitAI?
        </div>
        <div class="card-text">
            DigitAI is a handwritten digit recognition application
            developed as part of the <strong>CodeAlpha Machine Learning
            Internship</strong>.
            <br><br>
            The application uses a Convolutional Neural Network (CNN)
            trained on the MNIST dataset to classify handwritten digits
            from <strong>0 to 9</strong>.
            <br><br>
            Users can upload an image containing a handwritten digit.
            The application automatically preprocesses the image,
            sends it through the trained neural network, and displays
            the predicted digit along with its confidence score.
        </div>
    </div>
    """
)


# ============================================================
# KEY STATISTICS
# ============================================================

st.markdown("### 📊 Project at a Glance")

col1, col2, col3, col4 = st.columns(4)


with col1:

    md(
        """
        <div class="stat-card">
            <div class="stat-value">
                60K
            </div>
            <div class="stat-label">
                Training Images
            </div>
        </div>
        """
    )


with col2:

    md(
        """
        <div class="stat-card">
            <div class="stat-value">
                10K
            </div>
            <div class="stat-label">
                Test Images
            </div>
        </div>
        """
    )


with col3:

    md(
        """
        <div class="stat-card">
            <div class="stat-value">
                10
            </div>
            <div class="stat-label">
                Digit Classes
            </div>
        </div>
        """
    )


with col4:

    md(
        """
        <div class="stat-card">
            <div class="stat-value">
                99.5%
            </div>
            <div class="stat-label">
                Test Accuracy
            </div>
        </div>
        """
    )


# ============================================================
# TECHNOLOGY STACK
# ============================================================

st.markdown("### 🛠️ Technology Stack")

col1, col2 = st.columns(2)


with col1:

    md(
        """
        <div class="content-card">
            <div class="card-title">
                🤖 Machine Learning
            </div>
            <div class="card-text">
                <strong>Python</strong><br>
                Used as the primary programming language.
                <br><br>
                <strong>TensorFlow / Keras</strong><br>
                Used to build and train the CNN.
                <br><br>
                <strong>MNIST</strong><br>
                Dataset used for handwritten digit recognition.
                <br><br>
                <strong>NumPy</strong><br>
                Used for numerical operations and image arrays.
            </div>
        </div>
        """
    )


with col2:

    md(
        """
        <div class="content-card">
            <div class="card-title">
                🌐 Application
            </div>
            <div class="card-text">
                <strong>Streamlit</strong><br>
                Used to build the interactive web application.
                <br><br>
                <strong>Pillow</strong><br>
                Used for image loading and preprocessing.
                <br><br>
                <strong>Matplotlib</strong><br>
                Used for model evaluation visualizations.
                <br><br>
                <strong>Scikit-learn</strong><br>
                Used for classification metrics and evaluation.
            </div>
        </div>
        """
    )


# ============================================================
# APPLICATION WORKFLOW
# ============================================================

st.markdown("### 🔄 Application Workflow")


workflow = [
    (
        "01",
        "Upload",
        "Upload a PNG, JPG, or JPEG image containing a handwritten digit."
    ),
    (
        "02",
        "Preprocess",
        "Convert the image to grayscale, crop the digit, resize it, center it, and normalize the pixels."
    ),
    (
        "03",
        "Predict",
        "The trained CNN analyzes the processed image and calculates probabilities for all ten digits."
    ),
    (
        "04",
        "Result",
        "The application displays the predicted digit, confidence score, and probability distribution."
    ),
]


for number, title, description in workflow:

    md(
        f"""
        <div class="workflow-step">
            <div class="workflow-number">
                {number}
            </div>
            <div>
                <strong>
                    {title}
                </strong>
                <br>
                <span>
                    {description}
                </span>
            </div>
        </div>
        """
    )


# ============================================================
# PROJECT FEATURES
# ============================================================

st.markdown("### ✨ Key Features")

col1, col2, col3 = st.columns(3)


with col1:

    md(
        """
        <div class="content-card">
            <div class="card-title">
                ✍️ Digit Prediction
            </div>
            <div class="card-text">
                Upload a handwritten digit image and receive
                an instant prediction from the trained CNN.
            </div>
        </div>
        """
    )


with col2:

    md(
        """
        <div class="content-card">
            <div class="card-title">
                🎯 Confidence Score
            </div>
            <div class="card-text">
                View the model's confidence for its predicted
                digit together with probabilities for all classes.
            </div>
        </div>
        """
    )


with col3:

    md(
        """
        <div class="content-card">
            <div class="card-title">
                📊 Model Analysis
            </div>
            <div class="card-text">
                Explore accuracy, precision, recall, F1-score,
                confusion matrix, and per-digit performance.
            </div>
        </div>
        """
    )


# ============================================================
# MODEL PERFORMANCE
# ============================================================

st.markdown("### 🧠 Model Performance")

md(
    """
    <div class="content-card">
        <div class="card-title">
            CNN Performance
        </div>
        <div class="card-text">
            The trained CNN achieved a test accuracy of
            <strong>99.50%</strong> on the MNIST test dataset.
            <br><br>
            The model uses multiple convolutional layers to learn
            visual patterns such as edges, curves, strokes, and
            shapes within handwritten digits.
            <br><br>
            Batch normalization and dropout are used to improve
            training stability and reduce overfitting.
        </div>
    </div>
    """
)


# ============================================================
# PROJECT STRUCTURE
# ============================================================

st.markdown("### 📁 Project Structure")

st.code(
    """
CodeAlpha3_HandwrittenCharacterRecognition/
│
├── app.py
│
├── dataset/
│   └── mnist_data.npz
│
├── models/
│   ├── mnist_cnn.keras
│   └── evaluation/
│       ├── classification_report.txt
│       ├── confusion_matrix.png
│       ├── per_digit_accuracy.png
│       └── evaluation_metrics.npz
│
├── pages/
│   ├── home.py
│   ├── prediction.py
│   ├── analysis.py
│   ├── model_info.py
│   └── about.py
│
└── utils/
    ├── image_utils.py
    ├── model_utils.py
    └── styles.py
    """,
    language="text"
)


# ============================================================
# DEVELOPER
# ============================================================

st.markdown("### 👨‍💻 Developer")

md(
    """
    <div class="content-card">
        <div class="card-title">
            Mehul Gupta
        </div>
        <div class="card-text">
            Computer Science & Engineering Student
            <br>
            Machine Learning & Full-Stack Development Enthusiast
            <br><br>
            This project was developed as part of the
            <strong>CodeAlpha Machine Learning Internship</strong>.
        </div>
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
        "https://github.com/mehul-10",
        use_container_width=True
    )


with col2:

    st.link_button(
        "LinkedIn",
        "https://www.linkedin.com/in/mehulgupta-developer/",
        use_container_width=True
    )


# ============================================================
# EDUCATIONAL DISCLAIMER
# ============================================================

md(
    """
    <div class="disclaimer">
        <strong>Educational Project</strong>
        <br><br>
        DigitAI was developed for educational and demonstration
        purposes as part of a machine learning internship.
        <br><br>
        The reported 99.50% accuracy is based on the MNIST test
        dataset. Performance on arbitrary real-world handwriting,
        photographs, different backgrounds, or unusual writing
        styles may be lower.
    </div>
    """
)


# ============================================================
# FOOTER
# ============================================================

render_footer()