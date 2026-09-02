import streamlit as st

from utils.styles import render_footer


# ============================================================
# HERO
# ============================================================

st.markdown(
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
    """,
    unsafe_allow_html=True
)


# ============================================================
# CTA
# ============================================================

col1, col2 = st.columns([1, 2])

with col1:

    if st.button(
        "🎤 Analyze Your Audio",
        use_container_width=True,
        type="primary"
    ):
        st.switch_page("pages/prediction.py")


# ============================================================
# STATS
# ============================================================

st.markdown("<br>", unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(
        """
        <div class="stat-card">
            <div class="stat-value">1,440</div>
            <div class="stat-label">Audio Samples</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with c2:
    st.markdown(
        """
        <div class="stat-card">
            <div class="stat-value">8</div>
            <div class="stat-label">Emotions</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with c3:
    st.markdown(
        """
        <div class="stat-card">
            <div class="stat-value">24</div>
            <div class="stat-label">Actors</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with c4:
    st.markdown(
        """
        <div class="stat-card">
            <div class="stat-value">CNN + BiLSTM</div>
            <div class="stat-label">Model Architecture</div>
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# ABOUT
# ============================================================

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown(
    '<div class="section-label">About the project</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="card">

        <div class="card-title">
            How does it work?
        </div>

        <div class="card-text">
            The application converts speech into numerical
            audio representations including MFCC, Delta,
            Delta-Delta and Mel-Spectrogram features.
            These features are processed by a convolutional
            neural network and a bidirectional LSTM to
            produce an emotion prediction.
        </div>

    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# WORKFLOW
# ============================================================

st.markdown(
    '<div class="section-label">Workflow</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <div class="card">
            <div style="font-size:2rem;">🎤</div>
            <div class="card-title">
                01 · Provide Audio
            </div>
            <div class="card-text">
                Upload a WAV file or record speech
                directly through your browser.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div class="card">
            <div style="font-size:2rem;">🔬</div>
            <div class="card-title">
                02 · Extract Features
            </div>
            <div class="card-text">
                Extract MFCC, delta, delta-delta and
                Mel-spectrogram representations.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        """
        <div class="card">
            <div style="font-size:2rem;">🧠</div>
            <div class="card-title">
                03 · Predict Emotion
            </div>
            <div class="card-text">
                The CNN-BiLSTM model predicts one
                of eight emotional categories.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# DISCLAIMER
# ============================================================

st.markdown("<br>", unsafe_allow_html=True)

st.warning(
    "This application is an educational machine-learning "
    "project. Its predictions are experimental and should "
    "not be treated as a definitive assessment of a person's "
    "actual emotional state."
)


render_footer()