# World Cup Analytics & Prediction Platform

A full-stack football analytics platform built using Python, FastAPI, PostgreSQL and Streamlit. The platform analyses historical international football data, provides interactive analytics dashboards, predicts match outcomes using a rule-based prediction engine, and is being extended with a machine learning prediction model.

---

# Overview

The World Cup Analytics & Prediction Platform was developed to explore historical international football data while demonstrating modern software engineering principles.

The application provides:

- REST API built with FastAPI
- PostgreSQL relational database
- Interactive Streamlit dashboard
- Team analytics
- Historical World Cup analytics
- Rule-based match prediction engine
- Machine Learning prediction pipeline (In Progress)

The project follows a layered architecture consisting of repositories, services, routers and presentation components to encourage separation of concerns and maintainability.

---

# Technology Stack

## Backend

- Python 3
- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic

## Frontend

- Streamlit
- Plotly
- Pandas

## Database

- PostgreSQL
- SQLAlchemy ORM

## Machine Learning (Planned)

- Scikit-Learn
- Joblib
- NumPy
- Pandas

## Testing

- Pytest

## DevOps (Planned)

- Docker
- Docker Compose
- GitHub Actions

---

# Architecture

```
Dashboard (Streamlit)
        │
        ▼
REST API (FastAPI)
        │
        ▼
Services
        │
        ▼
Repositories
        │
        ▼
PostgreSQL
```

The application separates:

- Data Access
- Business Logic
- API Layer
- User Interface

to improve scalability and maintainability.

---

# Features

## Team Analytics

- Team Summary
- Wins
- Draws
- Losses
- Goals Scored
- Goals Conceded
- Goal Difference
- Win Percentage

---

## Head-to-Head Analysis

Compare two national teams.

Displays:

- Matches Played
- Wins
- Draws
- Goals Scored
- Goal Difference
- Win Rates

---

## Team Comparison

Compares two teams using:

- Team Summary
- Strength Score
- Historical Performance
- Head-to-Head Statistics

---

## Strength Score Engine

Custom weighted scoring system based on:

- Recent Form
- Historical Win Percentage
- Goal Difference

The score is normalised to produce an overall team strength score.

---

## Rule-Based Match Prediction

Predicts the likely winner using:

- Team Strength
- Recent Form
- Win Percentage
- Goal Difference
- Head-to-Head Bonus

Returns:

- Predicted Winner
- Confidence Rating
- Human-readable Explanation

---

## World Cup History

Interactive historical dashboard containing:

- Tournament Overview
- Tournament Timeline
- Most Successful Nations
- Tournament Explorer
- Historical Statistics

---

# Project Structure

```
World-Cup-Analytics-Platform/

app/
dashboard/
services/
tests/
docs/
scripts/

data/
    raw/

ml/ (Planned)

saved_models/ (Planned)
```

---

# Database

Current entities include:

- Teams
- Matches
- World Cups

The database currently contains:

- Historical international football matches
- National teams
- Historical FIFA World Cup tournaments

---

# REST API

Current endpoints include:

## Teams

- GET /teams

## Analytics

- GET /analytics/team/{team}
- GET /analytics/recent-form/{team}
- GET /analytics/head-to-head
- GET /analytics/strength/{team}
- GET /analytics/compare

## Prediction

- GET /prediction

## World Cup History

- GET /history/overview
- GET /history/timeline
- GET /history/winners
- GET /history/tournament/{year}
- GET /history/facts

Swagger documentation is available at:

```
http://localhost:8000/docs
```

---

# Dashboard Pages

Current dashboard includes:

- Home
- Team Analytics
- Team Comparison
- Match Predictor
- World Cup History

---

# Machine Learning Roadmap

The next phase of development introduces supervised machine learning.

Training dataset:

- Historical international football matches

Testing dataset:

- FIFA World Cup matches

Target:

- Home Win
- Draw
- Away Win

Models to be evaluated:

- Logistic Regression
- Random Forest
- Gradient Boosting

Evaluation metrics:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

The best-performing model will be integrated into the prediction API.

---

# Testing

Current testing framework:

- Pytest

Planned coverage:

- Repository tests
- Service tests
- Prediction engine tests
- API endpoint tests
- Machine learning validation tests

---

# DevOps Roadmap

Planned improvements include:

- Docker
- Docker Compose
- GitHub Actions
- Automated testing
- CI/CD pipeline

---

# Sprint Progress

## Sprint 1

Completed

- Project setup
- PostgreSQL configuration
- Database schema
- Team import
- Match import

---

## Sprint 2

Completed

- Repository layer
- Analytics services
- FastAPI endpoints
- Swagger documentation

---

## Sprint 3

Completed

- Streamlit dashboard
- Team Analytics
- Team Comparison
- Prediction dashboard

---

## Sprint 4

Completed

- Rule-based prediction engine
- Strength score engine
- Prediction explanations
- World Cup History dashboard

---

## Sprint 5 (Current)

In Progress

- Machine Learning dataset preparation
- Feature engineering
- Model training
- Model evaluation

---

## Sprint 6

Planned

- ML model deployment
- API integration
- Prediction comparison
- Dashboard enhancements

---

## Sprint 7

Planned

- Docker
- Docker Compose
- GitHub Actions
- Automated testing

---

## Sprint 8

Planned

- Documentation
- UML diagrams
- ERD
- Deployment diagrams
- Final polish

---

# Future Enhancements

- FIFA Rankings
- Elo Ratings
- Player statistics
- Live match integration
- Tournament simulation
- Model comparison dashboard
- Prediction confidence visualisation

---

# Author

Developed as a Software Engineering portfolio project demonstrating:

- Backend Software Engineering
- Database Design
- REST API Development
- Data Analytics
- Machine Learning
- Software Architecture
- DevOps