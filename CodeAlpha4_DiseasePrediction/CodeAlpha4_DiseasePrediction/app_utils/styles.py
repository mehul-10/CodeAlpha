import streamlit as st


def apply_custom_css():
    st.markdown(
        """
        <style>

        /* ==================================================
           DESIGN TOKENS
        ================================================== */

        :root {
            --ink-900: #0f0f10;
            --ink-700: #2a2a2c;
            --ink-500: #6b6b70;
            --ink-300: #9a9aa0;
            --surface-0: #ffffff;
            --surface-1: #fafafa;
            --surface-2: #f3f3f5;
            --border-soft: #e8e8ec;
            --border-strong: #d8d8de;
            --accent: #0f766e;
            --accent-hover: #0c5f59;
            --accent-soft: #e6f4f2;
            --danger: #b3441e;
            --danger-soft: #fbeee7;
            --radius-sm: 10px;
            --radius-md: 14px;
            --radius-lg: 18px;
            --radius-xl: 22px;
            --shadow-sm: 0 2px 8px rgba(15, 15, 16, 0.05);
            --shadow-md: 0 6px 20px rgba(15, 15, 16, 0.07);
            --shadow-lg: 0 14px 34px rgba(15, 15, 16, 0.10);
            --ease: cubic-bezier(0.22, 1, 0.36, 1);
        }

        /* ==================================================
           GLOBAL
        ================================================== */

        html, body, [class*="css"] {
            font-family: "Inter", "Segoe UI", -apple-system,
                BlinkMacSystemFont, sans-serif !important;
        }

        .stApp {
            background: linear-gradient(
                180deg,
                #ffffff 0%,
                #fbfbfc 100%
            );
        }

        .main .block-container {
            max-width: 1200px;
            padding-top: 2.2rem;
            padding-bottom: 3.5rem;
        }

        ::selection {
            background: rgba(15, 118, 110, 0.15);
        }

        ::-webkit-scrollbar {
            width: 10px;
            height: 10px;
        }

        ::-webkit-scrollbar-track {
            background: transparent;
        }

        ::-webkit-scrollbar-thumb {
            background: var(--border-strong);
            border-radius: 10px;
        }

        ::-webkit-scrollbar-thumb:hover {
            background: var(--ink-300);
        }

        /* ==================================================
           SIDEBAR
        ================================================== */

        section[data-testid="stSidebar"] {
            background: var(--surface-1);
            border-right: 1px solid var(--border-soft);
        }

        section[data-testid="stSidebar"] * {
            color: var(--ink-700) !important;
        }

        /* ==================================================
           TYPOGRAPHY
        ================================================== */

        h1 {
            font-size: 40px !important;
            font-weight: 800 !important;
            letter-spacing: -1.3px;
            color: var(--ink-900) !important;
            line-height: 1.15 !important;
        }

        h2 {
            font-weight: 750 !important;
            letter-spacing: -0.6px;
            color: var(--ink-900) !important;
        }

        h3 {
            font-weight: 700 !important;
            color: var(--ink-700) !important;
        }

      p,
li,
ul,
ol,
span:not(.hero-badge):not(.eyebrow):not(.stat-label):not(.workflow-step span):not(.feature-row span):not(.section-label) {
    color: var(--ink-500) !important;
}

strong,
b {
    color: var(--ink-900) !important;
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

        .eyebrow {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            font-size: 11.5px;
            font-weight: 800;
            letter-spacing: 1.6px;
            color: var(--accent) !important;
            margin-bottom: 10px;
        }

        .eyebrow::before {
            content: "";
            width: 6px;
            height: 6px;
            border-radius: 50%;
            background: var(--accent);
            display: inline-block;
        }

        .section-label {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            font-size: 11.5px;
            font-weight: 800;
            letter-spacing: 1.6px;
            color: var(--accent) !important;
            margin-bottom: 10px;
        }

        .section-label::before {
            content: "";
            width: 6px;
            height: 6px;
            border-radius: 50%;
            background: var(--accent);
            display: inline-block;
        }

        /* ==================================================
           CARDS
        ================================================== */

        .content-card {
            background: var(--surface-0);
            border: 1px solid var(--border-soft);
            border-radius: var(--radius-lg);
            padding: 26px 28px;
            margin: 12px 0 24px 0;
            box-shadow: var(--shadow-sm);
            transition: box-shadow 0.25s var(--ease),
                transform 0.25s var(--ease),
                border-color 0.25s var(--ease);
        }

        .content-card:hover {
            box-shadow: var(--shadow-md);
            border-color: var(--border-strong);
            transform: translateY(-2px);
        }

        .card-title {
            font-size: 20px;
            font-weight: 750;
            color: var(--ink-900);
            margin-bottom: 8px;
        }

        .card-text {
            font-size: 15px;
            line-height: 1.7;
            color: var(--ink-500);
        }

        .info-card {
            background: var(--surface-0);
            border: 1px solid var(--border-soft);
            border-left: 3px solid var(--accent);
            border-radius: var(--radius-lg);
            padding: 22px 26px;
            margin: 12px 0 22px 0;
            box-shadow: var(--shadow-sm);
            transition: box-shadow 0.25s var(--ease),
                transform 0.25s var(--ease);
        }

        .info-card:hover {
            box-shadow: var(--shadow-md);
            transform: translateY(-2px);
        }

        .info-card h3 {
            margin-top: 0;
            margin-bottom: 6px;
        }

        .info-card p {
            margin-bottom: 8px;
        }

        .info-card p:last-child {
            margin-bottom: 0;
        }

        .hero-card {
            background: linear-gradient(
                160deg,
                var(--accent-soft) 0%,
                #ffffff 100%
            );
            border: 1px solid var(--border-soft);
            border-radius: var(--radius-xl);
            padding: 30px 32px;
            margin: 12px 0 24px 0;
            box-shadow: var(--shadow-md);
        }

        .hero-card h2 {
            margin-top: 6px;
            margin-bottom: 8px;
        }

        .feature-row {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 16px;
            padding: 14px 18px;
            border: 1px solid var(--border-soft);
            border-radius: var(--radius-md);
            margin-bottom: 8px;
            background: var(--surface-0);
            transition: background 0.2s var(--ease),
                border-color 0.2s var(--ease);
        }

        .feature-row:hover {
            background: var(--surface-1);
            border-color: var(--border-strong);
        }

        .feature-row strong {
            color: var(--ink-900);
            min-width: 160px;
        }

        .feature-row span {
            color: var(--ink-500);
            font-size: 14px;
            text-align: right;
        }

        /* ==================================================
           PREDICTION CARD
        ================================================== */

        .prediction-card {
            background: linear-gradient(
                160deg,
                #fbfbfc 0%,
                #f2f2f4 100%
            );
            border: 1px solid var(--border-soft);
            border-radius: var(--radius-xl);
            padding: 34px 30px;
            text-align: center;
            margin: 12px 0;
            box-shadow: var(--shadow-md);
            position: relative;
            overflow: hidden;
        }

        .prediction-card::before {
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 4px;
            background: linear-gradient(
                90deg,
                var(--accent),
                #4a4a4a,
                var(--accent)
            );
        }

        .prediction-icon {
            font-size: 42px;
            margin-bottom: 10px;
        }

        .prediction-title {
            font-size: 34px;
            font-weight: 800;
            color: var(--ink-900);
            line-height: 1.2;
            letter-spacing: -0.5px;
        }

        .prediction-confidence {
            margin-top: 12px;
            color: var(--ink-500);
            font-size: 14px;
            font-weight: 500;
        }

        /* ==================================================
           HERO
        ================================================== */

        .hero {
            padding: 34px 0 38px 0;
        }

        .hero-badge {
            display: inline-block;
            padding: 8px 14px;
            border-radius: 999px;
            background: var(--accent-soft);
            border: 1px solid var(--border-soft);
            color: var(--accent);
            font-size: 12px;
            font-weight: 750;
            letter-spacing: 0.7px;
        }

        .hero-title {
            font-size: 52px;
            font-weight: 850;
            line-height: 1.05;
            letter-spacing: -2px;
            color: var(--ink-900);
            margin: 18px 0 14px 0;
        }

        .hero-subtitle {
            font-size: 18px;
            line-height: 1.7;
            color: var(--ink-500);
            max-width: 800px;
        }

        /* ==================================================
           STAT CARDS
        ================================================== */

        .stat-card {
            background: var(--surface-0);
            border: 1px solid var(--border-soft);
            border-radius: var(--radius-md);
            padding: 22px;
            text-align: center;
            box-shadow: var(--shadow-sm);
            transition: transform 0.25s var(--ease),
                box-shadow 0.25s var(--ease);
        }

        .stat-card:hover {
            transform: translateY(-3px);
            box-shadow: var(--shadow-md);
        }

        .stat-value {
            font-size: 30px;
            font-weight: 800;
            color: var(--ink-900);
            letter-spacing: -0.5px;
        }

        .stat-label {
            font-size: 13px;
            color: var(--ink-500);
            margin-top: 4px;
        }

        /* ==================================================
           NUMBER INPUTS
        ================================================== */

        [data-testid="stNumberInput"] input {
            border-radius: var(--radius-sm) !important;
            border: 1px solid var(--border-strong) !important;
        }

        [data-testid="stNumberInput"] input:focus {
            border-color: var(--accent) !important;
            box-shadow: 0 0 0 3px var(--accent-soft) !important;
        }

        /* ==================================================
           METRICS
        ================================================== */

        [data-testid="stMetric"] {
            background: var(--surface-1);
            border: 1px solid var(--border-soft);
            border-radius: var(--radius-md);
            padding: 20px;
            transition: box-shadow 0.2s var(--ease);
        }

        [data-testid="stMetric"]:hover {
            box-shadow: var(--shadow-sm);
        }

        [data-testid="stMetricValue"] {
            color: var(--ink-900) !important;
            font-weight: 800 !important;
        }

        /* ==================================================
           BUTTONS
        ================================================== */

        .stButton > button {
            border-radius: var(--radius-sm);
            border: 1px solid var(--accent);
            padding: 12px 26px;
            font-weight: 650;
            font-size: 15px;
            background: var(--accent);
            color: #ffffff;
            box-shadow: var(--shadow-sm);
            transition: background 0.18s var(--ease),
                box-shadow 0.18s var(--ease),
                transform 0.18s var(--ease),
                border-color 0.18s var(--ease);
        }

        .stButton > button:hover {
            background: var(--accent-hover);
            border-color: var(--accent-hover);
            box-shadow: var(--shadow-md);
            transform: translateY(-1px);
        }

        .stButton > button:active {
            transform: translateY(0);
            box-shadow: var(--shadow-sm);
        }

        .stButton > button:focus-visible {
            outline: none;
            box-shadow: 0 0 0 3px rgba(15, 118, 110, 0.22);
        }

        .stButton > button p {
            color: #ffffff !important;
        }

        .stButton > button[kind="secondary"] {
            background: var(--surface-0);
            color: var(--ink-900);
            border: 1.5px solid var(--border-strong);
            box-shadow: none;
        }

        .stButton > button[kind="secondary"] p {
            color: var(--ink-900) !important;
        }

        .stButton > button[kind="secondary"]:hover {
            background: var(--surface-1);
            border-color: var(--ink-700);
        }

        /* ==================================================
           LINK BUTTONS
        ================================================== */

        .stLinkButton > a {
            border-radius: var(--radius-sm) !important;
            border: 1.5px solid var(--border-strong) !important;
            padding: 12px 26px !important;
            font-weight: 650 !important;
            background: var(--surface-0) !important;
            color: var(--ink-900) !important;
            box-shadow: var(--shadow-sm);
            transition: background 0.18s var(--ease),
                border-color 0.18s var(--ease),
                transform 0.18s var(--ease);
        }

        .stLinkButton > a:hover {
            background: var(--surface-1) !important;
            border-color: var(--accent) !important;
            transform: translateY(-1px);
        }

        /* ==================================================
           DOWNLOAD BUTTONS
        ================================================== */

        .stDownloadButton > button {
            border-radius: var(--radius-sm);
            border: 1px solid var(--accent);
            padding: 12px 26px;
            font-weight: 650;
            background: var(--accent);
            color: #ffffff;
            box-shadow: var(--shadow-sm);
            transition: background 0.18s var(--ease),
                box-shadow 0.18s var(--ease),
                transform 0.18s var(--ease);
        }

        .stDownloadButton > button:hover {
            background: var(--accent-hover);
            box-shadow: var(--shadow-md);
            transform: translateY(-1px);
        }

        /* ==================================================
           PROGRESS BAR
        ================================================== */

        .stProgress > div > div {
            background: linear-gradient(
                90deg,
                var(--accent),
                #14a89c
            ) !important;
            border-radius: 999px;
        }

        .stProgress > div {
            background: var(--surface-2) !important;
            border-radius: 999px;
        }

        /* ==================================================
           ALERTS
        ================================================== */

        .stAlert {
            border-radius: var(--radius-md);
            border: 1px solid var(--border-soft);
        }

        /* ==================================================
           EXPANDERS
        ================================================== */

        .streamlit-expanderHeader {
            font-weight: 650;
            border-radius: var(--radius-sm);
        }

        details[data-testid="stExpander"] {
            border: 1px solid var(--border-soft);
            border-radius: var(--radius-md);
            box-shadow: var(--shadow-sm);
        }

        /* ==================================================
           TABLES
        ================================================== */

        [data-testid="stDataFrame"] {
            border-radius: var(--radius-md);
            overflow: hidden;
            border: 1px solid var(--border-soft);
        }

        /* ==================================================
           WORKFLOW
        ================================================== */

        .workflow-step {
            display: flex;
            align-items: flex-start;
            gap: 16px;
            color: var(--ink-700);
            line-height: 1.5;
            padding: 10px 0;
        }

        .workflow-step p {
            color: var(--ink-500);
            font-size: 14px;
            margin: 2px 0 0 0;
        }

        .workflow-step span {
            color: var(--ink-500);
            font-size: 14px;
        }

        .workflow-number {
            min-width: 42px;
            height: 42px;
            border-radius: 50%;
            background: var(--accent-soft);
            border: 1px solid var(--border-soft);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 13px;
            font-weight: 750;
            color: var(--accent);
            flex-shrink: 0;
        }

        /* ==================================================
           DISCLAIMER
        ================================================== */

        .disclaimer {
            background: var(--danger-soft);
            border: 1px solid #f0d9c8;
            border-left: 3px solid var(--danger);
            border-radius: var(--radius-md);
            padding: 18px 22px;
            margin: 25px 0;
            color: #7a4a2e !important;
            font-size: 13px;
            line-height: 1.6;
        }

        .disclaimer strong {
            color: var(--danger) !important;
        }

        /* ==================================================
           FOOTER
        ================================================== */

        .footer {
            text-align: center;
            color: var(--ink-300) !important;
            font-size: 13px;
            padding: 38px 0 10px 0;
            border-top: 1px solid var(--border-soft);
            margin-top: 48px;
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
                font-size: 30px !important;
            }

            .hero-title {
                font-size: 38px;
            }

            .hero-subtitle {
                font-size: 16px;
            }

            .prediction-title {
                font-size: 26px;
            }

            .content-card,
            .info-card {
                padding: 20px;
            }

            .feature-row {
                flex-direction: column;
                align-items: flex-start;
                gap: 4px;
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
            <div>
                Built with Python, Scikit-learn &amp; Streamlit
            </div>
            <div style="margin-top: 6px;">
                MediPredict &middot; CodeAlpha ML Internship
            </div>
            <div style="margin-top: 6px;">
                Developed by <strong>Mehul Gupta</strong>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )