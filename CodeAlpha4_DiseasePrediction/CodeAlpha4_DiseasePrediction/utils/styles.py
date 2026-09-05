import streamlit as st


def apply_custom_css():
    st.markdown(
        """
        <style>

        /* =====================================================
           GLOBAL
        ===================================================== */

        .stApp {
            background: #ffffff;
            color: #222222;
        }

        .block-container {
            max-width: 1200px;
            padding-top: 2rem;
            padding-bottom: 3rem;
        }

        h1, h2, h3, h4 {
            color: #111111;
        }

        p, li, span, label {
            color: #333333;
        }


        /* =====================================================
           SIDEBAR
           ===================================================== */

        section[data-testid="stSidebar"] {
            background: #fafafa;
            border-right: 1px solid #eeeeee;
        }

        .sidebar-brand {
            text-align: center;
            padding: 10px 0 20px 0;
        }

        .sidebar-logo {
            font-size: 42px;
        }

        .sidebar-title {
            font-size: 22px;
            font-weight: 800;
            color: #111111;
            margin-top: 4px;
        }

        .sidebar-subtitle {
            font-size: 13px;
            color: #777777;
            line-height: 1.5;
        }

        .sidebar-developer {
            font-size: 13px;
            color: #666666;
            text-align: center;
            margin-top: 25px;
        }


        /* =====================================================
           PAGE HEADER
           ===================================================== */

        .page-header {
            margin-bottom: 30px;
        }

        .section-label {
            font-size: 12px;
            font-weight: 700;
            letter-spacing: 1.5px;
            text-transform: uppercase;
            color: #777777;
            margin-bottom: 8px;
        }

        .page-title {
            font-size: 38px;
            font-weight: 800;
            color: #111111;
            margin-bottom: 8px;
        }

        .page-subtitle {
            font-size: 17px;
            color: #666666;
            line-height: 1.6;
            max-width: 800px;
        }


        /* =====================================================
           HERO
           ===================================================== */

        .hero {
            background: #f7f7f7;
            border: 1px solid #eeeeee;
            border-radius: 20px;
            padding: 42px;
            margin-bottom: 30px;
        }

        .hero-badge {
            display: inline-block;
            background: #ffffff;
            border: 1px solid #dddddd;
            border-radius: 999px;
            padding: 7px 14px;
            font-size: 12px;
            font-weight: 700;
            color: #555555;
            margin-bottom: 16px;
        }

        .hero-title {
            font-size: 44px;
            line-height: 1.1;
            font-weight: 850;
            color: #111111;
            margin: 0 0 15px 0;
        }

        .hero-subtitle {
            font-size: 17px;
            line-height: 1.7;
            color: #666666;
            max-width: 750px;
        }


        /* =====================================================
           CARDS
           ===================================================== */

        .content-card {
            background: #ffffff;
            border: 1px solid #e9e9e9;
            border-radius: 16px;
            padding: 25px;
            margin-bottom: 20px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.03);
        }

        .card-title {
            font-size: 20px;
            font-weight: 750;
            color: #111111;
            margin-bottom: 8px;
        }

        .card-text {
            font-size: 15px;
            color: #666666;
            line-height: 1.7;
        }


        /* =====================================================
           STAT CARDS
           ===================================================== */

        .stat-card {
            background: #fafafa;
            border: 1px solid #eeeeee;
            border-radius: 15px;
            padding: 22px;
            text-align: center;
        }

        .stat-value {
            font-size: 28px;
            font-weight: 800;
            color: #111111;
        }

        .stat-label {
            font-size: 13px;
            color: #777777;
            margin-top: 5px;
        }


        /* =====================================================
           PREDICTION
           ===================================================== */

        .prediction-card {
            background: #f7f7f7;
            border: 1px solid #e5e5e5;
            border-radius: 20px;
            padding: 35px;
            text-align: center;
            margin: 25px 0;
        }

        .prediction-icon {
            font-size: 45px;
            margin-bottom: 10px;
        }

        .prediction-title {
            font-size: 30px;
            font-weight: 800;
            color: #111111;
        }

        .prediction-confidence {
            font-size: 17px;
            color: #666666;
            margin-top: 8px;
        }


        /* =====================================================
           WORKFLOW
           ===================================================== */

        .workflow-step {
            display: flex;
            align-items: center;
            gap: 16px;
            color: #333333;
            line-height: 1.5;
            margin-bottom: 15px;
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


        /* =====================================================
           UPLOADER
           ===================================================== */

        [data-testid="stFileUploader"] {
            border: 1px dashed #cccccc;
            border-radius: 15px;
            padding: 10px;
        }


        /* =====================================================
           BUTTONS
           ===================================================== */

        .stButton > button {
            border-radius: 10px;
            border: 1px solid #dddddd;
            background: #111111;
            color: #ffffff;
            font-weight: 650;
            padding: 10px 20px;
        }

        .stButton > button:hover {
            background: #333333;
            border-color: #333333;
        }


        /* =====================================================
           DISCLAIMER
           ===================================================== */

        .disclaimer {
            background: #fafafa;
            border: 1px solid #eeeeee;
            border-radius: 12px;
            padding: 18px;
            margin-top: 30px;
            color: #666666;
            font-size: 13px;
            line-height: 1.6;
        }


        /* =====================================================
           FOOTER
           ===================================================== */

        .footer {
            border-top: 1px solid #eeeeee;
            margin-top: 45px;
            padding-top: 20px;
            text-align: center;
            color: #888888;
            font-size: 13px;
        }


        /* =====================================================
           MOBILE
           ===================================================== */

        @media (max-width: 768px) {

            .hero {
                padding: 25px;
            }

            .hero-title {
                font-size: 32px;
            }

            .page-title {
                font-size: 30px;
            }

            .block-container {
                padding-left: 1rem;
                padding-right: 1rem;
            }
        }
          .info-card {
        background: #ffffff;
        border: 1px solid #e5e7eb;
        border-radius: 16px;
        padding: 24px;
        margin: 12px 0;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.04);
    }

    .info-card h3 {
        margin-top: 0;
        margin-bottom: 8px;
    }

    .feature-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 24px;
        background: #ffffff;
        border: 1px solid #e5e7eb;
        border-radius: 12px;
        padding: 15px 18px;
        margin: 8px 0;
    }

    .feature-row strong {
        min-width: 220px;
    }

    .feature-row span {
        color: #6b7280;
        text-align: right;
    }

    @media (max-width: 768px) {

        .feature-row {
            flex-direction: column;
            align-items: flex-start;
            gap: 5px;
        }

        .feature-row span {
            text-align: left;
        }

    }

        </style>
        """,
        unsafe_allow_html=True
    )


def render_footer():
    st.markdown(
        """
        <div class="footer">
            Built with Python, Scikit-learn & Streamlit ·
            CodeAlpha Machine Learning Internship ·
            <strong>Mehul Gupta</strong>
        </div>
        """,
        unsafe_allow_html=True
    )