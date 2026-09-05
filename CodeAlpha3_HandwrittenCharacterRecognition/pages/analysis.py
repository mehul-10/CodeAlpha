import os
import textwrap

import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report

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
    page_title="Model Analysis",
    page_icon="📊",
    layout="wide"
)

apply_custom_css()


# ============================================================
# PATHS
# ============================================================

EVALUATION_DIR = "models/evaluation"

METRICS_PATH = os.path.join(
    EVALUATION_DIR,
    "evaluation_metrics.npz"
)

CONFUSION_MATRIX_PATH = os.path.join(
    EVALUATION_DIR,
    "confusion_matrix.png"
)

PER_DIGIT_PATH = os.path.join(
    EVALUATION_DIR,
    "per_digit_accuracy.png"
)

REPORT_PATH = os.path.join(
    EVALUATION_DIR,
    "classification_report.txt"
)


# ============================================================
# HEADER
# ============================================================

md(
    """
    <div class="page-header">
        <div class="section-label">MODEL EVALUATION</div>
        <h1>Performance Analysis</h1>
        <p>
            Detailed evaluation of the handwritten digit recognition
            CNN on the MNIST test dataset.
        </p>
    </div>
    """
)


# ============================================================
# CHECK EVALUATION FILE
# ============================================================

if not os.path.exists(METRICS_PATH):

    st.error(
        "Evaluation data could not be found."
    )

    st.info(
        "Please run evaluate_model.py first."
    )

    st.stop()


# ============================================================
# LOAD EVALUATION DATA
# ============================================================

try:

    metrics = np.load(
        METRICS_PATH,
        allow_pickle=True
    )

    y_true = metrics["y_true"]
    y_pred = metrics["y_pred"]

except Exception as error:

    st.error(
        f"Unable to load evaluation data: {error}"
    )

    st.stop()


# ============================================================
# CALCULATE METRICS
# ============================================================

accuracy = float(
    np.mean(y_true == y_pred)
)

report = classification_report(
    y_true,
    y_pred,
    labels=list(range(10)),
    target_names=[str(i) for i in range(10)],
    output_dict=True,
    zero_division=0
)

macro_precision = report["macro avg"]["precision"]
macro_recall = report["macro avg"]["recall"]
macro_f1 = report["macro avg"]["f1-score"]

weighted_precision = report["weighted avg"]["precision"]
weighted_recall = report["weighted avg"]["recall"]
weighted_f1 = report["weighted avg"]["f1-score"]


# ============================================================
# MAIN METRICS
# ============================================================

st.markdown("### 📈 Overall Performance")

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(
        "Test Accuracy",
        f"{accuracy * 100:.2f}%"
    )

with col2:

    st.metric(
        "Macro Precision",
        f"{macro_precision * 100:.2f}%"
    )

with col3:

    st.metric(
        "Macro Recall",
        f"{macro_recall * 100:.2f}%"
    )

with col4:

    st.metric(
        "Macro F1 Score",
        f"{macro_f1 * 100:.2f}%"
    )


# ============================================================
# PERFORMANCE SUMMARY CARD
# ============================================================

md(
    f"""
    <div class="content-card">
        <div class="card-title">
            🎯 Evaluation Summary
        </div>
        <div class="card-text">
            The CNN achieved a test accuracy of
            <strong>{accuracy * 100:.2f}%</strong>
            on the MNIST test dataset.
            <br><br>
            The macro-averaged precision, recall, and F1-score are
            <strong>{macro_precision * 100:.2f}%</strong>,
            <strong>{macro_recall * 100:.2f}%</strong>, and
            <strong>{macro_f1 * 100:.2f}%</strong>
            respectively.
            <br><br>
            These results indicate that the model performs consistently
            across the ten handwritten digit classes.
        </div>
    </div>
    """
)


# ============================================================
# PER-DIGIT PERFORMANCE
# ============================================================

st.markdown("### 🔢 Per-Digit Performance")


digit_rows = []

for digit in range(10):

    digit_string = str(digit)

    digit_rows.append(
        {
            "Digit": digit_string,
            "Precision": report[digit_string]["precision"],
            "Recall": report[digit_string]["recall"],
            "F1 Score": report[digit_string]["f1-score"],
            "Support": int(report[digit_string]["support"]),
        }
    )


digit_df = pd.DataFrame(digit_rows)


display_df = digit_df.copy()

display_df["Precision"] = (
    display_df["Precision"] * 100
).round(2)

display_df["Recall"] = (
    display_df["Recall"] * 100
).round(2)

display_df["F1 Score"] = (
    display_df["F1 Score"] * 100
).round(2)


display_df = display_df.rename(
    columns={
        "Precision": "Precision (%)",
        "Recall": "Recall (%)",
        "F1 Score": "F1 Score (%)"
    }
)


st.dataframe(
    display_df,
    use_container_width=True,
    hide_index=True
)


# ============================================================
# BEST / WEAKEST DIGIT
# ============================================================

best_digit_index = digit_df["F1 Score"].idxmax()
worst_digit_index = digit_df["F1 Score"].idxmin()

best_digit = digit_df.loc[
    best_digit_index,
    "Digit"
]

worst_digit = digit_df.loc[
    worst_digit_index,
    "Digit"
]

best_f1 = digit_df.loc[
    best_digit_index,
    "F1 Score"
]

worst_f1 = digit_df.loc[
    worst_digit_index,
    "F1 Score"
]


col1, col2 = st.columns(2)

with col1:

    md(
        f"""
        <div class="content-card">
            <div class="card-title">
                🏆 Strongest Class
            </div>
            <div class="card-text">
                Digit <strong>{best_digit}</strong>
                achieved the highest F1-score of
                <strong>{best_f1 * 100:.2f}%</strong>
                on the test dataset.
            </div>
        </div>
        """
    )


with col2:

    md(
        f"""
        <div class="content-card">
            <div class="card-title">
                🔍 Most Challenging Class
            </div>
            <div class="card-text">
                Digit <strong>{worst_digit}</strong>
                had the lowest F1-score of
                <strong>{worst_f1 * 100:.2f}%</strong>
                among the ten classes.
            </div>
        </div>
        """
    )


# ============================================================
# CONFUSION MATRIX
# ============================================================

st.markdown("### 🧩 Confusion Matrix")

md(
    """
    <div class="content-card">
        <div class="card-text">
            The confusion matrix shows how the model's predictions
            are distributed across the ten digit classes.
            Diagonal values represent correctly classified images,
            while off-diagonal values represent misclassifications.
        </div>
    </div>
    """
)


if os.path.exists(CONFUSION_MATRIX_PATH):

    st.image(
        CONFUSION_MATRIX_PATH,
        use_container_width=True
    )

else:

    st.warning(
        "Confusion matrix image was not found."
    )


# ============================================================
# PER-DIGIT ACCURACY CHART
# ============================================================

st.markdown("### 📊 Accuracy by Digit")


if os.path.exists(PER_DIGIT_PATH):

    st.image(
        PER_DIGIT_PATH,
        use_container_width=True
    )

else:

    # Create chart directly if saved image is unavailable

    digit_accuracy = []

    for digit in range(10):

        mask = y_true == digit

        if np.sum(mask) > 0:

            digit_acc = np.mean(
                y_pred[mask] == digit
            )

        else:

            digit_acc = 0

        digit_accuracy.append(
            digit_acc * 100
        )


    fig, ax = plt.subplots(
        figsize=(10, 5)
    )

    ax.bar(
        range(10),
        digit_accuracy
    )

    ax.set_xlabel("Digit")
    ax.set_ylabel("Accuracy (%)")
    ax.set_title("Per-Digit Test Accuracy")
    ax.set_xticks(range(10))
    ax.set_ylim(0, 105)

    st.pyplot(
        fig,
        use_container_width=True
    )

    plt.close(fig)


# ============================================================
# CLASSIFICATION REPORT
# ============================================================

st.markdown("### 📋 Classification Report")


classification_data = digit_df[
    [
        "Digit",
        "Precision",
        "Recall",
        "F1 Score",
        "Support"
    ]
].copy()


classification_data = classification_data.rename(
    columns={
        "Digit": "Class",
        "F1 Score": "F1-Score"
    }
)


st.dataframe(
    classification_data.style.format(
        {
            "Precision": "{:.4f}",
            "Recall": "{:.4f}",
            "F1-Score": "{:.4f}",
        }
    ),
    use_container_width=True,
    hide_index=True
)


# ============================================================
# AVERAGE METRICS
# ============================================================

st.markdown("### 📌 Average Metrics")


col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "Weighted Precision",
        f"{weighted_precision * 100:.2f}%"
    )

with col2:

    st.metric(
        "Weighted Recall",
        f"{weighted_recall * 100:.2f}%"
    )

with col3:

    st.metric(
        "Weighted F1",
        f"{weighted_f1 * 100:.2f}%"
    )


# ============================================================
# RAW CLASSIFICATION REPORT
# ============================================================

if os.path.exists(REPORT_PATH):

    with st.expander(
        "View Original Classification Report"
    ):

        try:

            with open(
                REPORT_PATH,
                "r",
                encoding="utf-8"
            ) as file:

                report_text = file.read()

            st.code(
                report_text,
                language="text"
            )

        except Exception as error:

            st.warning(
                f"Could not read classification report: {error}"
            )


# ============================================================
# INTERPRETATION
# ============================================================

st.markdown("### 💡 What These Results Mean")

md(
    """
    <div class="content-card">
        <div class="card-title">
            Model Interpretation
        </div>
        <div class="card-text">
            <strong>Accuracy</strong><br>
            Measures the overall percentage of test images classified
            correctly.
            <br><br>
            <strong>Precision</strong><br>
            Measures how often predictions for a particular digit are
            actually correct.
            <br><br>
            <strong>Recall</strong><br>
            Measures how effectively the model identifies all examples
            belonging to a particular digit.
            <br><br>
            <strong>F1 Score</strong><br>
            Combines precision and recall into a single performance
            measure. It is useful when comparing performance across
            individual digit classes.
            <br><br>
            <strong>Confusion Matrix</strong><br>
            Helps identify which digits are most frequently confused
            with one another.
        </div>
    </div>
    """
)


# ============================================================
# IMPORTANT NOTE
# ============================================================

md(
    """
    <div class="disclaimer">
        <strong>Important:</strong><br><br>
        The reported performance is based on the MNIST test dataset.
        MNIST contains standardized 28 × 28 grayscale handwritten
        digit images. Performance on real-world photographs,
        handwritten notes, different backgrounds, unusual writing
        styles, or significantly different image formats may be lower.
    </div>
    """
)


# ============================================================
# FOOTER
# ============================================================

render_footer()