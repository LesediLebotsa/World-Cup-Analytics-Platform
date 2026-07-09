# Machine Learning Design Decisions

## Overview

The World Cup Analytics Platform includes a machine learning component designed to predict the outcome of international football matches.

Unlike the rule-based prediction engine, which relies on manually defined weights and thresholds, the machine learning model will learn patterns directly from historical match data.

The machine learning model is intended to complement the existing rule-based prediction engine, allowing both approaches to be compared within the application.

---

# Prediction Objective

The objective of the model is to predict the outcome of a football match before it is played.

The problem is treated as a multiclass classification problem with three possible outcomes.

| Target | Outcome |
|---------|---------|
| 0 | Away Win |
| 1 | Draw |
| 2 | Home Win |

---

# Training Dataset

The model will be trained using the complete historical international football matches dataset imported into PostgreSQL.

This dataset contains more than 17,000 international matches from multiple competitions and countries.

The decision to use all international matches rather than only FIFA World Cup matches was made for several reasons:

- Provides a significantly larger training dataset.
- Reduces the likelihood of overfitting.
- Allows the model to learn from a wider variety of opponents and playing styles.
- Produces more reliable strength estimates for national teams.
- Improves generalisation to future competitions.

---

# Model Evaluation Dataset

The 2022 FIFA World Cup dataset will not be included in the initial training dataset.

Instead, it will be reserved for evaluating the model after training.

This approach simulates predicting a future tournament using only historical information and provides a more realistic measure of model performance.

---

# Feature Engineering

Rather than training directly on raw match data, engineered features will be generated from the existing analytics engine.

The following features will be included:

- Home team strength score
- Away team strength score
- Home recent form
- Away recent form
- Home win percentage
- Away win percentage
- Home goal difference
- Away goal difference
- Head-to-head wins
- Head-to-head goal difference

These features are derived from the existing analytics services to ensure consistency between the analytics dashboard, rule-based engine and machine learning model.

---

# Machine Learning Models

Multiple supervised learning algorithms will be trained and evaluated.

## Logistic Regression

Purpose:

- Baseline classification model.

Reasons for selection:

- Fast to train.
- Easy to interpret.
- Common benchmark for multiclass classification.
- Provides a performance baseline for comparison.

---

## Random Forest Classifier

Purpose:

- Primary prediction model.

Reasons for selection:

- Handles nonlinear relationships well.
- Robust to noisy data.
- Reduces overfitting through ensemble learning.
- Performs well with tabular datasets.
- Requires minimal feature scaling.

---

## Gradient Boosting Classifier

Purpose:

- Alternative ensemble model.

Reasons for selection:

- Often achieves higher predictive accuracy.
- Learns complex interactions between features.
- Frequently performs well on structured datasets.
- Useful for comparison against Random Forest.

---

# Model Selection

All trained models will be evaluated using the same testing dataset.

The best-performing model will be selected based on evaluation metrics rather than personal preference.

The selected model will be saved and used by the prediction API.

---

# Evaluation Metrics

Each model will be evaluated using the following metrics:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

Using multiple evaluation metrics provides a more complete assessment of model performance than accuracy alone.

---

# Model Persistence

After evaluation, the best-performing model will be saved using Joblib.

Example:

```python
joblib.dump(model, "saved_models/match_predictor.pkl")
```

Persisting the model avoids retraining every time the application starts.

---

# API Integration

The trained model will be integrated into the existing FastAPI backend.

The prediction workflow will become:

User Request

↓

Feature Engineering

↓

Machine Learning Model

↓

Prediction

↓

Dashboard

The existing rule-based prediction engine will remain available for comparison.

---

# Future Improvements

The machine learning component has been designed to support future enhancements, including:

- FIFA Ranking integration
- Elo rating integration
- Player availability
- Squad market value
- Home advantage weighting
- Expected Goals (xG)
- Ensemble prediction combining multiple models
- Live match prediction using current tournament data

---

# Expected Project Benefits

Adding machine learning expands the project from a rule-based analytics application into a complete football prediction platform.

The combination of:

- Software Engineering
- Data Engineering
- Data Analytics
- Machine Learning
- REST APIs
- PostgreSQL
- Streamlit Dashboard
- Docker
- CI/CD

creates a comprehensive portfolio project demonstrating both backend software engineering and applied machine learning.