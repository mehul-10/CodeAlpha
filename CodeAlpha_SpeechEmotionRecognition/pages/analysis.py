import os
import tempfile

import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

from audio_features import extract_mfcc
from utils.audio_utils import get_audio_info
from utils.styles import render_footer


# ============================================================
# PAGE HEADER
# ============================================================

st.markdown(
    '<div class="section-label">AUDIO ANALYSIS</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<h1 class="page-title">Explore Your Audio</h1>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <p class="page-subtitle">
        Visualize the acoustic characteristics of your speech
        through waveform, spectrogram, and MFCC analysis.
    </p>
    """,
    unsafe_allow_html=True
)


# ============================================================
# CHECK FOR AUDIO
# ============================================================

audio_bytes = st.session_state.get(
    "analysis_audio_bytes"
)

audio_name = st.session_state.get(
    "analysis_audio_name",
    "recorded_audio.wav"
)


if audio_bytes is None:

    st.info(
        "🎙️ No audio available yet. "
        "Go to Emotion Prediction, upload or record audio, "
        "and then return here to analyze it."
    )

    if st.button(
        "Go to Emotion Prediction",
        use_container_width=False
    ):
        st.switch_page("pages/prediction.py")

    st.stop()


# ============================================================
# CREATE TEMP AUDIO FILE
# ============================================================

suffix = ".wav"

if audio_name.lower().endswith(".mp3"):
    suffix = ".mp3"

temp_path = None

try:

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=suffix
    ) as temp_file:

        temp_file.write(audio_bytes)
        temp_path = temp_file.name


    # ========================================================
    # AUDIO PLAYER
    # ========================================================

    st.markdown(
        '<div class="section-label">AUDIO</div>',
        unsafe_allow_html=True
    )

    st.audio(
        audio_bytes,
        format="audio/wav"
    )


    # ========================================================
    # AUDIO INFORMATION
    # ========================================================

    info = get_audio_info(temp_path)

    audio = info["audio"]
    sample_rate = info["sample_rate"]
    duration = info["duration"]


    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Duration",
            f"{duration:.2f} sec"
        )

    with col2:
        st.metric(
            "Sample Rate",
            f"{sample_rate:,} Hz"
        )

    with col3:
        st.metric(
            "Samples",
            f"{len(audio):,}"
        )


    # ========================================================
    # WAVEFORM
    # ========================================================

    st.markdown(
        '<div class="section-label">WAVEFORM</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        "### Amplitude over Time"
    )

    fig, ax = plt.subplots(
        figsize=(12, 4)
    )

    time = np.linspace(
        0,
        duration,
        len(audio)
    )

    ax.plot(
        time,
        audio
    )

    ax.set_xlabel(
        "Time (seconds)"
    )

    ax.set_ylabel(
        "Amplitude"
    )

    ax.set_title(
        "Speech Waveform"
    )

    ax.grid(
        alpha=0.2
    )

    plt.tight_layout()

    st.pyplot(
        fig,
        use_container_width=True
    )

    plt.close(fig)


    # ========================================================
    # SPECTROGRAM
    # ========================================================

    st.markdown(
        '<div class="section-label">SPECTROGRAM</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        "### Frequency Content over Time"
    )

    spectrogram = librosa.feature.melspectrogram(
        y=audio,
        sr=sample_rate,
        n_mels=128,
        n_fft=2048,
        hop_length=512
    )

    spectrogram_db = librosa.power_to_db(
        spectrogram,
        ref=np.max
    )

    fig, ax = plt.subplots(
        figsize=(12, 5)
    )

    img = librosa.display.specshow(
        spectrogram_db,
        sr=sample_rate,
        hop_length=512,
        x_axis="time",
        y_axis="mel",
        ax=ax
    )

    ax.set_title(
        "Mel Spectrogram"
    )

    fig.colorbar(
        img,
        ax=ax,
        format="%+2.0f dB"
    )

    plt.tight_layout()

    st.pyplot(
        fig,
        use_container_width=True
    )

    plt.close(fig)


    # ========================================================
    # MFCC
    # ========================================================

    st.markdown(
        '<div class="section-label">MFCC</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        "### Mel-Frequency Cepstral Coefficients"
    )

    mfcc = librosa.feature.mfcc(
        y=audio,
        sr=sample_rate,
        n_mfcc=40
    )

    fig, ax = plt.subplots(
        figsize=(12, 6)
    )

    img = librosa.display.specshow(
        mfcc,
        sr=sample_rate,
        hop_length=512,
        x_axis="time",
        ax=ax
    )

    ax.set_title(
        "40 MFCC Coefficients"
    )

    ax.set_ylabel(
        "MFCC Coefficient"
    )

    fig.colorbar(
        img,
        ax=ax
    )

    plt.tight_layout()

    st.pyplot(
        fig,
        use_container_width=True
    )

    plt.close(fig)


    # ========================================================
    # MODEL FEATURES
    # ========================================================

    st.markdown(
        '<div class="section-label">MODEL FEATURES</div>',
        unsafe_allow_html=True
    )

    features = extract_mfcc(
        temp_path
    )

    if features is not None:

        st.markdown(
            """
            <div class="info-card">
                <h3>Feature Representation</h3>
                <p>
                    The emotion recognition model combines four
                    acoustic representations:
                </p>
                <ul>
                    <li>MFCC</li>
                    <li>Delta MFCC</li>
                    <li>Delta-Delta MFCC</li>
                    <li>Log-Mel Spectrogram</li>
                </ul>
                <p>
                    Final feature shape:
                    <strong>40 × 174 × 4</strong>
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )


except Exception as e:

    st.error(
        f"Unable to analyze this audio: {e}"
    )


finally:

    if temp_path and os.path.exists(temp_path):

        try:
            os.remove(temp_path)

        except Exception:
            pass


# ============================================================
# DISCLAIMER
# ============================================================

st.warning(
    """
    This application is an educational machine learning project.
    Speech emotion recognition is probabilistic and should not be
    treated as a definitive assessment of a person's emotional state.
    """
)


# ============================================================
# FOOTER
# ============================================================

render_footer()