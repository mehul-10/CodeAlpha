import pandas as pd
import streamlit as st

from utils import (
    configure_page,
    render_footer,
    load_model,
    FEATURE_COLUMNS,
    FEATURE_DESCRIPTIONS,
    FEATURE_GROUPS,
)

configure_page("Model Insights", page_icon="📊")

st.markdown('<div class="main-title">📊 Model Insights</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">What the model looks at, and how much each input matters</div>',
    unsafe_allow_html=True,
)
st.divider()

model, error = load_model()
if error:
    st.error(f"🚫 {error}")
    st.stop()

# ============================================================
# FEATURE IMPORTANCE
# ============================================================
st.markdown('<div class="section-title">Feature Importance</div>', unsafe_allow_html=True)

if hasattr(model, "feature_importances_"):
    importances = pd.Series(model.feature_importances_, index=FEATURE_COLUMNS)
    importances = importances.sort_values(ascending=False)

    st.write(
        "These values show how much each field influences the model's "
        "predictions overall — not how any single applicant is scored."
    )
    st.bar_chart(importances, height=420)

    with st.expander("See exact importance values"):
        st.dataframe(
            importances.rename("Importance").to_frame().style.format({"Importance": "{:.4f}"}),
            use_container_width=True,
        )
else:
    st.info(
        "This model type doesn't expose `feature_importances_`, so a "
        "per-feature importance chart isn't available. The field "
        "reference below still explains what each input means."
    )

st.divider()

# ============================================================
# FIELD REFERENCE
# ============================================================
st.markdown('<div class="section-title">Field Reference</div>', unsafe_allow_html=True)
st.write("Every field in the Predict form, grouped the same way as the form itself.")

for group_name, fields in FEATURE_GROUPS.items():
    st.markdown(f'<div class="subsection-title">{group_name}</div>', unsafe_allow_html=True)
    for field in fields:
        st.markdown(
            f"""
            <div class="info-card">
                <b>{field.replace('_', ' ').title()}</b><br/>
                <span style="color:#6b7280;">{FEATURE_DESCRIPTIONS.get(field, '')}</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

render_footer()