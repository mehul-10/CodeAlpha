import os
import tempfile

import librosa
import numpy as np


# ============================================================
# SAVE UPLOADED / RECORDED AUDIO
# ============================================================

def save_audio_file(uploaded_file):

    suffix = ".wav"

    if uploaded_file.name.lower().endswith(".mp3"):
        suffix = ".mp3"

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=suffix
    ) as temp_file:

        temp_file.write(
            uploaded_file.getbuffer()
        )

        return temp_file.name


# ============================================================
# AUDIO INFORMATION
# ============================================================

def get_audio_info(file_path):

    audio, sample_rate = librosa.load(
        file_path,
        sr=None
    )

    duration = (
        len(audio) / sample_rate
    )

    return {
        "audio": audio,
        "sample_rate": sample_rate,
        "duration": duration
    }


# ============================================================
# CLEAN TEMP FILE
# ============================================================

def cleanup_audio(file_path):

    try:

        if os.path.exists(file_path):
            os.remove(file_path)

    except Exception:
        pass