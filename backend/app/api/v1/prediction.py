from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.models.request import LoanPredictionRequest
from app.models.response import LoanPredictionResponse

from app.db.dependencies import get_db
from app.services.prediction_service import save_prediction

router = APIRouter()
router = APIRouter()


@router.get("/")
def prediction_root():
    return {"message": "Prediction API V1"}


@router.post(
    "/",
    response_model=LoanPredictionResponse
)

@router.get("/history")
def get_history(
    db: Session = Depends(get_db)
):
    predictions = db.query(Prediction).all()

    return predictions

def predict(
    request: LoanPredictionRequest,
    db: Session = Depends(get_db)
):
    save_prediction(
        db,
        request,
        "Low",
        0.85,
        "High"
    )

    return LoanPredictionResponse(
        risk="Low",
        approval_probability=0.85,
        lead_priority="High"
    )
