import os
from dotenv import load_dotenv

load_dotenv()  # 讀取 .env 檔案

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "default-secret"
    if os.getenv("FLASK_ENV") == "production":
        SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    else:
        SQLALCHEMY_DATABASE_URI = 'sqlite:///local.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = "uploads"
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','zip'}

