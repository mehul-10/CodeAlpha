import streamlit as st


def apply_custom_css():
    st.markdown(
        """
        <style>

        /* ==================================================
           GLOBAL
        ================================================== */

        .stApp {
            background-color: #ffffff;
        }

        .main .block-container {
            max-width: 1200px;
            padding-top: 2rem;
            padding-bottom: 3rem;
        }

        /* ==================================================
           SIDEBAR
        ================================================== */

        section[data-testid="stSidebar"] {
            background-color: #fafafa;
            border-right: 1px solid #eeeeee;
        }

        section[data-testid="stSidebar"] * {
            color: #222222;
        }

        /* ==================================================
           TYPOGRAPHY
        ================================================== */

        h1 {
            font-size: 42px !important;
            font-weight: 750 !important;
            letter-spacing: -1.5px;
            color: #111111;
        }

        h2 {
            color: #111111;
        }

        h3 {
            color: #222222;
        }

        p {
            color: #555555;
        }

        /* ==================================================
           PAGE HEADER
        ================================================== */

        .page-header {
            padding: 10px 0 30px 0;
        }

        .page-header h1 {
            margin-top: 8px;
            margin-bottom: 10px;
        }

        .page-header p {
            font-size: 17px;
            max-width: 750px;
            line-height: 1.7;
        }

        /* ==================================================
           SECTION LABEL
        ================================================== */

        .section-label {
            font-size: 12px;
            font-weight: 700;
            letter-spacing: 1.5px;
            color: #777777;
            margin-bottom: 8px;
        }

        /* ==================================================
           CARDS
        ================================================== */

        .content-card {
            background: #ffffff;
            border: 1px solid #e8e8e8;
            border-radius: 16px;
            padding: 24px;
            margin: 12px 0 24px 0;
            box-shadow: 0 4px 18px rgba(0, 0, 0, 0.04);
        }

        .card-title {
            font-size: 20px;
            font-weight: 700;
            color: #171717;
            margin-bottom: 8px;
        }

        .card-text {
            font-size: 15px;
            line-height: 1.7;
            color: #5c5c5c;
        }

        /* ==================================================
           PREDICTION CARD
        ================================================== */

        .prediction-card {
            background: #fafafa;
            border: 1px solid #e5e5e5;
            border-radius: 18px;
            padding: 30px;
            text-align: center;
            margin: 10px 0;
        }

        .prediction-emoji {
            font-size: 40px;
            margin-bottom: 8px;
        }

        .prediction-emotion {
            font-size: 64px;
            font-weight: 800;
            color: #111111;
            line-height: 1.1;
        }

        .prediction-confidence {
            margin-top: 10px;
            color: #777777;
            font-size: 14px;
        }

        /* ==================================================
           HERO
        ================================================== */

        .hero {
            padding: 30px 0 35px 0;
        }

        .hero-badge {
            display: inline-block;
            padding: 7px 12px;
            border-radius: 999px;
            background: #f3f3f3;
            color: #555555;
            font-size: 12px;
            font-weight: 700;
            letter-spacing: 0.7px;
        }

        .hero-title {
            font-size: 52px;
            font-weight: 800;
            line-height: 1.05;
            letter-spacing: -2px;
            color: #111111;
            margin: 16px 0 14px 0;
        }

        .hero-subtitle {
            font-size: 18px;
            line-height: 1.7;
            color: #666666;
            max-width: 800px;
        }

        /* ==================================================
           STAT CARDS
        ================================================== */

        .stat-card {
            background: #ffffff;
            border: 1px solid #e8e8e8;
            border-radius: 14px;
            padding: 20px;
            text-align: center;
            box-shadow: 0 3px 14px rgba(0, 0, 0, 0.035);
        }

        .stat-value {
            font-size: 28px;
            font-weight: 800;
            color: #111111;
        }

        .stat-label {
            font-size: 13px;
            color: #777777;
            margin-top: 4px;
        }

        /* ==================================================
           STREAMLIT FILE UPLOADER
        ================================================== */

        [data-testid="stFileUploader"] {
            border: 1px dashed #cccccc;
            border-radius: 14px;
            padding: 10px;
            background: #fafafa;
        }

        /* ==================================================
           METRICS
        ================================================== */

        [data-testid="stMetric"] {
            background: #fafafa;
            border: 1px solid #e8e8e8;
            border-radius: 14px;
            padding: 18px;
        }

        /* ==================================================
           BUTTONS
        ================================================== */

        .stButton > button {
            border-radius: 10px;
            border: 1px solid #dddddd;
            padding: 10px 20px;
            font-weight: 600;
            background: #111111;
            color: #ffffff;
        }

        .stButton > button:hover {
            border-color: #111111;
        }

        /* ==================================================
           ALERTS
        ================================================== */

        .stAlert {
            border-radius: 12px;
        }

        /* ==================================================
           EXPANDERS
        ================================================== */

        .streamlit-expanderHeader {
            font-weight: 600;
        }

        /* ==================================================
           TABLES
        ================================================== */

        [data-testid="stDataFrame"] {
            border-radius: 12px;
            overflow: hidden;
        }

        /* ==================================================
           DISCLAIMER
        ================================================== */

        .disclaimer {
            background: #f8f8f8;
            border: 1px solid #e5e5e5;
            border-radius: 14px;
            padding: 18px 20px;
            margin: 25px 0;
            color: #666666;
            font-size: 13px;
            line-height: 1.6;
        }

        /* ==================================================
           FOOTER
        ================================================== */

        .footer {
            text-align: center;
            color: #888888;
            font-size: 13px;
            padding: 35px 0 10px 0;
            border-top: 1px solid #eeeeee;
            margin-top: 45px;
        }

        /* ==================================================
           MOBILE
        ================================================== */

        @media (max-width: 768px) {

            .main .block-container {
                padding-left: 1rem;
                padding-right: 1rem;
            }

            h1 {
                font-size: 32px !important;
            }

            .hero-title {
                font-size: 38px;
            }

            .hero-subtitle {
                font-size: 16px;
            }

            .prediction-emotion {
                font-size: 52px;
            }

        }
        /* ==================================================
   WORKFLOW
   ================================================== */

.workflow-step {
    display: flex;
    align-items: center;
    gap: 16px;
    color: #333333;
    line-height: 1.5;
}

.workflow-step span {
    color: #777777;
    font-size: 14px;
}

.workflow-number {
    min-width: 42px;
    height: 42px;
    border-radius: 50%;
    background: #f2f2f2;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 13px;
    font-weight: 700;
    color: #333333;
}

        </style>
        """,
        unsafe_allow_html=True
    )


def render_footer():
    st.markdown(
        """
        <div class="footer">
            <div>
                Built with Python, TensorFlow & Streamlit
            </div>
            <div style="margin-top: 6px;">
                Handwritten Digit Recognition · CodeAlpha ML Internship
            </div>
            <div style="margin-top: 6px;">
                Developed by <strong>Mehul Gupta</strong>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )