# 🩺 MediPredict — Disease Prediction System

A machine learning-based diabetes risk prediction system built as part of the **CodeAlpha Machine Learning Internship**.

MediPredict analyzes a user's medical measurements and predicts the likelihood of diabetes using a trained **Random Forest Classifier**.

The project includes data preprocessing, multiple machine learning models, model evaluation, feature importance analysis, and an interactive Streamlit web application.

---

## 📌 Project Overview

Diabetes is a common chronic disease that can be influenced by factors such as glucose level, blood pressure, BMI, age, insulin level, and other medical indicators.

This project uses machine learning to analyze these features and provide a predicted diabetes risk.

### Main objectives

- Perform exploratory data analysis
- Preprocess medical data
- Train multiple machine learning models
- Compare model performance
- Select the best-performing model
- Build an interactive prediction interface
- Visualize model performance
- Deploy the application using Streamlit

---

## 📊 Dataset

The project uses the **Pima Indians Diabetes Dataset**.

### Dataset characteristics

| Property | Value |
|---|---:|
| Total Records | 768 |
| Input Features | 8 |
| Target Classes | 2 |
| Target | Outcome |
| Class 0 | No Diabetes |
| Class 1 | Diabetes |

### Features

| Feature | Description |
|---|---|
| Pregnancies | Number of pregnancies |
| Glucose | Plasma glucose concentration |
| BloodPressure | Diastolic blood pressure |
| SkinThickness | Triceps skin fold thickness |
| Insulin | 2-Hour serum insulin |
| BMI | Body Mass Index |
| DiabetesPedigreeFunction | Diabetes pedigree function |
| Age | Age in years |

---

## 🔄 Machine Learning Workflow

```text
Dataset
   ↓
Data Exploration
   ↓
Data Cleaning
   ↓
Missing/Invalid Value Handling
   ↓
Feature Scaling
   ↓
Train/Test Split
   ↓
Model Training
   ↓
Model Comparison
   ↓
Best Model Selection
   ↓
Evaluation
   ↓
Streamlit Prediction App