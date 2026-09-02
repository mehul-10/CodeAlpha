import os
import tempfile

import pandas as pd
import streamlit as st

from audio_features import extract_mfcc
from utils.audio_utils import (
    save_audio_file,
    get_audio_info,
    cleanup_audio,
)
from utils.model_utils import (
    predict_emotion,
    EMOTION_EMOJIS,
)
from utils.styles import render_footer


# ============================================================
# PAGE HEADER
# ============================================================

st.markdown(
    '<div class="section-label">AI PREDICTION</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<h1 class="page-title">Emotion Prediction</h1>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <p class="page-subtitle">
        Upload or record your speech and let the deep learning
        model estimate the emotional characteristics of the audio.
    </p>
    """,
    unsafe_allow_html=True
)


# ============================================================
# AUDIO INPUT
# ============================================================

st.markdown(
    '<div class="section-label">AUDIO INPUT</div>',
    unsafe_allow_html=True
)

input_method = st.radio(
    "Choose how you want to provide audio",
    [
        "Upload Audio",
        "Record Audio"
    ],
    horizontal=True
)


audio_bytes = None
audio_name = None


# ============================================================
# UPLOAD AUDIO
# ============================================================

if input_method == "Upload Audio":

    uploaded_file = st.file_uploader(
        "Upload a WAV audio file",
        type=["wav"],
        help="For best results, use a clear speech recording."
    )

    if uploaded_file is not None:

        audio_bytes = uploaded_file.getvalue()
        audio_name = uploaded_file.name

        st.session_state["analysis_audio_bytes"] = audio_bytes
        st.session_state["analysis_audio_name"] = audio_name

        st.audio(
            audio_bytes,
            format="audio/wav"
        )


# ============================================================
# RECORD AUDIO
# ============================================================

else:

    st.markdown(
        """
        <div class="info-card">
            <h3>🎙️ Record your voice</h3>
            <p>
                Click the microphone button below and record a
                short speech sample.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    recorded_audio = st.audio_input(
        "Record your speech"
    )

    if recorded_audio is not None:

        audio_bytes = recorded_audio.getvalue()
        audio_name = "recorded_audio.wav"

        st.session_state["analysis_audio_bytes"] = audio_bytes
        st.session_state["analysis_audio_name"] = audio_name

        st.audio(
            audio_bytes,
            format="audio/wav"
        )


# ============================================================
# ANALYZE BUTTON
# ============================================================

if audio_bytes is not None:

    st.markdown("")

    analyze_button = st.button(
        "🎯 Analyze Emotion",
        type="primary",
        use_container_width=True
    )

    if analyze_button:

        temp_path = None

        try:

            # ====================================================
            # SAVE AUDIO TEMPORARILY
            # ====================================================

            with tempfile.NamedTemporaryFile(
                delete=False,
                suffix=".wav"
            ) as temp_file:

                temp_file.write(audio_bytes)
                temp_path = temp_file.name


            # ====================================================
            # AUDIO INFORMATION
            # ====================================================

            audio_info = get_audio_info(
                temp_path
            )

            duration = audio_info["duration"]
            sample_rate = audio_info["sample_rate"]


            # ====================================================
            # FEATURE EXTRACTION
            # ====================================================

            with st.spinner(
                "Extracting audio features..."
            ):

                features = extract_mfcc(
                    temp_path
                )


            if features is None:

                st.error(
                    "Unable to extract features from this audio."
                )

                st.stop()


            # ====================================================
            # CHECK FEATURE SHAPE
            # ====================================================

            if features.shape != (40, 174, 4):

                st.error(
                    f"Unexpected feature shape: "
                    f"{features.shape}. "
                    f"Expected (40, 174, 4)."
                )

                st.stop()


            # ====================================================
            # EMOTION PREDICTION
            # ====================================================

            with st.spinner(
                "Analyzing emotional characteristics..."
            ):

                (
                    emotion,
                    confidence,
                    probabilities
                ) = predict_emotion(
                    features
                )


            # ====================================================
            # STORE RESULTS IN SESSION
            # ====================================================

            st.session_state["predicted_emotion"] = emotion
            st.session_state["prediction_confidence"] = confidence
            st.session_state["prediction_probabilities"] = probabilities
            st.session_state["prediction_duration"] = duration
            st.session_state["prediction_sample_rate"] = sample_rate


            # ====================================================
            # RESULT HEADER
            # ====================================================

            st.markdown("---")

            st.markdown(
                '<div class="section-label">PREDICTION RESULT</div>',
                unsafe_allow_html=True
            )


            # ====================================================
            # EMOTION RESULT
            # ====================================================

            emoji = EMOTION_EMOJIS.get(
                emotion.lower(),
                "🎭"
            )

            confidence_percentage = (
                confidence * 100
            )


            st.markdown(
                f"""
                <div class="prediction-card">

                    <div class="prediction-emoji">
                        {emoji}
                    </div>

                    <div class="prediction-label">
                        DETECTED EMOTION
                    </div>

                    <div class="prediction-emotion">
                        {emotion.upper()}
                    </div>

                    <div class="prediction-confidence">
                        Confidence: {confidence_percentage:.2f}%
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )


            # ====================================================
            # AUDIO METRICS
            # ====================================================

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
                    "Feature Shape",
                    "40 × 174 × 4"
                )


            # ====================================================
            # PROBABILITY BAR CHART
            # ====================================================

            st.markdown("---")

            st.markdown(
                '<div class="section-label">PROBABILITY DISTRIBUTION</div>',
                unsafe_allow_html=True
            )

            st.markdown(
                "### Emotion Probabilities"
            )

            labels = [
                "angry",
                "calm",
                "disgust",
                "fearful",
                "happy",
                "neutral",
                "sad",
                "surprised",
            ]


            probability_values = (
                probabilities * 100
            )


            probability_df = pd.DataFrame(
                {
                    "Emotion": labels,
                    "Probability": probability_values,
                }
            )

            probability_df = probability_df.sort_values(
                "Probability",
                ascending=False
            )

            chart_df = probability_df.set_index(
                "Emotion"
            )


            st.bar_chart(
                chart_df[
                    "Probability"
                ],
                use_container_width=True
            )


            # ====================================================
            # EXACT PROBABILITIES
            # ====================================================

            with st.expander(
                "View exact probabilities"
            ):

                display_df = probability_df.copy()

                display_df["Probability"] = (
                    display_df["Probability"]
                    .map(
                        lambda x: f"{x:.2f}%"
                    )
                )

                st.dataframe(
                    display_df,
                    use_container_width=True,
                    hide_index=True
                )


            # ====================================================
            # AUDIO ANALYSIS BUTTON
            # ====================================================

            st.markdown("---")

            st.markdown(
                """
                <div class="info-card">
                    <h3>📊 Explore your audio</h3>
                    <p>
                        View the waveform, Mel spectrogram and MFCC
                        representation of this recording.
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )

            if st.button(
                "Open Audio Analysis →",
                use_container_width=True
            ):

                st.switch_page(
                    "pages/analysis.py"
                )


        except Exception as e:

            st.error(
                "Something went wrong while analyzing the audio."
            )

            st.exception(e)


        finally:

            if temp_path is not None:

                cleanup_audio(
                    temp_path
                )


# ============================================================
# NO AUDIO SELECTED
# ============================================================

else:

    st.info(
        "🎙️ Upload a WAV file or record your voice "
        "to begin emotion analysis."
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
    person's emotional state.
    """
)


# ============================================================
# FOOTER
# ============================================================

render_footer()