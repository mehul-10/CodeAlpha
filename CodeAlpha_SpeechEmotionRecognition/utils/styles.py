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
            color: #111827;
        }

        .main .block-container {
            max-width: 1180px;
            padding-top: 2rem;
            padding-bottom: 3rem;
        }


        /* =====================================================
           SIDEBAR
        ===================================================== */

        [data-testid="stSidebar"] {
            background: #f8fafc;
            border-right: 1px solid #e5e7eb;
        }

        [data-testid="stSidebar"] * {
            color: #111827;
        }


        /* =====================================================
           TYPOGRAPHY
        ===================================================== */

        h1, h2, h3 {
            color: #111827 !important;
            letter-spacing: -0.02em;
        }

        p {
            color: #4b5563;
        }


        /* =====================================================
           HERO
        ===================================================== */

        .hero {
            padding: 3rem 0 2rem 0;
        }

        .hero-badge {
            display: inline-block;
            padding: 0.45rem 0.8rem;
            background: #eff6ff;
            color: #2563eb;
            border: 1px solid #dbeafe;
            border-radius: 999px;
            font-size: 0.85rem;
            font-weight: 600;
            margin-bottom: 1rem;
        }

        .hero-title {
            font-size: 3.4rem;
            line-height: 1.05;
            font-weight: 800;
            color: #111827;
            margin-bottom: 1rem;
        }

        .hero-subtitle {
            font-size: 1.15rem;
            line-height: 1.7;
            max-width: 720px;
            color: #6b7280;
        }


        /* =====================================================
           CARDS
        ===================================================== */

        .card {
            background: #ffffff;
            border: 1px solid #e5e7eb;
            border-radius: 18px;
            padding: 1.5rem;
            margin-bottom: 1rem;
            box-shadow: 0 4px 18px rgba(15, 23, 42, 0.04);
        }

        .card-title {
            font-size: 1.05rem;
            font-weight: 700;
            color: #111827;
            margin-bottom: 0.5rem;
        }

        .card-text {
            color: #6b7280;
            line-height: 1.65;
        }


        /* =====================================================
           STAT CARDS
        ===================================================== */

        .stat-card {
            background: #ffffff;
            border: 1px solid #e5e7eb;
            border-radius: 16px;
            padding: 1.25rem;
            text-align: center;
            height: 100%;
            box-shadow: 0 4px 18px rgba(15, 23, 42, 0.04);
        }

        .stat-value {
            font-size: 1.8rem;
            font-weight: 800;
            color: #111827;
        }

        .stat-label {
            font-size: 0.85rem;
            color: #6b7280;
            margin-top: 0.25rem;
        }


        /* =====================================================
           PREDICTION
        ===================================================== */

        .prediction-card {
            background: #f8fafc;
            border: 1px solid #e5e7eb;
            border-radius: 20px;
            padding: 2rem;
            text-align: center;
            margin: 1.5rem 0;
        }

        .prediction-emoji {
            font-size: 3.5rem;
            margin-bottom: 0.5rem;
        }

        .prediction-emotion {
            font-size: 2.2rem;
            font-weight: 800;
            color: #111827;
        }

        .prediction-confidence {
            font-size: 1rem;
            color: #6b7280;
            margin-top: 0.5rem;
        }


        /* =====================================================
           SECTION LABEL
        ===================================================== */

        .section-label {
            font-size: 0.78rem;
            font-weight: 700;
            color: #2563eb;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            margin-bottom: 0.5rem;
        }


        /* =====================================================
           FOOTER
        ===================================================== */

        .footer {
            margin-top: 4rem;
            padding-top: 1.5rem;
            border-top: 1px solid #e5e7eb;
            text-align: center;
            color: #6b7280;
            font-size: 0.85rem;
        }


        /* =====================================================
           RESPONSIVE
        ===================================================== */

        @media (max-width: 768px) {

            .main .block-container {
                padding-left: 1rem;
                padding-right: 1rem;
            }

            .hero-title {
                font-size: 2.35rem;
            }

            .hero-subtitle {
                font-size: 1rem;
            }

            .prediction-emotion {
                font-size: 1.8rem;
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
                Built with Python, TensorFlow, Librosa & Streamlit
            </div>
            <div style="margin-top: 6px;">
                © 2026 Mehul Gupta · Speech Emotion Recognition
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )