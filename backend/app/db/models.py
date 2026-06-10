# backend/app/db/models.py

from sqlalchemy import Column
from sqlalchemy import Float
from sqlalchemy import Integer
from sqlalchemy import String

from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True)

    gender = Column(String)
    married = Column(String)
    dependents = Column(String)
    education = Column(String)
    self_employed = Column(String)

    applicant_income = Column(Float)
    coapplicant_income = Column(Float)

    loan_amount = Column(Float)
    loan_amount_term = Column(Float)

    credit_history = Column(Float)

    property_area = Column(String)

    prediction = Column(String)
    approval_probability = Column(Float)