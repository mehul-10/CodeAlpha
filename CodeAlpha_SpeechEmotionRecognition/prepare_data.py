import os
import numpy as np

from audio_features import extract_mfcc


# ============================================================
# CONFIGURATION
# ============================================================

DATASET_PATH = "dataset/ravdess"
OUTPUT_PATH = "dataset/processed_data.npz"


# RAVDESS emotion codes
EMOTIONS = {
    "01": "neutral",
    "02": "calm",
    "03": "happy",
    "04": "sad",
    "05": "angry",
    "06": "fearful",
    "07": "disgust",
    "08": "surprised"
}


# ============================================================
# STORAGE
# ============================================================

features = []
labels = []
actors = []


print("=" * 60)
print("RAVDESS DATA PREPARATION")
print("=" * 60)


# ============================================================
# PROCESS ACTORS
# ============================================================

for actor in sorted(os.listdir(DATASET_PATH)):

    actor_path = os.path.join(DATASET_PATH, actor)

    if not os.path.isdir(actor_path):
        continue

    print(f"Processing {actor}...")

    # Extract actor number
    actor_id = int(actor.split("_")[1])

    for filename in sorted(os.listdir(actor_path)):

        if not filename.lower().endswith(".wav"):
            continue

        # Example:
        # 03-01-06-01-02-01-12.wav

        parts = filename.split("-")

        if len(parts) != 7:
            continue

        emotion_code = parts[2]

        if emotion_code not in EMOTIONS:
            continue

        file_path = os.path.join(
            actor_path,
            filename
        )

        mfcc = extract_mfcc(file_path)

        if mfcc is not None:

            features.append(mfcc)

            # Store emotion NAME
            labels.append(
                EMOTIONS[emotion_code]
            )

            # Store actor ID
            actors.append(actor_id)


# ============================================================
# CONVERT TO NUMPY
# ============================================================

X = np.array(features)
y = np.array(labels)
actor_ids = np.array(actors)


# ============================================================
# DISPLAY INFORMATION
# ============================================================

print("\n" + "=" * 60)
print("DATA PREPARATION COMPLETE")
print("=" * 60)

print(f"Features shape: {X.shape}")
print(f"Labels shape:   {y.shape}")
print(f"Actors shape:   {actor_ids.shape}")


# ============================================================
# EMOTION DISTRIBUTION
# ============================================================

print("\nEmotion distribution:")

for emotion in EMOTIONS.values():

    count = np.sum(y == emotion)

    print(f"{emotion:10s}: {count}")


# ============================================================
# ACTOR DISTRIBUTION
# ============================================================

print("\nActor distribution:")

for actor_id in range(1, 25):

    count = np.sum(actor_ids == actor_id)

    print(
        f"Actor {actor_id:02d}: {count}"
    )


# ============================================================
# SAVE DATASET
# ============================================================

np.savez_compressed(
    OUTPUT_PATH,
    X=X,
    y=y,
    actors=actor_ids
)

print("\nProcessed dataset saved to:")

print(OUTPUT_PATH)