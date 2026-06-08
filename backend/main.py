from fastapi import FastAPI

from app.api.v1.prediction import router
from app.db.database import engine
from app.db.models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Loan Risk Prediction API",
    version="1.0.0"
)


@app.get("/health")
def health_check():
    return {"status": "healthy"}


app.include_router(
    router,
    prefix="/api/v1/predict",
    tags=["Prediction"]
)