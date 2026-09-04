import streamlit as st


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Handwritten Digit Recognition",
    page_icon="✍️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# PAGE DEFINITIONS
# ============================================================

home = st.Page(
    "pages/home.py",
    title="Home",
    icon="🏠",
    default=True
)

prediction = st.Page(
    "pages/prediction.py",
    title="Digit Prediction",
    icon="✍️"
)

analysis = st.Page(
    "pages/analysis.py",
    title="Model Analysis",
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


# ============================================================
# NAVIGATION
# ============================================================

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
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        """
        <div style="
            padding: 10px 0 20px 0;
        ">
            <div style="
                font-size: 28px;
                font-weight: 700;
            ">
                ✍️ DigitAI
            </div>

            <div style="
                color: #666;
                font-size: 14px;
                margin-top: 5px;
            ">
                Handwritten Digit Recognition
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.markdown(
        """
        <div style="
            font-size: 13px;
            color: #666;
            line-height: 1.6;
        ">
            A CNN-powered handwritten digit
            recognition application trained
            on the MNIST dataset.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.markdown(
        """
        <div style="
            font-size: 13px;
            color: #777;
            line-height: 1.6;
        ">
            <strong>Developer</strong><br>
            Mehul Gupta
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style="
            margin-top: 12px;
            font-size: 13px;
        ">
            <a href="https://github.com/mehul-10"
               target="_blank"
               style="
                   text-decoration: none;
                   margin-right: 15px;
               ">
                GitHub
            </a>

            <a href="https://www.linkedin.com/in/mehulgupta-developer/"
               target="_blank"
               style="
                   text-decoration: none;
               ">
                LinkedIn
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# RUN APPLICATION
# ============================================================

pg.run()