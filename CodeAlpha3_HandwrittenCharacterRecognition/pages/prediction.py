import textwrap

import streamlit as st
from PIL import Image

from utils.image_utils import preprocess_image
from utils.model_utils import predict_digit
from utils.styles import apply_custom_css, render_footer


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
    page_title="Digit Prediction | Handwritten Character Recognition",
    page_icon="✍️",
    layout="wide"
)

apply_custom_css()


# ============================================================
# HEADER
# ============================================================

md(
    """
    <div class="page-header">
        <div class="section-label">AI PREDICTION</div>
        <h1>Handwritten Digit Recognition</h1>
        <p>
            Upload an image of a handwritten digit and let the
            trained CNN identify it.
        </p>
    </div>
    """
)


# ============================================================
# UPLOAD SECTION
# ============================================================

md(
    """
    <div class="content-card">
        <div class="card-title">Upload a handwritten digit</div>
        <div class="card-text">
            Upload a clear image containing one handwritten digit
            from 0 to 9.
        </div>
    </div>
    """
)

uploaded_file = st.file_uploader(
    "Choose an image",
    type=["png", "jpg", "jpeg"],
    label_visibility="collapsed"
)


# ============================================================
# PREDICTION
# ============================================================

if uploaded_file is not None:

    try:

        # ----------------------------------------------------
        # Load uploaded image
        # ----------------------------------------------------

        original_image = Image.open(
            uploaded_file
        )

        # ----------------------------------------------------
        # Preprocess image
        # ----------------------------------------------------

        processed_array, processed_image = (
            preprocess_image(original_image)
        )

        # ----------------------------------------------------
        # Prediction
        # ----------------------------------------------------

        predicted_digit, confidence, probabilities = (
            predict_digit(processed_array)
        )

        # ----------------------------------------------------
        # Display images
        # ----------------------------------------------------

        md(
            """
            <div class="section-label">
                IMAGE PROCESSING
            </div>
            """
        )

        col1, col2 = st.columns(2)

        with col1:

            st.markdown(
                "### Original Image"
            )

            st.image(
                original_image,
                use_container_width=True
            )

        with col2:

            st.markdown(
                "### Processed Image"
            )

            st.image(
                processed_image,
                width=280
            )

            st.caption(
                "Converted to 28 × 28 grayscale format"
            )


        # ----------------------------------------------------
        # Prediction result
        # ----------------------------------------------------

        md("<br>")

        md(
            """
            <div class="section-label">
                PREDICTION RESULT
            </div>
            """
        )

        result_col1, result_col2 = st.columns(
            [1, 2]
        )

        with result_col1:

            md(
                f"""
                <div class="prediction-card">
                    <div class="prediction-emoji">🔢</div>
                    <div class="prediction-emotion">{predicted_digit}</div>
                    <div class="prediction-confidence">Predicted Digit</div>
                </div>
                """
            )

        with result_col2:

            confidence_percentage = confidence * 100

            st.metric(
                "Confidence",
                f"{confidence_percentage:.2f}%"
            )

            st.progress(
                confidence
            )

            if confidence >= 0.90:

                st.success(
                    f"High-confidence prediction: "
                    f"the model predicts **{predicted_digit}**."
                )

            elif confidence >= 0.70:

                st.warning(
                    f"Moderate-confidence prediction: "
                    f"the model predicts **{predicted_digit}**."
                )

            else:

                st.warning(
                    f"Low-confidence prediction: "
                    f"the model predicts **{predicted_digit}**. "
                    "Try a clearer image."
                )


        # ----------------------------------------------------
        # Probability distribution
        # ----------------------------------------------------

        md(
            """
            <div class="section-label">
                MODEL PROBABILITIES
            </div>
            """
        )

        probability_data = {
            "Digit": [
                str(i)
                for i in range(10)
            ],
            "Probability": [
                float(probability)
                for probability in probabilities
            ]
        }

        st.bar_chart(
            probability_data,
            x="Digit",
            y="Probability"
        )


        # ----------------------------------------------------
        # Exact probabilities
        # ----------------------------------------------------

        with st.expander(
            "View exact probabilities"
        ):

            for digit, probability in enumerate(
                probabilities
            ):

                st.write(
                    f"**{digit}** — "
                    f"{probability * 100:.4f}%"
                )


    except ValueError as error:

        st.error(
            f"Unable to process this image: {error}"
        )

    except Exception as error:

        st.error(
            "Something went wrong while processing "
            "the image."
        )

        st.exception(error)


else:

    # ========================================================
    # EMPTY STATE
    # ========================================================

    md(
        """
        <div class="content-card">
            <div class="card-title">
                Ready for a prediction?
            </div>
            <div class="card-text">
                Upload a PNG, JPG, or JPEG image containing
                a single handwritten digit.
            </div>
        </div>
        """
    )


# ============================================================
# MODEL INFORMATION
# ============================================================

md(
    """
    <div class="content-card">
        <div class="card-title">
            About the model
        </div>
        <div class="card-text">
            This application uses a Convolutional Neural Network
            trained on the MNIST handwritten digit dataset.
            The model achieved <strong>99.50% test accuracy</strong>
            on 10,000 unseen MNIST test images.
        </div>
    </div>
    """
)


# ============================================================
# DISCLAIMER
# ============================================================

md(
    """
    <div class="disclaimer">
        <strong>Educational Project</strong><br>
        This application is developed as a machine learning
        internship project. Predictions may vary depending on
        handwriting style, image quality, positioning, and
        preprocessing.
    </div>
    """
)


# ============================================================
# FOOTER
# ============================================================

render_footer()