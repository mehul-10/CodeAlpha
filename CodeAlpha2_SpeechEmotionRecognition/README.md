# 🎙️ Speech Emotion Recognition

A deep learning-based Speech Emotion Recognition (SER) application that analyzes human speech and predicts the emotional state expressed in an audio recording.

The project uses audio feature extraction with MFCCs, Delta, Delta-Delta and Log-Mel Spectrogram features, followed by a hybrid CNN + Bidirectional LSTM architecture.

The complete application is built and deployed using Streamlit.

---

## 🚀 Live Demo

🔗 **Live App:**  
[https://YOUR-STREAMLIT-APP-LINK.streamlit.app/](https://speech-emotion-recognition10.streamlit.app/)

🔗 **GitHub Repository:**  
[https://github.com/mehul-10/CodeAlpha_SpeechEmotionRecognition](https://github.com/mehul-10/CodeAlpha/tree/main/CodeAlpha_SpeechEmotionRecognition)

---

## 📌 Features

- 🎤 Upload an audio file for emotion prediction
- 🎙️ Record audio directly from the browser
- 🧠 CNN + Bidirectional LSTM deep learning model
- 🎵 MFCC feature extraction
- 📈 Delta and Delta-Delta audio features
- 🔊 Log-Mel Spectrogram analysis
- 📊 Emotion probability visualization
- 🌊 Audio waveform visualization
- 🎼 Mel Spectrogram visualization
- 📉 MFCC visualization
- 📋 Model and dataset information
- 📱 Responsive and modern Streamlit interface

---

## 🎭 Supported Emotions

The model recognizes 8 different emotions:

| Emotion | Emoji |
|---------|-------|
| Angry | 😠 |
| Calm | 😌 |
| Disgust | 🤢 |
| Fearful | 😨 |
| Happy | 😊 |
| Neutral | 😐 |
| Sad | 😢 |
| Surprised | 😲 |

---

## 🧠 Model Architecture

The project uses a hybrid **CNN + Bidirectional LSTM (BiLSTM)** architecture.

```text
Input Audio
     │
     ▼
Audio Preprocessing
     │
     ▼
Feature Extraction
     │
     ├── MFCC
     ├── Delta
     ├── Delta-Delta
     └── Log-Mel Spectrogram
     │
     ▼
Feature Tensor
40 × 174 × 4
     │
     ▼
CNN Block 1
Conv2D → BatchNorm → MaxPooling → Dropout
     │
     ▼
CNN Block 2
Conv2D → BatchNorm → MaxPooling → Dropout
     │
     ▼
CNN Block 3
Conv2D → BatchNorm → MaxPooling → Dropout
     │
     ▼
Reshape
     │
     ▼
Bidirectional LSTM
     │
     ▼
Dense Layer
     │
     ▼
Softmax
     │
     ▼
Emotion Prediction
