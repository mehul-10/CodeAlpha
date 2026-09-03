import pandas as pd
import streamlit as st

from utils import (
    configure_page,
    render_footer,
    load_model,
    FEATURE_COLUMNS,
    CHECKING_ACCOUNT_MAP,
    SAVINGS_ACCOUNT_MAP,
    PURPOSE_MAP,
    CREDIT_HISTORY_MAP,
    OTHER_INSTALLMENT_MAP,
    EMPLOYMENT_MAP,
    PROPERTY_MAP,
    HOUSING_MAP,
    PERSONAL_STATUS_MAP,
    OTHER_DEBTORS_MAP,
    JOB_MAP,
    TELEPHONE_MAP,
    FOREIGN_WORKER_MAP,
)

configure_page("Predict", page_icon="🔮")

st.markdown('<div class="main-title">🔮 Predict Credit Risk</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Fill in the applicant\'s details below</div>',
    unsafe_allow_html=True,
)
st.divider()

# Load model up front and stop cleanly if it isn't available, instead of
# crashing deep inside the prediction block after the user has already
# filled out the whole form.
model, error = load_model()
if error:
    st.error(f"🚫 {error}")
    st.stop()

st.markdown('<div class="section-title">Applicant Information</div>', unsafe_allow_html=True)

with st.form("credit_form"):

    # ========================================================
    # FINANCIAL INFORMATION
    # ========================================================
    st.markdown('<div class="subsection-title">Financial Information</div>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)

    with col1:
        checking_account_label = st.selectbox("Checking Account", list(CHECKING_ACCOUNT_MAP.keys()))
        checking_account = CHECKING_ACCOUNT_MAP[checking_account_label]

    with col2:
        savings_account_label = st.selectbox("Savings Account", list(SAVINGS_ACCOUNT_MAP.keys()))
        savings_account = SAVINGS_ACCOUNT_MAP[savings_account_label]

    with col3:
        credit_amount = st.number_input(
            "Credit Amount", min_value=250, max_value=20000, value=2500, step=100
        )

    # ========================================================
    # LOAN INFORMATION
    # ========================================================
    st.markdown('<div class="subsection-title">Loan Information</div>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)

    with col1:
        duration_months = st.number_input(
            "Loan Duration (months)", min_value=4, max_value=72, value=24, step=1
        )

    with col2:
        installment_rate = st.selectbox(
            "Installment Rate",
            [1, 2, 3, 4],
            format_func=lambda x: {
                1: "1 - Very low", 2: "2 - Low", 3: "3 - Moderate", 4: "4 - High"
            }[x],
        )

    with col3:
        purpose_label = st.selectbox("Loan Purpose", list(PURPOSE_MAP.keys()))
        purpose = PURPOSE_MAP[purpose_label]

    # ========================================================
    # CREDIT HISTORY
    # ========================================================
    st.markdown('<div class="subsection-title">Credit History</div>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)

    with col1:
        credit_history_label = st.selectbox("Credit History", list(CREDIT_HISTORY_MAP.keys()))
        credit_history = CREDIT_HISTORY_MAP[credit_history_label]

    with col2:
        existing_credits = st.selectbox("Existing Credits", [1, 2, 3, 4])

    with col3:
        other_installment_label = st.selectbox("Other Installment Plans", list(OTHER_INSTALLMENT_MAP.keys()))
        other_installment_plans = OTHER_INSTALLMENT_MAP[other_installment_label]

    # ========================================================
    # PERSONAL INFORMATION
    # ========================================================
    st.markdown('<div class="subsection-title">Personal Information</div>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input("Age", min_value=18, max_value=80, value=30)

    with col2:
        employment_label = st.selectbox("Employment Duration", list(EMPLOYMENT_MAP.keys()))
        employment_duration = EMPLOYMENT_MAP[employment_label]

    with col3:
        dependents = st.selectbox("Number of Dependents", [1, 2])

    # ========================================================
    # RESIDENCE & ASSETS
    # ========================================================
    st.markdown('<div class="subsection-title">Residence & Assets</div>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)

    with col1:
        residence_since = st.selectbox("Years at Current Residence", [1, 2, 3, 4])

    with col2:
        property_label = st.selectbox("Property", list(PROPERTY_MAP.keys()))
        property_type = PROPERTY_MAP[property_label]

    with col3:
        housing_label = st.selectbox("Housing", list(HOUSING_MAP.keys()))
        housing = HOUSING_MAP[housing_label]

    # ========================================================
    # OTHER DETAILS
    # ========================================================
    st.markdown('<div class="subsection-title">Other Details</div>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)

    with col1:
        personal_status_label = st.selectbox("Personal Status", list(PERSONAL_STATUS_MAP.keys()))
        personal_status_sex = PERSONAL_STATUS_MAP[personal_status_label]

    with col2:
        other_debtors_label = st.selectbox("Other Debtors", list(OTHER_DEBTORS_MAP.keys()))
        other_debtors = OTHER_DEBTORS_MAP[other_debtors_label]

    with col3:
        job_label = st.selectbox("Job", list(JOB_MAP.keys()))
        job = JOB_MAP[job_label]

    col1, col2 = st.columns(2)

    with col1:
        telephone_label = st.selectbox("Telephone", list(TELEPHONE_MAP.keys()))
        telephone = TELEPHONE_MAP[telephone_label]

    with col2:
        foreign_worker_label = st.selectbox("Foreign Worker", list(FOREIGN_WORKER_MAP.keys()))
        foreign_worker = FOREIGN_WORKER_MAP[foreign_worker_label]

    st.markdown("")
    submitted = st.form_submit_button("Assess Credit Risk", use_container_width=True)


# ============================================================
# PREDICTION
# ============================================================
if submitted:

    input_data = pd.DataFrame(
        [[
            checking_account, duration_months, credit_history, purpose, credit_amount,
            savings_account, employment_duration, installment_rate, personal_status_sex,
            other_debtors, residence_since, property_type, age, other_installment_plans,
            housing, existing_credits, job, dependents, telephone, foreign_worker,
        ]],
        columns=FEATURE_COLUMNS,
    )

    try:
        prediction = model.predict(input_data)[0]
        probabilities = model.predict_proba(input_data)[0]
    except Exception as exc:  # noqa: BLE001 - surface any inference error clearly
        st.error(
            f"🚫 The model could not process this input: {exc}\n\n"
            "This usually means the input columns don't match what the "
            "model was trained on."
        )
        st.stop()

    bad_probability = probabilities[0]
    good_probability = probabilities[1]
    confidence = max(good_probability, bad_probability)

    st.divider()
    st.markdown('<div class="section-title">Credit Risk Assessment</div>', unsafe_allow_html=True)

    if prediction == 1:
        st.markdown(
            """
            <div class="result-card">
                <div class="result-icon">✓</div>
                <div class="result-title">Good Credit Risk</div>
                <div class="result-description">
                    The model predicts a relatively favorable credit profile for this applicant.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            """
            <div class="result-card">
                <div class="result-icon">!</div>
                <div class="result-title">Bad Credit Risk</div>
                <div class="result-description">
                    The model identifies a relatively higher credit risk for this applicant.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Probability cards
    st.markdown("")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            f"""
            <div class="probability-card">
                <div class="probability-label">Good Credit Probability</div>
                <div class="probability-value">{good_probability * 100:.2f}%</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            f"""
            <div class="probability-card">
                <div class="probability-label">Bad Credit Probability</div>
                <div class="probability-value">{bad_probability * 100:.2f}%</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            f"""
            <div class="probability-card">
                <div class="probability-label">Model Confidence</div>
                <div class="probability-value">{confidence * 100:.2f}%</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Probability chart
    st.markdown("")
    st.markdown('<div class="subsection-title">Prediction Probability</div>', unsafe_allow_html=True)

    probability_df = pd.DataFrame(
        {
            "Credit Risk": ["Good Credit", "Bad Credit"],
            "Probability": [good_probability, bad_probability],
        }
    )
    st.bar_chart(probability_df.set_index("Credit Risk"), height=280)

    # Applicant summary
    st.markdown('<div class="subsection-title">Applicant Summary</div>', unsafe_allow_html=True)
    st.markdown('<div class="summary-card">', unsafe_allow_html=True)

    summary_col1, summary_col2, summary_col3 = st.columns(3)

    with summary_col1:
        st.write(f"**Age**  \n{age}")
        st.write(f"**Credit Amount**  \n{credit_amount}")

    with summary_col2:
        st.write(f"**Loan Duration**  \n{duration_months} months")
        st.write(f"**Loan Purpose**  \n{purpose_label}")

    with summary_col3:
        st.write(f"**Employment**  \n{employment_label}")
        st.write(f"**Housing**  \n{housing_label}")

    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("")
st.caption(
    "This application is an educational machine learning project and should "
    "not be used as the sole basis for real-world lending decisions."
)

render_footer()