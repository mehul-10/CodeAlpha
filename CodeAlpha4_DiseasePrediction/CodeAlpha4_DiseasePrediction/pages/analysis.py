import os

import pandas as pd
import streamlit as st

from utils.styles import inject_css, render_footer


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Model Analysis | MediPredict",
    page_icon="📊",
    layout="wide"
)

inject_css()


# ============================================================
# HEADER
# ============================================================

st.markdown(
    """
    <div class="page-header">
        <div class="eyebrow">MODEL PERFORMANCE</div>
        <h1>Model Analysis</h1>
        <p>
            Explore how the machine learning models performed and
            understand the factors influencing predictions.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# MODEL COMPARISON
# ============================================================

st.markdown("### 📊 Model Comparison")

comparison_path = "models/model_comparison.csv"

if os.path.exists(comparison_path):

    comparison = pd.read_csv(comparison_path)

    # Format display
    display_df = comparison.copy()

    numeric_columns = [
        "Accuracy",
        "Precision",
        "Recall",
        "F1 Score",
        "ROC-AUC"
    ]

    for column in numeric_columns:
        if column in display_df.columns:
            display_df[column] = display_df[column].round(4)

    st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True
    )

else:
    st.warning("Model comparison data not found.")


# ============================================================
# BEST MODEL
# ============================================================

st.markdown("### 🏆 Selected Model")

st.markdown(
    """
    <div class="info-card">
        <h3>Random Forest Classifier</h3>
        <p>
            The Random Forest model was selected because it achieved
            the strongest overall F1 score among the evaluated models.
            It also provided the highest ROC-AUC score in the comparison.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# PERFORMANCE SUMMARY
# ============================================================

st.markdown("### 📈 Performance Summary")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Accuracy", "73.38%")

with col2:
    st.metric("Precision", "59.70%")

with col3:
    st.metric("Recall", "74.07%")

with col4:
    st.metric("ROC-AUC", "82.41%")


# ============================================================
# CONFUSION MATRIX
# ============================================================

st.markdown("### 🔲 Confusion Matrix")

confusion_path = "models/evaluation/confusion_matrix.png"

if os.path.exists(confusion_path):
    st.image(
        confusion_path,
        caption="Random Forest Confusion Matrix",
        width="stretch"
    )

    st.markdown(
        """
        **Interpretation**

        - **73** patients were correctly predicted as having no diabetes.
        - **40** patients were correctly predicted as having diabetes.
        - **27** patients without diabetes were incorrectly classified.
        - **14** diabetic patients were incorrectly classified as no diabetes.
        """,
    )

else:
    st.info("Confusion matrix image not found.")


# ============================================================
# ROC CURVE
# ============================================================

st.markdown("### 📉 ROC Curve")

roc_path = "models/evaluation/roc_curve.png"

if os.path.exists(roc_path):
    st.image(
        roc_path,
        caption="ROC Curve",
        width="stretch"
    )
else:
    st.info("ROC curve image not found.")


# ============================================================
# FEATURE IMPORTANCE
# ============================================================

st.markdown("### 🧠 Feature Importance")

feature_path = "models/evaluation/feature_importance.png"

if os.path.exists(feature_path):
    st.image(
        feature_path,
        caption="Random Forest Feature Importance",
        width="stretch"
    )
else:
    st.info("Feature importance image not found.")


# ============================================================
# FEATURE TABLE
# ============================================================

csv_path = "models/evaluation/feature_importance.csv"

if os.path.exists(csv_path):

    st.markdown("### Feature Importance Values")

    feature_df = pd.read_csv(csv_path)

    st.dataframe(
        feature_df.round(4),
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# DISCLAIMER
# ============================================================

st.markdown(
    """
    <div class="disclaimer">
        <strong>⚠️ Educational Project</strong><br>
        These results are intended for demonstrating machine learning
        concepts only. The model should not be used as a medical
        diagnostic system or as a substitute for professional medical advice.
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# FOOTER
# ============================================================

render_footer()