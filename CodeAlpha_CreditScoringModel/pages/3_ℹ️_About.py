import streamlit as st

from utils import configure_page, render_footer

configure_page("About", page_icon="ℹ️")

st.markdown('<div class="main-title">ℹ️ About This Model</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Performance, dataset, and important disclaimers</div>',
    unsafe_allow_html=True,
)
st.divider()

st.markdown('<div class="section-title">Model Performance</div>', unsafe_allow_html=True)
st.write("This application uses a tuned Random Forest classifier trained on the German Credit dataset.")

metric_col1, metric_col2, metric_col3, metric_col4, metric_col5 = st.columns(5)
metrics = [
    ("Accuracy", "73.0%"),
    ("Precision", "85.25%"),
    ("Macro F1", "70.13%"),
    ("ROC-AUC", "78.71%"),
    ("Bad Credit Recall", "70.0%"),
]
for col, (label, value) in zip(
    [metric_col1, metric_col2, metric_col3, metric_col4, metric_col5], metrics
):
    with col:
        st.markdown(
            f"""
            <div class="probability-card">
                <div class="probability-label">{label}</div>
                <div class="probability-value" style="font-size:22px;">{value}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.divider()

st.markdown('<div class="section-title">About the Dataset</div>', unsafe_allow_html=True)
st.write(
    "The model was trained on the **German Credit dataset**, a widely used "
    "benchmark for credit risk classification. It contains 1,000 loan "
    "applicants described by 20 financial, personal, and demographic "
    "attributes, each labeled as a good or bad credit risk based on "
    "historical outcomes."
)

st.markdown('<div class="section-title">Methodology</div>', unsafe_allow_html=True)
st.write(
    "The model uses financial, credit history, employment, demographic, "
    "and residential attributes to estimate credit risk. It outputs both "
    "a class prediction (good/bad) and a probability for each class, "
    "shown together on the Predict page."
)

st.divider()

st.markdown('<div class="section-title">Disclaimer</div>', unsafe_allow_html=True)
st.markdown(
    """
    <div style="
        color: black;
        background-color: #fff3cd;
        padding: 12px 16px;
        border-radius: 8px;
        border: 1px solid #ffe69c;
        font-size: 14px;
        line-height: 1.5;
    ">
        ⚠️ This application is an educational machine learning project and
        should <strong>not</strong> be used as the sole basis for real-world
        lending decisions. Credit decisions in practice are subject to
        regulatory, fairness, and legal requirements that this demo does not
        implement.
    </div>
    """,
    unsafe_allow_html=True
)

render_footer()