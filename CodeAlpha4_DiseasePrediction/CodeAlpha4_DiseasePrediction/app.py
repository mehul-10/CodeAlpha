import streamlit as st

from utils.styles import inject_css


st.set_page_config(
    page_title="MediPredict",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

inject_css()


# ============================================================
# NAVIGATION
# ============================================================

home = st.Page(
    "pages/home.py",
    title="Home",
    icon="⌂"
)

prediction = st.Page(
    "pages/prediction.py",
    title="Predict Diabetes",
    icon="🩺"
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
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        """
        <div style="
            padding: 10px 0 20px 0;
        ">
            <h1 style="
                margin: 0;
                font-size: 28px;
                font-weight: 700;
            ">
                🩺 MediPredict
            </h1>

            <p style="
                color: #6b7280;
                margin-top: 5px;
            ">
                Diabetes Risk Prediction
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    st.markdown(
        """
        <div style="
            font-size: 13px;
            color: #6b7280;
            line-height: 1.6;
        ">
            An educational machine learning application
            built with Python, Scikit-learn and Streamlit.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    st.markdown("**Developer**")

    st.markdown(
        """
        <div style="
            font-size: 14px;
            font-weight: 600;
        ">
            Mehul Gupta
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("")

    st.link_button(
        "GitHub",
        "https://github.com/mehul-10",
        use_container_width=True
    )

    st.link_button(
        "LinkedIn",
        "https://www.linkedin.com/in/mehulgupta-developer/",
        use_container_width=True
    )


# ============================================================
# RUN NAVIGATION
# ============================================================

pg = st.navigation(
    [
        home,
        prediction,
        analysis,
        model_info,
        about
    ]
)

pg.run()