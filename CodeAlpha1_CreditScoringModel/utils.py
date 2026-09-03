"""
Shared utilities for the Credit Risk Predictor app.

Keeping mappings, styling, and the model loader in one place avoids the
biggest bug risk in a multi-page Streamlit app: the same dropdown label
being encoded differently on two different pages.
"""

import os
import joblib
import streamlit as st

# ============================================================
# PATHS
# ============================================================

MODEL_PATH = os.path.join(os.path.dirname(__file__), "models", "credit_model.pkl")

FEATURE_COLUMNS = [
    "checking_account",
    "duration_months",
    "credit_history",
    "purpose",
    "credit_amount",
    "savings_account",
    "employment_duration",
    "installment_rate",
    "personal_status_sex",
    "other_debtors",
    "residence_since",
    "property",
    "age",
    "other_installment_plans",
    "housing",
    "existing_credits",
    "job",
    "dependents",
    "telephone",
    "foreign_worker",
]

FEATURE_DESCRIPTIONS = {
    "checking_account": "Status of the applicant's existing checking account.",
    "duration_months": "Length of the requested loan, in months.",
    "credit_history": "How the applicant has handled past credit.",
    "purpose": "What the loan will be used for.",
    "credit_amount": "Total amount of credit requested.",
    "savings_account": "Balance held in savings/bonds.",
    "employment_duration": "How long the applicant has been with their current employer.",
    "installment_rate": "Installment as a percentage of disposable income (1=low, 4=high).",
    "personal_status_sex": "Marital status combined with sex, as coded in the source dataset.",
    "other_debtors": "Whether a co-applicant or guarantor is attached to the loan.",
    "residence_since": "Years at current residence.",
    "property": "Most valuable property the applicant owns.",
    "age": "Applicant's age in years.",
    "other_installment_plans": "Other installment plans the applicant is paying into.",
    "housing": "Housing situation (rent, own, or provided free).",
    "existing_credits": "Number of existing credits at this bank.",
    "job": "Job / skill classification.",
    "dependents": "Number of people financially dependent on the applicant.",
    "telephone": "Whether a telephone is registered under the applicant's name.",
    "foreign_worker": "Whether the applicant is classified as a foreign worker.",
}

FEATURE_GROUPS = {
    "Financial Information": ["checking_account", "savings_account", "credit_amount"],
    "Loan Information": ["duration_months", "installment_rate", "purpose"],
    "Credit History": ["credit_history", "existing_credits", "other_installment_plans"],
    "Personal Information": ["age", "employment_duration", "dependents"],
    "Residence & Assets": ["residence_since", "property", "housing"],
    "Other Details": [
        "personal_status_sex",
        "other_debtors",
        "job",
        "telephone",
        "foreign_worker",
    ],
}

# ============================================================
# DROPDOWN MAPPINGS (label shown to user -> code the model expects)
# ============================================================

CHECKING_ACCOUNT_MAP = {
    "No checking account": "A14",
    "Less than 0 DM": "A11",
    "0 - 200 DM": "A12",
    "200 DM or more": "A13",
}

SAVINGS_ACCOUNT_MAP = {
    "Less than 100 DM": "A61",
    "100 - 500 DM": "A62",
    "500 - 1,000 DM": "A63",
    "1,000 DM or more": "A64",
    "Unknown / No savings account": "A65",
}

PURPOSE_MAP = {
    "New car": "A40",
    "Used car": "A41",
    "Furniture / Equipment": "A42",
    "Radio / Television": "A43",
    "Domestic appliances": "A44",
    "Repairs": "A45",
    "Education": "A46",
    "Vacation": "A47",
    "Retraining": "A48",
    "Business": "A49",
    "Other": "A410",
}

CREDIT_HISTORY_MAP = {
    "No credits taken / all credits paid back duly": "A30",
    "All credits at this bank paid back duly": "A31",
    "Existing credits paid back duly till now": "A32",
    "Delay in paying off in the past": "A33",
    "Critical account / other credits existing elsewhere": "A34",
}

OTHER_INSTALLMENT_MAP = {
    "Bank": "A141",
    "Stores": "A142",
    "None": "A143",
}

EMPLOYMENT_MAP = {
    "Unemployed": "A71",
    "Less than 1 year": "A72",
    "1 - 4 years": "A73",
    "4 - 7 years": "A74",
    "7 years or more": "A75",
}

PROPERTY_MAP = {
    "Real estate": "A121",
    "Building society / Life insurance": "A122",
    "Car or other property": "A123",
    "Unknown / No property": "A124",
}

HOUSING_MAP = {
    "Rent": "A151",
    "Own": "A152",
    "Free / Provided": "A153",
}

PERSONAL_STATUS_MAP = {
    "Male - Divorced / Separated": "A91",
    "Female - Divorced / Separated / Married": "A92",
    "Male - Single": "A93",
    "Male - Married / Widowed": "A94",
    "Female - Single": "A95",
}

OTHER_DEBTORS_MAP = {
    "None": "A101",
    "Co-applicant": "A102",
    "Guarantor": "A103",
}

JOB_MAP = {
    "Unemployed / Unskilled non-resident": "A171",
    "Unskilled resident": "A172",
    "Skilled employee / Official": "A173",
    "Management / Self-employed / Highly qualified": "A174",
}

TELEPHONE_MAP = {
    "No telephone": "A191",
    "Telephone registered": "A192",
}

FOREIGN_WORKER_MAP = {
    "Yes": "A201",
    "No": "A202",
}


# ============================================================
# MODEL LOADING
# ============================================================

@st.cache_resource(show_spinner="Loading model...")
def load_model():
    """
    Load the trained model once and cache it across pages/reruns.
    Returns (model, error_message). If loading fails, model is None
    and error_message explains why, so callers can show a clean
    message instead of crashing the app.
    """
    if not os.path.exists(MODEL_PATH):
        return None, (
            f"Model file not found at `{MODEL_PATH}`. "
            "Make sure `credit_model.pkl` is placed inside the `models/` folder."
        )
    try:
        model = joblib.load(MODEL_PATH)
        return model, None
    except Exception as exc:  # noqa: BLE001 - we want to surface any load error to the user
        return None, f"Failed to load model: {exc}"


# ============================================================
# SHARED PAGE CONFIG + CSS
# ============================================================

def configure_page(page_title: str, page_icon: str = "💳"):
    """Apply consistent st.set_page_config + CSS across all pages."""
    st.set_page_config(
        page_title=f"{page_title} · Credit Risk Predictor",
        page_icon=page_icon,
        layout="wide",
        initial_sidebar_state="expanded",
    )
    _inject_css()


def _inject_css():
    st.markdown(
        """
        <style>
        .stApp { background: #ffffff; }
        .block-container { max-width: 1180px; padding-top: 35px; padding-bottom: 50px; }
        #MainMenu { visibility: hidden; }
        footer { visibility: hidden; }
        header { background: transparent !important; }

        html, body, [class*="css"] {
            font-family: Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
        }

        /* ========================================================
           FORCE TEXT COLOR — safety net against dark-mode inheritance
           Without this, text can render white-on-white if the user's
           system/browser is set to dark mode, since Streamlit's base
           theme flips text color to white while our cards stay white.
           ======================================================== */

        .stApp, .stApp p, .stApp span, .stApp li, .stApp label,
        .stMarkdown, [data-testid="stMarkdownContainer"],
        [data-testid="stMarkdownContainer"] p,
        [data-testid="stMarkdownContainer"] li,
        [data-testid="stExpander"] p,
        [data-testid="stExpander"] span,
        [data-testid="stExpander"] summary,
        [data-testid="stExpander"] summary span,
        [data-testid="stMetricValue"],
        [data-testid="stMetricLabel"],
        [data-testid="stCaptionContainer"],
        div[data-baseweb="select"] * ,
        .stSelectbox label,
        .stNumberInput label,
        .stDataFrame, .stTable {
            color: #111827 !important;
        }

        /* Info/warning/success/error boxes keep readable text too */
        div[data-testid="stAlert"] p,
        div[data-testid="stAlert"] span {
            color: inherit !important;
        }

        .main-title {
            font-size: 42px; font-weight: 750; letter-spacing: -1.5px;
            color: #111827; margin-bottom: 4px;
        }
        .subtitle { color: #6b7280; font-size: 17px; margin-bottom: 30px; }
        .section-title {
            color: #111827; font-size: 22px; font-weight: 700;
            margin-top: 8px; margin-bottom: 18px;
        }
        .subsection-title {
            color: #374151; font-size: 17px; font-weight: 650;
            margin-top: 18px; margin-bottom: 12px;
        }

        hr { border: none; border-top: 1px solid #e5e7eb; margin: 25px 0; }

        label { color: #374151 !important; font-weight: 550 !important; }
        div[data-baseweb="select"] > div {
            background: #ffffff !important; border: 1px solid #d1d5db !important;
            border-radius: 9px !important;
        }
        div[data-baseweb="select"] > div:hover { border-color: #9ca3af !important; }
        input {
            background: #ffffff !important; border: 1px solid #d1d5db !important;
            border-radius: 9px !important; color: #111827 !important;
        }
        input:focus { border-color: #6b7280 !important; box-shadow: none !important; }

        div[data-testid="stForm"] {
            background: #ffffff; border: 1px solid #e5e7eb; border-radius: 16px;
            padding: 26px 28px; box-shadow: 0 4px 18px rgba(0, 0, 0, 0.04);
        }

        div.stButton > button, button[kind="primaryFormSubmit"] {
            background: #111827 !important; color: #ffffff !important;
            border: none !important; border-radius: 9px !important;
            height: 50px; font-size: 16px; font-weight: 650;
            transition: all 0.2s ease;
        }
        div.stButton > button:hover, button[kind="primaryFormSubmit"]:hover {
            background: #1f2937 !important; transform: translateY(-1px);
        }

        .result-card {
            background: #ffffff; border: 1px solid #e5e7eb; border-radius: 18px;
            padding: 32px; margin-top: 15px; text-align: center;
            box-shadow: 0 8px 30px rgba(0, 0, 0, 0.05);
        }
        .result-icon { font-size: 38px; margin-bottom: 8px; }
        .result-title { font-size: 30px; font-weight: 750; color: #111827; margin-bottom: 8px; }
        .result-description { font-size: 16px; color: #6b7280; margin-bottom: 4px; }

        .probability-card {
            background: #ffffff; border: 1px solid #e5e7eb; border-radius: 14px;
            padding: 20px; text-align: center; min-height: 105px;
            box-shadow: 0 3px 12px rgba(0, 0, 0, 0.03);
        }
        .probability-label { font-size: 14px; color: #6b7280; margin-bottom: 8px; }
        .probability-value { font-size: 27px; font-weight: 750; color: #111827; }

        .summary-card {
            background: #f9fafb; border: 1px solid #e5e7eb; border-radius: 14px;
            padding: 22px; margin-top: 15px;
        }

        .info-card {
            background: #ffffff; border: 1px solid #e5e7eb; border-radius: 14px;
            padding: 22px; margin-bottom: 16px;
            box-shadow: 0 3px 12px rgba(0, 0, 0, 0.03);
        }

        .custom-footer {
            text-align: center; color: #9ca3af; font-size: 13px;
            margin-top: 45px; padding-top: 20px; border-top: 1px solid #f0f0f0;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_footer():
    st.markdown(
        """
        <div class="custom-footer">
            Credit Risk Predictor · Machine Learning Project
          
        </div>
        """,
        unsafe_allow_html=True,
    )