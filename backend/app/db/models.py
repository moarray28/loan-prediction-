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

    income = Column(Float)

    loan_amount = Column(Float)

    credit_score = Column(Integer)

    risk = Column(String)

    approval_probability = Column(Float)

    lead_priority = Column(String)
