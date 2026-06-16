import os

class Settings:
    PROJECT_NAME: str = "Makoni AI App"
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://user:password@db:5432/makoni_ai")

settings = Settings()
