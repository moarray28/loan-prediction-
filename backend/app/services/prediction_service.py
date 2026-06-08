from app.db.models import Prediction


def save_prediction(
    db,
    request,
    risk,
    probability,
    priority
):
    prediction = Prediction(
        income=request.income,
        loan_amount=request.loan_amount,
        credit_score=request.credit_score,
        risk=risk,
        approval_probability=probability,
        lead_priority=priority
    )

    db.add(prediction)
    db.commit()
    db.refresh(prediction)

    return prediction