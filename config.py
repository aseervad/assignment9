import os

class Config:
    # Database configuration
    SQLALCHEMY_DATABASE_URI = "sqlite:///ielts_app.db"  # SQLite for simplicity
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key_for_dev")