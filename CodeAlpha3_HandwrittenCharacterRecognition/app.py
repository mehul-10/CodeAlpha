import textwrap

import streamlit as st


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

    md(
        """
        <div style="padding: 10px 0 20px 0;">
            <div style="font-size: 28px; font-weight: 700;">
                ✍️ DigitAI
            </div>
            <div style="color: #666; font-size: 14px; margin-top: 5px;">
                Handwritten Digit Recognition
            </div>
        </div>
        """
    )

    st.markdown("---")

    md(
        """
        <div style="font-size: 13px; color: #666; line-height: 1.6;">
            A CNN-powered handwritten digit
            recognition application trained
            on the MNIST dataset.
        </div>
        """
    )

    st.markdown("---")

    md(
        """
        <div style="font-size: 13px; color: #777; line-height: 1.6;">
            <strong>Developer</strong><br>
            Mehul Gupta
        </div>
        """
    )

    md(
        """
        <div style="margin-top: 12px; font-size: 13px;">
            <a href="https://github.com/mehul-10"
               target="_blank"
               style="text-decoration: none; margin-right: 15px;">
                GitHub
            </a>
            <a href="https://www.linkedin.com/in/mehulgupta-developer/"
               target="_blank"
               style="text-decoration: none;">
                LinkedIn
            </a>
        </div>
        """
    )


# ============================================================
# RUN APPLICATION
# ============================================================

pg.run()