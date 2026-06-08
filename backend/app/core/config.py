import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    APP_NAME = os.getenv("APP_NAME", "Loan Risk Prediction API")
    VERSION = os.getenv("VERSION", "1.0.0")


settings = Settings()
