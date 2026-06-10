# AI Loan Risk Prediction & Lead Prioritization System

## Overview

An end-to-end Machine Learning platform that predicts loan approval probability, customer risk level, and lead priority for financial institutions. The system exposes ML-powered predictions through FastAPI REST APIs and stores prediction history for auditing and analytics.

---

## Features

### Machine Learning Predictions

* Loan Approval Prediction
* Risk Classification
* Lead Prioritization
* Probability Scoring

### REST APIs

* Predict Loan Approval
* Predict Risk Level
* Prediction History Endpoint
* Interactive Swagger Documentation

### Data Persistence

* SQLite Database
* Prediction Audit Trail
* Historical Prediction Storage

### Engineering & DevOps

* FastAPI Backend
* SQLAlchemy ORM
* GitHub Actions CI/CD
* Automated Linting & Testing

---

## Tech Stack

### Machine Learning

* Python
* Pandas
* NumPy
* Scikit-Learn
* Random Forest Classifier
* Joblib

### Backend

* FastAPI
* Pydantic
* Uvicorn

### Database

* SQLite
* SQLAlchemy

### DevOps

* GitHub Actions

---

## Project Architecture

```text
Client / Swagger UI
        │
        ▼
FastAPI REST API
        │
        ▼
Machine Learning Service
        │
        ▼
Random Forest Model (.pkl)
        │
        ▼
Prediction Engine
        │
        ▼
SQLite Database
        │
        ▼
Prediction History API
```

---

## API Endpoints

### Health Check

```http
GET /
```

### Loan Prediction

```http
POST /api/v1/predict
```

Example Request:

```json
{
  "Gender": "Male",
  "Married": "Yes",
  "Dependents": "1",
  "Education": "Graduate",
  "Self_Employed": "No",
  "ApplicantIncome": 5000,
  "CoapplicantIncome": 1500,
  "LoanAmount": 120,
  "Loan_Amount_Term": 360,
  "Credit_History": 1,
  "Property_Area": "Urban"
}
```

Example Response:

```json
{
  "risk": "Low",
  "approval_probability": 0.84,
  "lead_priority": "High"
}
```

### Prediction History

```http
GET /api/v1/predict/history
```

---

## Dataset

The model is trained using a Loan Approval Prediction dataset containing:

* Applicant Income
* Co-applicant Income
* Loan Amount
* Loan Term
* Credit History
* Property Area
* Education
* Employment Information

Target Variable:

```text
Loan_Status
```

---

## Current Project Status

### Completed

* Repository Setup
* FastAPI Backend
* SQLite Database Integration
* SQLAlchemy ORM
* Dataset Processing
* Feature Engineering
* Random Forest Model Training
* Model Serialization (.pkl)
* ML Model Serving
* Prediction History Storage
* GitHub Actions CI/CD

### In Progress

* Docker Containerization
* PostgreSQL Migration
* Model Monitoring
* Azure Deployment

### Planned

* XGBoost Model
* Spark-Based Analytics
* Kafka Event Streaming
* Explainable AI (SHAP)
* Azure ML Integration
* Kubernetes Deployment

---

## Running Locally

Install dependencies:

```bash
pip install -r backend/requirements.txt
```

Run FastAPI:

```bash
cd backend
uvicorn main:app --reload
```

Swagger UI:

```text
http://localhost:8000/docs
```

---

## Resume Highlights

* Built an end-to-end Loan Risk Prediction platform using FastAPI and Scikit-Learn.
* Developed a Random Forest model for loan approval prediction and lead prioritization.
* Implemented REST APIs for real-time inference and prediction history.
* Integrated SQLite and SQLAlchemy for persistence and audit tracking.
* Automated quality checks using GitHub Actions CI/CD.
* Applied feature engineering, preprocessing, and model serialization for production-ready ML serving.
