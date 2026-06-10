from app.db.models import Prediction


def save_prediction(
    db,
    request,
    risk,
    probability,
    priority
):
    prediction = Prediction(
        gender=request.Gender,
        married=request.Married,
        dependents=request.Dependents,
        education=request.Education,
        self_employed=request.Self_Employed,

        applicant_income=request.ApplicantIncome,
        coapplicant_income=request.CoapplicantIncome,

        loan_amount=request.LoanAmount,
        loan_amount_term=request.Loan_Amount_Term,

        credit_history=request.Credit_History,

        property_area=request.Property_Area,

        risk=risk,
        approval_probability=probability,
        lead_priority=priority
    )

    db.add(prediction)
    db.commit()
    db.refresh(prediction)

    return prediction
