import os
import tempfile
import textwrap

import streamlit as st
import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt

from audio_features import extract_mfcc
from utils.audio_utils import (
    get_audio_info,
    cleanup_audio,
)
from utils.styles import render_footer
from utils.styles import apply_custom_css


def md(html: str) -> None:
    """
    st.markdown wrapper that strips leading indentation.

    Markdown treats any line indented with 4+ spaces as a
    preformatted code block. HTML snippets defined inside
    nested Python blocks (with/if/for) pick up that indentation
    from the triple-quoted string and get rendered as literal
    code instead of parsed HTML. Dedenting fixes that.
    """
    st.markdown(textwrap.dedent(html).strip(), unsafe_allow_html=True)


apply_custom_css()

# ============================================================
# PAGE HEADER
# ============================================================

md('<div class="section-label">AUDIO ANALYSIS</div>')

md('<h1 class="page-title">Audio Analysis</h1>')

md(
    """
    <p class="page-subtitle">
        Explore the acoustic characteristics of your speech through
        waveform, Mel spectrogram, and MFCC visualizations.
    </p>
    """
)


# ============================================================
# CHECK AUDIO
# ============================================================

audio_bytes = st.session_state.get(
    "analysis_audio_bytes"
)

audio_name = st.session_state.get(
    "analysis_audio_name",
    "audio.wav"
)


if audio_bytes is None:

    st.info(
        "🎙️ No audio is available for analysis."
    )

    st.page_link(
        "pages/prediction.py",
        label="← Go to Emotion Prediction",
        use_container_width=True
    )

    render_footer()

    st.stop()


# ============================================================
# CREATE TEMP AUDIO FILE
# ============================================================

temp_path = None


try:

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".wav"
    ) as temp_file:

        temp_file.write(audio_bytes)
        temp_path = temp_file.name


    # ========================================================
    # AUDIO PLAYER
    # ========================================================

    md('<div class="section-label">AUDIO SAMPLE</div>')

    md(
        f"""
        <div class="info-card">
            <h3>🎧 {audio_name}</h3>
            <p>
                Analyze the acoustic characteristics of your
                uploaded or recorded speech.
            </p>
        </div>
        """
    )

    st.audio(
        audio_bytes,
        format="audio/wav"
    )


    # ========================================================
    # AUDIO INFORMATION
    # ========================================================

    audio_info = get_audio_info(
        temp_path
    )

    duration = audio_info["duration"]
    sample_rate = audio_info["sample_rate"]


    # ========================================================
    # AUDIO METRICS
    # ========================================================

    st.markdown("")

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
            "Audio Samples",
            f"{audio_info.get('samples', 0):,}"
        )


    # ========================================================
    # LOAD AUDIO
    # ========================================================

    audio, sr = librosa.load(
        temp_path,
        sr=None
    )


    # ========================================================
    # WAVEFORM
    # ========================================================

    st.markdown("---")

    md('<div class="section-label">WAVEFORM</div>')

    st.markdown(
        "### 🎵 Time-Domain Waveform"
    )

    fig, ax = plt.subplots(
        figsize=(12, 4)
    )

    time_axis = np.linspace(
        0,
        len(audio) / sr,
        num=len(audio)
    )

    ax.plot(
        time_axis,
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
    # MEL SPECTROGRAM
    # ========================================================

    st.markdown("---")

    md('<div class="section-label">SPECTRAL ANALYSIS</div>')

    st.markdown(
        "### 🌈 Mel Spectrogram"
    )

    mel = librosa.feature.melspectrogram(
        y=audio,
        sr=sr,
        n_mels=40,
        n_fft=2048,
        hop_length=512
    )

    mel_db = librosa.power_to_db(
        mel,
        ref=np.max
    )

    fig, ax = plt.subplots(
        figsize=(12, 5)
    )

    img = librosa.display.specshow(
        mel_db,
        sr=sr,
        hop_length=512,
        x_axis="time",
        y_axis="mel",
        ax=ax
    )

    ax.set_title(
        "Mel-Frequency Spectrogram"
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

    st.markdown("---")

    md('<div class="section-label">FEATURE EXTRACTION</div>')

    st.markdown(
        "### 📊 MFCC Features"
    )

    mfcc = librosa.feature.mfcc(
        y=audio,
        sr=sr,
        n_mfcc=40
    )

    fig, ax = plt.subplots(
        figsize=(12, 5)
    )

    img = librosa.display.specshow(
        mfcc,
        x_axis="time",
        ax=ax
    )

    ax.set_title(
        "40 Mel-Frequency Cepstral Coefficients"
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

    st.markdown("---")

    md('<div class="section-label">MODEL INPUT</div>')

    st.markdown(
        "### 🧠 Extracted Feature Tensor"
    )

    features = extract_mfcc(
        temp_path
    )


    if features is not None:

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Feature Shape",
                str(features.shape)
            )

        with col2:

            st.metric(
                "Feature Channels",
                "4"
            )


        md(
            """
            <div class="info-card">
                <h3>Feature Channels</h3>
                <p>
                    The model receives four complementary acoustic
                    representations:
                </p>
                <ul>
                    <li><strong>MFCC</strong> — captures spectral characteristics</li>
                    <li><strong>Delta</strong> — captures first-order changes</li>
                    <li><strong>Delta-Delta</strong> — captures second-order changes</li>
                    <li><strong>Log-Mel</strong> — represents energy across Mel frequencies</li>
                </ul>
            </div>
            """
        )


        st.code(
            f"Model Input Shape: {features.shape}",
            language="text"
        )


    # ========================================================
    # NAVIGATION
    # ========================================================

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:

        st.page_link(
            "pages/prediction.py",
            label="← Emotion Prediction",
            use_container_width=True
        )

    with col2:

        st.page_link(
            "pages/model_info.py",
            label="Model & Dataset →",
            use_container_width=True
        )


# ============================================================
# ERROR HANDLING
# ============================================================

except Exception as e:

    st.error(
        "Something went wrong while analyzing the audio."
    )

    st.exception(e)


# ============================================================
# CLEANUP
# ============================================================

finally:

    if temp_path is not None:

        cleanup_audio(
            temp_path
        )


# ============================================================
# DISCLAIMER
# ============================================================

st.markdown("---")

st.warning(
    """
    **Disclaimer:** These visualizations describe acoustic
    characteristics of the supplied audio. They should not be
    interpreted as a definitive assessment of a person's
    emotional or psychological state.
    """
)


# ============================================================
# FOOTER
# ============================================================

render_footer()