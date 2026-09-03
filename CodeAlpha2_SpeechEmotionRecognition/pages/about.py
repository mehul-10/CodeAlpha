import textwrap

import streamlit as st

from utils.styles import render_footer
from utils.styles import apply_custom_css


def md(html: str) -> None:
    """
    st.markdown wrapper that strips leading indentation.

    Markdown treats any line indented with 4+ spaces as a
    preformatted code block. HTML snippets defined inside
    nested Python blocks (with/for) pick up that indentation
    from the triple-quoted string and get rendered as literal
    code instead of parsed HTML. Dedenting fixes that.
    """
    st.markdown(textwrap.dedent(html).strip(), unsafe_allow_html=True)


apply_custom_css()


# ============================================================
# PAGE HEADER
# ============================================================

md(
    """
    <div class="page-header">
        <div class="section-label">ABOUT THE PROJECT</div>
        <h1>Built to Explore Speech & AI</h1>
        <p>
            A deep learning project that analyzes speech recordings
            and predicts the emotion expressed in the audio.
        </p>
    </div>
    """
)


# ============================================================
# PROJECT OVERVIEW
# ============================================================

md(
    """
    <div class="content-card">
        <h2>🎙️ Speech Emotion Recognition</h2>
        <p>
            This project demonstrates how machine learning and deep learning
            can be applied to human speech to identify emotional patterns.
        </p>
        <p>
            Audio recordings are transformed into meaningful time-frequency
            representations using MFCCs, Delta features, Delta-Delta features,
            and Log-Mel Spectrograms. These features are then processed by a
            hybrid CNN and Bidirectional LSTM architecture.
        </p>
        <p>
            The application provides an interactive interface where users can
            upload or record audio, inspect its acoustic characteristics,
            and obtain a model prediction.
        </p>
    </div>
    """
)


# ============================================================
# TECHNOLOGY STACK
# ============================================================

md(
    """
    <div class="section-label">TECHNOLOGY STACK</div>
    <h2>Tools & Technologies</h2>
    """
)

col1, col2, col3 = st.columns(3)

with col1:
    md(
        """
        <div class="content-card">
            <h3>🐍 Python</h3>
            <p>
                Core programming language used for data processing,
                feature extraction, model training, and application logic.
            </p>
        </div>
        """
    )

with col2:
    md(
        """
        <div class="content-card">
            <h3>🧠 TensorFlow</h3>
            <p>
                Used to build and train the CNN + Bidirectional LSTM
                deep learning model.
            </p>
        </div>
        """
    )

with col3:
    md(
        """
        <div class="content-card">
            <h3>🎨 Streamlit</h3>
            <p>
                Provides the interactive web interface for audio prediction,
                analysis, and model exploration.
            </p>
        </div>
        """
    )


# ============================================================
# AUDIO PROCESSING
# ============================================================

md(
    """
    <div class="section-label">AUDIO PROCESSING</div>
    <h2>How the Audio Is Processed</h2>
    """
)

steps = [
    (
        "01",
        "Audio Input",
        "The user uploads or records a speech sample."
    ),
    (
        "02",
        "Feature Extraction",
        "The audio is converted into MFCC, Delta, Delta-Delta, and Log-Mel features."
    ),
    (
        "03",
        "Deep Learning",
        "The extracted features are processed through convolutional and recurrent layers."
    ),
    (
        "04",
        "Prediction",
        "The model produces probabilities for eight possible emotional classes."
    ),
]

for number, title, description in steps:
    md(
        f"""
        <div class="workflow-step">
            <div class="workflow-number">{number}</div>
            <div>
                <h3>{title}</h3>
                <p>{description}</p>
            </div>
        </div>
        """
    )


# ============================================================
# EMOTIONS
# ============================================================

md(
    """
    <div class="section-label">SUPPORTED EMOTIONS</div>
    <h2>Emotion Classes</h2>
    """
)

emotions = [
    ("😠", "Angry"),
    ("😌", "Calm"),
    ("🤢", "Disgust"),
    ("😨", "Fearful"),
    ("😊", "Happy"),
    ("😐", "Neutral"),
    ("😢", "Sad"),
    ("😲", "Surprised"),
]

cols = st.columns(4)

for index, (emoji, emotion) in enumerate(emotions):

    with cols[index % 4]:

        md(
            f"""
            <div class="emotion-card">
                <div class="emotion-icon">{emoji}</div>
                <div class="emotion-name">
                    {emotion}
                </div>
            </div>
            """
        )


# ============================================================
# DEVELOPER
# ============================================================

md(
    """
    <div class="section-label">DEVELOPER</div>
    <h2>Created by Mehul Gupta</h2>
    """
)

md(
    """
    <div class="content-card">
        <p>
            This project was developed as part of a Machine Learning
            internship to gain practical experience in audio processing,
            feature engineering, deep learning, model evaluation,
            and deployment.
        </p>
        <p>
            The goal was not only to train a model, but also to build a
            complete end-to-end machine learning application with an
            interactive user interface.
        </p>
    </div>
    """
)


# ============================================================
# LINKS
# ============================================================

md(
    """
    <div class="section-label">CONNECT</div>
    <h2>Find Me Online</h2>
    """
)

col1, col2 = st.columns(2)

with col1:

    md(
        """
        <a href="https://github.com/mehul-10"
           target="_blank"
           class="link-card">
            <div class="link-icon">💻</div>
            <div>
                <strong>GitHub</strong>
                <p>View my projects and source code</p>
            </div>
        </a>
        """
    )

with col2:

    md(
        """
        <a href="https://www.linkedin.com/in/mehulgupta-developer/"
           target="_blank"
           class="link-card">
            <div class="link-icon">💼</div>
            <div>
                <strong>LinkedIn</strong>
                <p>Connect with me professionally</p>
            </div>
        </a>
        """
    )


# ============================================================
# DISCLAIMER
# ============================================================

md(
    """
    <div class="disclaimer">
        <strong>⚠️ Important Disclaimer</strong>
        <p>
            This application is an educational machine learning project.
            Speech emotion recognition is an inherently difficult task and
            model predictions should not be treated as definitive statements
            about a person's actual emotional state.
        </p>
        <p>
            Performance can vary depending on recording quality,
            speaker characteristics, language, background noise,
            and other factors.
        </p>
    </div>
    """
)


# ============================================================
# NAVIGATION
# ============================================================

st.markdown("<br>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.page_link(
        "pages/home.py",
        label="← Back to Home",
        use_container_width=True
    )

with col2:
    st.page_link(
        "pages/model_info.py",
        label="🧠 Model & Dataset →",
        use_container_width=True
    )


# ============================================================
# FOOTER
# ============================================================

render_footer()