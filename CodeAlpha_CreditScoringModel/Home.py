import streamlit as st
from utils import configure_page, render_footer, load_model

configure_page("Home")

st.markdown('<div class="main-title">💳 Credit Risk Predictor</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Machine learning powered creditworthiness assessment</div>',
    unsafe_allow_html=True,
)
st.divider()

# Quietly check the model status here so the person finds out on the
# landing page rather than after filling out the whole form.
model, error = load_model()
if error:
    st.warning(
        f"⚠️ {error}\n\nThe **Predict** page will not work until this is fixed, "
        "but you can still browse the other pages."
    )
else:
    st.success("✅ Model loaded and ready.")

st.markdown('<div class="section-title">What this app does</div>', unsafe_allow_html=True)
st.write(
    "This app estimates whether a loan applicant is likely to be a **good** "
    "or **bad** credit risk, using a model trained on the German Credit "
    "dataset. Use the pages in the sidebar to navigate:"
)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <div class="info-card">
            <div class="subsection-title">🔮 Predict</div>
            Fill in an applicant's details and get an instant
            good/bad credit risk assessment with probabilities.
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.page_link("pages/1_🔮_Predict.py", label="Go to Predict", icon="🔮")

with col2:
    st.markdown(
        """
        <div class="info-card">
            <div class="subsection-title">📊 Model Insights</div>
            See which features the model relies on most and what
            each input field actually means.
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.page_link("pages/2_📊_Model_Insights.py", label="Go to Model Insights", icon="📊")

with col3:
    st.markdown(
        """
        <div class="info-card">
            <div class="subsection-title">ℹ️ About</div>
            Model performance metrics, the dataset it was trained
            on, and important disclaimers.
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.page_link("pages/3_ℹ️_About.py", label="Go to About", icon="ℹ️")

render_footer()