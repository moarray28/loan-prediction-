from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.models.request import LoanPredictionRequest
from app.models.response import LoanPredictionResponse

from app.db.dependencies import get_db
from app.db.models import Prediction

from app.services.ml_service import predict_loan
from app.services.prediction_service import save_prediction

router = APIRouter()


@router.get("/")
def prediction_root():
    return {
        "message": "Prediction API V1"
    }


@router.post(
    "/",
    response_model=LoanPredictionResponse
)

@router.post(
    "/",
    response_model=LoanPredictionResponse
)
def predict(
    request: LoanPredictionRequest,
    db: Session = Depends(get_db)
):
    prediction, probability = predict_loan(
        request.model_dump()
    )

    risk = (
        "Low"
        if prediction == 1
        else "High"
    )

    lead_priority = (
        "High"
        if probability > 0.80
        else "Medium"
        if probability > 0.50
        else "Low"
    )

    save_prediction(
        db,
        request,
        risk,
        float(probability),
        lead_priority
    )

    return LoanPredictionResponse(
        risk=risk,
        approval_probability=round(
            float(probability),
            2
        ),
        lead_priority=lead_priority
    )

@router.get("/history")
def get_history(
    db: Session = Depends(get_db)
):
    predictions = db.query(
        Prediction
    ).all()

    result = []

    for p in predictions:
        result.append(
            {
                "id": p.id,
                "gender": p.gender,
                "married": p.married,
                "dependents": p.dependents,
                "education": p.education,
                "self_employed": p.self_employed,
                "applicant_income": p.applicant_income,
                "coapplicant_income": p.coapplicant_income,
                "loan_amount": p.loan_amount,
                "loan_amount_term": p.loan_amount_term,
                "credit_history": p.credit_history,
                "property_area": p.property_area,
                "risk": p.risk,
                "approval_probability": p.approval_probability,
                "lead_priority": p.lead_priority
            }
        )

    return result
