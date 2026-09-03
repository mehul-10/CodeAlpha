import streamlit as st
import pandas as pd

from utils.styles import render_footer

from utils.styles import apply_custom_css

apply_custom_css()
# ============================================================
# PAGE HEADER
# ============================================================

st.markdown(
    '<div class="section-label">MODEL & DATASET</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<h1 class="page-title">Model & Dataset</h1>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <p class="page-subtitle">
        Technical overview of the dataset, feature engineering,
        deep learning architecture, and evaluation methodology.
    </p>
    """,
    unsafe_allow_html=True
)


# ============================================================
# DATASET OVERVIEW
# ============================================================

st.markdown(
    '<div class="section-label">DATASET</div>',
    unsafe_allow_html=True
)

st.markdown(
    "### RAVDESS Speech Dataset"
)

st.markdown(
    """
    The model was trained using the **Ryerson Audio-Visual Database
    of Emotional Speech and Song (RAVDESS)** speech dataset.

    The dataset contains speech recordings from **24 actors**
    representing **8 different emotional categories**.
    """
)


# ============================================================
# DATASET STATISTICS
# ============================================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Audio Samples",
        "1,440"
    )

with col2:
    st.metric(
        "Emotions",
        "8"
    )

with col3:
    st.metric(
        "Actors",
        "24"
    )

with col4:
    st.metric(
        "Samples / Actor",
        "60"
    )


# ============================================================
# EMOTION CLASSES
# ============================================================

st.markdown("")

st.markdown(
    "### Emotion Classes"
)

emotion_data = pd.DataFrame(
    {
        "Emotion": [
            "Angry",
            "Calm",
            "Disgust",
            "Fearful",
            "Happy",
            "Neutral",
            "Sad",
            "Surprised",
        ],
        "Samples": [
            192,
            192,
            192,
            192,
            192,
            96,
            192,
            192,
        ],
    }
)

st.dataframe(
    emotion_data,
    use_container_width=True,
    hide_index=True
)


# ============================================================
# TRAIN / VALIDATION / TEST SPLIT
# ============================================================

st.markdown("---")

st.markdown(
    '<div class="section-label">DATA SPLIT</div>',
    unsafe_allow_html=True
)

st.markdown(
    "### Actor-Independent Evaluation"
)

st.markdown(
    """
    To reduce the possibility of the model learning
    speaker-specific characteristics, the dataset was divided
    by **actor identity** rather than randomly splitting
    individual audio files.
    """
)

split_data = pd.DataFrame(
    {
        "Split": [
            "Training",
            "Validation",
            "Testing",
        ],
        "Actors": [
            "1–18",
            "19–20",
            "21–24",
        ],
        "Samples": [
            1080,
            120,
            240,
        ],
    }
)

st.dataframe(
    split_data,
    use_container_width=True,
    hide_index=True
)


# ============================================================
# FEATURE ENGINEERING
# ============================================================

st.markdown("---")

st.markdown(
    '<div class="section-label">FEATURE ENGINEERING</div>',
    unsafe_allow_html=True
)

st.markdown(
    "### Multi-Channel Audio Representation"
)

st.markdown(
    """
    Each speech recording is converted into four complementary
    acoustic representations:

    **1. MFCC**  
    Mel-Frequency Cepstral Coefficients capture important
    characteristics of the speech spectrum.

    **2. Delta**  
    First-order temporal changes in the MFCC features.

    **3. Delta-Delta**  
    Second-order temporal changes in the speech signal.

    **4. Log-Mel Spectrogram**  
    Represents the distribution of acoustic energy across
    Mel-frequency bands.
    """
)


# ============================================================
# FEATURE SHAPE
# ============================================================

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "MFCC Coefficients",
        "40"
    )

with col2:

    st.metric(
        "Time Frames",
        "174"
    )

with col3:

    st.metric(
        "Channels",
        "4"
    )


st.code(
    """
Input Tensor
────────────────────
(40, 174, 4)

40   → Feature coefficients
174  → Time frames
4    → MFCC + Delta + Delta-Delta + Log-Mel
""",
    language="text"
)


# ============================================================
# MODEL ARCHITECTURE
# ============================================================

st.markdown("---")

st.markdown(
    '<div class="section-label">DEEP LEARNING MODEL</div>',
    unsafe_allow_html=True
)

st.markdown(
    "### CNN + Bidirectional LSTM"
)

st.markdown(
    """
    The model combines **Convolutional Neural Networks (CNN)**
    with a **Bidirectional Long Short-Term Memory (BiLSTM)**
    network.

    CNN layers learn local acoustic patterns from the
    time-frequency representation, while the BiLSTM processes
    temporal relationships in both forward and backward
    directions.
    """
)


# ============================================================
# ARCHITECTURE PIPELINE
# ============================================================

st.code(
    """
Input
(40 × 174 × 4)
        ↓
Conv2D
32 Filters
        ↓
Batch Normalization
        ↓
Max Pooling
        ↓
Dropout
        ↓
Conv2D
64 Filters
        ↓
Batch Normalization
        ↓
Max Pooling
        ↓
Dropout
        ↓
Conv2D
128 Filters
        ↓
Batch Normalization
        ↓
Max Pooling
        ↓
Dropout
        ↓
Reshape
        ↓
Bidirectional LSTM
96 Units
        ↓
Dense
128 Units
        ↓
Batch Normalization
        ↓
Dropout
        ↓
Softmax
8 Emotion Classes
""",
    language="text"
)


# ============================================================
# MODEL PARAMETERS
# ============================================================

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "Architecture",
        "CNN + BiLSTM"
    )

with col2:

    st.metric(
        "Output Classes",
        "8"
    )

with col3:

    st.metric(
        "Parameters",
        "686,696"
    )


# ============================================================
# TRAINING
# ============================================================

st.markdown("---")

st.markdown(
    '<div class="section-label">TRAINING</div>',
    unsafe_allow_html=True
)

st.markdown(
    "### Training Strategy"
)

training_data = pd.DataFrame(
    {
        "Technique": [
            "Normalization",
            "Class Weighting",
            "Gaussian Noise",
            "Early Stopping",
            "Learning Rate Reduction",
            "Model Checkpointing",
        ],
        "Purpose": [
            "Standardize feature values",
            "Handle class imbalance",
            "Improve generalization",
            "Prevent overfitting",
            "Improve optimization",
            "Save best validation model",
        ],
    }
)

st.dataframe(
    training_data,
    use_container_width=True,
    hide_index=True
)


# ============================================================
# MODEL PERFORMANCE
# ============================================================

st.markdown("---")

st.markdown(
    '<div class="section-label">EVALUATION</div>',
    unsafe_allow_html=True
)

st.markdown(
    "### Test Performance"
)

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "Test Accuracy",
        "28.75%"
    )

with col2:

    st.metric(
        "Test Samples",
        "240"
    )

with col3:

    st.metric(
        "Random Baseline",
        "12.50%"
    )


st.info(
    """
    The current model performs above the theoretical random
    baseline for eight classes, but its accuracy is still
    relatively low. The result demonstrates a working
    end-to-end speech emotion recognition pipeline rather
    than a production-ready emotion classifier.
    """
)


# ============================================================
# LIMITATIONS
# ============================================================

st.markdown("---")

st.markdown(
    '<div class="section-label">LIMITATIONS</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    ### Important Considerations

    - The model is trained on the **RAVDESS dataset** and may
      not generalize well to other speakers, languages,
      microphones, environments, or speaking styles.

    - Emotion recognition from speech is inherently
      probabilistic.

    - Model confidence does not represent psychological
      certainty.

    - The current test performance is not sufficient for
      high-stakes or real-world emotional assessment.

    - The application should be treated as an **educational
      machine learning project**.
    """
)


# ============================================================
# DATASET SOURCE
# ============================================================

st.markdown("---")

st.markdown(
    '<div class="section-label">DATASET INFORMATION</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    **Dataset:** Ryerson Audio-Visual Database of Emotional
    Speech and Song (RAVDESS)

    **License:** CC BY-NC-SA 4.0

    The dataset is used here for educational and research
    purposes.
    """
)


# ============================================================
# NAVIGATION
# ============================================================

st.markdown("---")

col1, col2 = st.columns(2)

with col1:

    st.page_link(
        "pages/analysis.py",
        label="← Audio Analysis",
        use_container_width=True
    )

with col2:

    st.page_link(
        "pages/about.py",
        label="About Project →",
        use_container_width=True
    )


# ============================================================
# DISCLAIMER
# ============================================================

st.markdown("---")

st.warning(
    """
    **Disclaimer:** This application is an educational machine
    learning project. Speech emotion recognition is probabilistic
    and should not be treated as a definitive assessment of a
    person's emotional or psychological state.
    """
)


# ============================================================
# FOOTER
# ============================================================

render_footer()