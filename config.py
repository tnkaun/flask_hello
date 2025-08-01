import os
from dotenv import load_dotenv

load_dotenv()  # 讀取 .env 檔案

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "default-secret"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = "uploads"

