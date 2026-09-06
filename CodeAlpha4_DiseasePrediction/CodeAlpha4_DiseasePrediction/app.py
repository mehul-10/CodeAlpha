import textwrap

import streamlit as st
import app_utils.styles as styles


def md(html: str) -> None:
    """
    st.markdown wrapper that strips leading indentation.

    Markdown treats any line indented with 4+ spaces as a
    preformatted code block. HTML snippets defined inside
    nested Python blocks (with/if/for) pick up that indentation
    from the triple-quoted string and get rendered as literal
    code instead of parsed HTML. Dedenting fixes that.

    IMPORTANT: blank lines *inside* the HTML also break rendering,
    since Markdown treats a blank line as the end of a raw HTML
    block. Never leave a fully empty line between tags in the
    strings passed to this function -- use <br> instead.
    """
    st.markdown(textwrap.dedent(html).strip(), unsafe_allow_html=True)


# set_page_config MUST be the very first Streamlit command in the
# script -- calling apply_custom_css() (which uses st.markdown) before
# this raises StreamlitAPIException.
st.set_page_config(
    page_title="MediPredict",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

styles.apply_custom_css()

md(
    """
    <style>
    .sidebar-logo {
        display: flex;
        align-items: center;
        gap: 12px;
        padding: 6px 0 4px 0;
    }
    .sidebar-logo-badge {
        width: 42px;
        height: 42px;
        border-radius: 12px;
        background: linear-gradient(160deg, #0f766e 0%, #14a89c 100%);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 20px;
        box-shadow: 0 4px 12px rgba(15, 118, 110, 0.25);
        flex-shrink: 0;
    }
    .sidebar-logo-text {
        display: flex;
        flex-direction: column;
        line-height: 1.15;
    }
    .sidebar-logo-title {
        font-size: 18px;
        font-weight: 800;
        color: #0f0f10;
        letter-spacing: -0.3px;
    }
    .sidebar-logo-subtitle {
        font-size: 12px;
        color: #6b6b70;
        margin-top: 2px;
    }
    .sidebar-blurb {
        font-size: 13px;
        color: #6b6b70;
        line-height: 1.65;
        padding: 4px 0;
    }
    .sidebar-developer-card {
        background: #ffffff;
        border: 1px solid #e8e8ec;
        border-radius: 14px;
        padding: 14px 16px;
        margin: 4px 0 10px 0;
    }
    .sidebar-developer-label {
        font-size: 10.5px;
        font-weight: 800;
        letter-spacing: 1.2px;
        color: #9a9aa0;
        margin-bottom: 4px;
    }
    .sidebar-developer-name {
        font-size: 14.5px;
        font-weight: 700;
        color: #0f0f10;
    }
    </style>
    """
)


# ============================================================
# NAVIGATION
# ============================================================

home = st.Page(
    "pages/home.py",
    title="Home",
    icon="🏠"
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

    md(
        """
        <div class="sidebar-logo">
            <div class="sidebar-logo-badge">🩺</div>
            <div class="sidebar-logo-text">
                <div class="sidebar-logo-title">MediPredict</div>
                <div class="sidebar-logo-subtitle">Diabetes Risk Prediction</div>
            </div>
        </div>
        """
    )

    st.divider()

    md(
        """
        <div class="sidebar-blurb">
            An educational machine learning application
            built with Python, Scikit-learn and Streamlit.
        </div>
        """
    )

    st.divider()

    md(
        """
        <div class="sidebar-developer-card">
            <div class="sidebar-developer-label">DEVELOPER</div>
            <div class="sidebar-developer-name">Mehul Gupta</div>
        </div>
        """
    )

    link_col1, link_col2 = st.columns(2)

    with link_col1:
        st.link_button(
            "GitHub",
            "https://github.com/mehul-10",
            use_container_width=True
        )

    with link_col2:
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