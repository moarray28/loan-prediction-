from pydantic import BaseModel


class LoanPredictionResponse(BaseModel):
    risk: str
    approval_probability: float
    lead_priority: str
