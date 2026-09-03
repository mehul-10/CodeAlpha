import librosa
import numpy as np


# ============================================================
# PAD / CROP
# ============================================================

def pad_or_crop(feature, max_pad_len=174):
    """
    Make sure every feature has exactly 174 time frames.
    """

    if feature.shape[1] < max_pad_len:

        pad_width = max_pad_len - feature.shape[1]

        feature = np.pad(
            feature,
            ((0, 0), (0, pad_width)),
            mode="constant"
        )

    else:

        feature = feature[:, :max_pad_len]

    return feature


# ============================================================
# FEATURE EXTRACTION
# ============================================================

def extract_mfcc(
    file_path,
    n_mfcc=40,
    max_pad_len=174
):
    """
    Extract the same four feature channels used during training:

    1. MFCC
    2. Delta MFCC
    3. Delta-Delta MFCC
    4. Log-Mel Spectrogram

    Returns:
        numpy array with shape (40, 174, 4)
    """

    try:

        # ----------------------------------------------------
        # Load audio
        # ----------------------------------------------------

        audio, sample_rate = librosa.load(
            file_path,
            sr=22050,
            duration=3
        )

        # ----------------------------------------------------
        # MFCC
        # ----------------------------------------------------

        mfcc = librosa.feature.mfcc(
            y=audio,
            sr=sample_rate,
            n_mfcc=n_mfcc
        )

        mfcc = pad_or_crop(
            mfcc,
            max_pad_len
        )

        # ----------------------------------------------------
        # Delta
        # ----------------------------------------------------

        delta = librosa.feature.delta(
            mfcc
        )

        delta = pad_or_crop(
            delta,
            max_pad_len
        )

        # ----------------------------------------------------
        # Delta-Delta
        # ----------------------------------------------------

        delta2 = librosa.feature.delta(
            mfcc,
            order=2
        )

        delta2 = pad_or_crop(
            delta2,
            max_pad_len
        )

        # ----------------------------------------------------
        # Mel Spectrogram
        # ----------------------------------------------------

        mel = librosa.feature.melspectrogram(
            y=audio,
            sr=sample_rate,
            n_mels=40,
            n_fft=2048,
            hop_length=512
        )

        mel_db = librosa.power_to_db(
            mel,
            ref=np.max
        )

        mel_db = pad_or_crop(
            mel_db,
            max_pad_len
        )

        # ----------------------------------------------------
        # Stack features
        # ----------------------------------------------------

        features = np.stack(
            [
                mfcc,
                delta,
                delta2,
                mel_db
            ],
            axis=-1
        )

        return features.astype(
            np.float32
        )

    except Exception as e:

        print(
            f"Error processing {file_path}: {e}"
        )

        return None