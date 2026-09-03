import textwrap

import streamlit as st

from utils.styles import apply_custom_css, render_footer


def md(html: str) -> None:
    """
    st.markdown wrapper that strips leading indentation.

    Markdown treats any line indented with 4+ spaces as a
    preformatted code block. Because our HTML snippets live
    inside nested Python blocks (for loops, with-blocks, etc.),
    the triple-quoted strings pick up that indentation and get
    rendered as literal code instead of parsed HTML. Dedenting
    here fixes that for every call site.
    """
    st.markdown(textwrap.dedent(html).strip(), unsafe_allow_html=True)


# ============================================================
# CSS
# ============================================================

apply_custom_css()


# ============================================================
# HERO
# ============================================================

md(
    """
    <div class="hero">
        <div class="hero-badge">
            🎙️ Deep Learning · Speech Analysis
        </div>
        <div class="hero-title">
            Speech Emotion<br>
            Recognition
        </div>
        <div class="hero-subtitle">
            Analyze speech recordings and explore how
            deep learning can identify emotional patterns
            from audio.
        </div>
    </div>
    """
)


# ============================================================
# CTA
# ============================================================

col1, col2, col3 = st.columns([1.2, 1, 2])

with col1:
    if st.button(
        "🎤 Analyze Your Audio",
        type="primary",
        use_container_width=True
    ):
        st.switch_page("pages/prediction.py")


# ============================================================
# STATS
# ============================================================

st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

stats = [
    ("1,440", "Audio Samples"),
    ("8", "Emotions"),
    ("24", "Actors"),
    ("CNN + BiLSTM", "Architecture"),
]

for column, (value, label) in zip(
    [col1, col2, col3, col4],
    stats
):
    with column:
        md(
            f"""
            <div class="stat-card">
                <div class="stat-value">
                    {value}
                </div>
                <div class="stat-label">
                    {label}
                </div>
            </div>
            """
        )


# ============================================================
# ABOUT PROJECT
# ============================================================

md(
    """
    <div class="section-label">ABOUT THE PROJECT</div>
    <h2>How does it work?</h2>
    """
)

md(
    """
    <div class="content-card">
        <p>
            The application converts speech into numerical
            audio representations including MFCC, Delta,
            Delta-Delta and Mel-Spectrogram features.
        </p>
        <p>
            These features are processed by a convolutional
            neural network and a bidirectional LSTM to
            produce an emotion prediction.
        </p>
    </div>
    """
)


# ============================================================
# WORKFLOW
# ============================================================

md(
    """
    <div class="section-label">WORKFLOW</div>
    <h2>From Audio to Prediction</h2>
    """
)

steps = [
    (
        "01",
        "Record or Upload",
        "Provide a speech recording through the application."
    ),
    (
        "02",
        "Extract Features",
        "Convert the audio into MFCC, Delta, Delta-Delta and Log-Mel features."
    ),
    (
        "03",
        "Analyze with AI",
        "The CNN extracts spatial patterns while the BiLSTM captures temporal information."
    ),
    (
        "04",
        "Predict Emotion",
        "The trained model generates probabilities across eight emotion classes."
    ),
]

for number, title, description in steps:
    md(
        f"""
        <div class="workflow-step">
            <div class="workflow-number">
                {number}
            </div>
            <div>
                <h3>{title}</h3>
                <p>{description}</p>
            </div>
        </div>
        """
    )


# ============================================================
# SUPPORTED EMOTIONS
# ============================================================

md(
    """
    <div class="section-label">SUPPORTED EMOTIONS</div>
    <h2>What can the model recognize?</h2>
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
                <div class="emotion-icon">
                    {emoji}
                </div>
                <div class="emotion-name">
                    {emotion}
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
        <strong>⚠️ Educational Project</strong>
        <p>
            This application is designed for educational and
            experimental purposes. Speech emotion recognition
            predictions should not be interpreted as definitive
            statements about a person's actual emotional state.
        </p>
    </div>
    """
)


# ============================================================
# NAVIGATION
# ============================================================

st.markdown("<br>", unsafe_allow_html=True)

st.page_link(
    "pages/prediction.py",
    label="🎤 Start Emotion Prediction →",
    use_container_width=True
)


# ============================================================
# FOOTER
# ============================================================

render_footer()