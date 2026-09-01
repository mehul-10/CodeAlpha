# Credit Risk Predictor

A multi-page Streamlit app that estimates credit risk using a trained
Random Forest classifier on the German Credit dataset.

## Structure

```
credit_risk_app/
├── Home.py                          # Landing page
├── utils.py                         # Shared mappings, model loader, CSS
├── models/
│   └── credit_model.pkl             # <-- put your trained model here
├── pages/
│   ├── 1_🔮_Predict.py              # Form + prediction
│   ├── 2_📊_Model_Insights.py       # Feature importance + field reference
│   └── 3_ℹ️_About.py                # Performance metrics + disclaimer
└── requirements.txt
```

## Setup

1. Place your trained model at `models/credit_model.pkl`. It must
   support `.predict()` and `.predict_proba()`, and expect a DataFrame
   with these 20 columns in this order:

   ```
   checking_account, duration_months, credit_history, purpose,
   credit_amount, savings_account, employment_duration,
   installment_rate, personal_status_sex, other_debtors,
   residence_since, property, age, other_installment_plans,
   housing, existing_credits, job, dependents, telephone,
   foreign_worker
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the app:
   ```
   streamlit run Home.py
   ```

## What changed from the original single-file version

- **Multi-page layout** — the form, feature/importance info, and
  performance metrics now live on separate pages (`Home`, `Predict`,
  `Model Insights`, `About`) instead of one long scrolling page.
- **No more silent crash on missing model** — `joblib.load` is wrapped
  in a cached loader that returns a clear error message instead of
  throwing an unhandled exception at import time.
- **Prediction errors are caught** — if the model rejects the input
  (e.g. a column mismatch), the app shows a message instead of a raw
  traceback.
- **Mappings centralized in `utils.py`** — every dropdown-to-code
  mapping (checking account, purpose, job, etc.) is defined once and
  imported everywhere, so the Predict and Model Insights pages can't
  drift out of sync.
- **New Model Insights page** — shows a feature-importance chart (when
  the model supports it) and a plain-language description of every
  input field, grouped the same way as the form.
- **Shared styling via `configure_page()`** — consistent look across
  all pages without repeating the CSS block in every file.