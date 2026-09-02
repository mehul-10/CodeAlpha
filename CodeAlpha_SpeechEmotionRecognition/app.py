import streamlit as st

from utils.styles import apply_custom_css, render_footer


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Speech Emotion AI",
    page_icon="🎙️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# GLOBAL CSS
# ============================================================

apply_custom_css()


# ============================================================
# SIDEBAR BRANDING
# ============================================================

with st.sidebar:

    st.markdown(
        """
        <div style="
            padding: 0.5rem 0 1.5rem 0;
            text-align: center;
        ">
            <div style="font-size: 2.2rem;">🎙️</div>

            <div style="
                font-size: 1.15rem;
                font-weight: 800;
                color: #111827;
                margin-top: 0.4rem;
            ">
                Speech Emotion AI
            </div>

            <div style="
                font-size: 0.78rem;
                color: #6b7280;
                margin-top: 0.25rem;
            ">
                Deep Learning Project
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    st.caption("Explore")

    st.markdown(
        """
        <div style="
            padding: 0.8rem 0;
            color: #6b7280;
            font-size: 0.82rem;
            line-height: 1.6;
        ">
            Analyze speech, explore audio
            features, and learn how the
            emotion recognition model works.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    st.markdown(
        """
        <div style="text-align:center;">
            <div style="
                font-size: 0.75rem;
                color: #6b7280;
                margin-bottom: 0.5rem;
            ">
                Built by
            </div>

            <div style="
                font-weight: 700;
                color: #111827;
            ">
                Mehul Gupta
            </div>

            <div style="margin-top: 0.8rem;">

                <a href="https://github.com/mehul-10"
                   target="_blank"
                   style="
                       color:#2563eb;
                       text-decoration:none;
                       font-size:0.82rem;
                       margin-right:12px;
                   ">
                    GitHub
                </a>

                <a href="https://www.linkedin.com/in/mehulgupta-developer/"
                   target="_blank"
                   style="
                       color:#2563eb;
                       text-decoration:none;
                       font-size:0.82rem;
                   ">
                    LinkedIn
                </a>

            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# NAVIGATION
# ============================================================

home = st.Page(
    "pages/home.py",
    title="Home",
    icon="🏠",
    default=True
)

prediction = st.Page(
    "pages/prediction.py",
    title="Emotion Prediction",
    icon="🎤"
)

analysis = st.Page(
    "pages/analysis.py",
    title="Audio Analysis",
    icon="📊"
)

model_info = st.Page(
    "pages/model_info.py",
    title="Model & Dataset",
    icon="🧠"
)

about = st.Page(
    "pages/about.py",
    title="About",
    icon="ℹ️"
)


pg = st.navigation(
    {
        "Application": [
            home,
            prediction,
            analysis
        ],
        "Information": [
            model_info,
            about
        ]
    }
)


# ============================================================
# RUN SELECTED PAGE
# ============================================================

pg.run()