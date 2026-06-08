from pydantic import BaseModel


class LoanPredictionRequest(BaseModel):
    income: float
    loan_amount: float
    credit_score: int
    employment_years: int
