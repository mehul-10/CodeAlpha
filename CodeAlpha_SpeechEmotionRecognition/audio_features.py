import librosa
import numpy as np


def extract_mfcc(
    file_path,
    n_mfcc=40,
    max_pad_len=174
):
    """
    Extract MFCC + Delta + Delta-Delta features.

    Output shape:
        (40, 174, 3)

    Channels:
        0 -> MFCC
        1 -> Delta
        2 -> Delta-Delta
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


        # ----------------------------------------------------
        # Delta
        # ----------------------------------------------------

        delta = librosa.feature.delta(
            mfcc
        )


        # ----------------------------------------------------
        # Delta-Delta
        # ----------------------------------------------------

        delta2 = librosa.feature.delta(
            mfcc,
            order=2
        )


        # ----------------------------------------------------
        # Pad / crop
        # ----------------------------------------------------

        def pad_or_crop(feature):

            if feature.shape[1] < max_pad_len:

                pad_width = (
                    max_pad_len - feature.shape[1]
                )

                feature = np.pad(
                    feature,
                    pad_width=(
                        (0, 0),
                        (0, pad_width)
                    ),
                    mode="constant"
                )

            else:

                feature = feature[
                    :, :max_pad_len
                ]

            return feature


        mfcc = pad_or_crop(mfcc)
        delta = pad_or_crop(delta)
        delta2 = pad_or_crop(delta2)


        # ----------------------------------------------------
        # Stack as channels
        # ----------------------------------------------------

        features = np.stack(
            [
                mfcc,
                delta,
                delta2
            ],
            axis=-1
        )


        return features


    except Exception as e:

        print(
            f"Error processing {file_path}: {e}"
        )

        return None