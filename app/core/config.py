import os
from typing import List

from dotenv import load_dotenv
from pydantic import BaseSettings, AnyHttpUrl

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
load_dotenv(os.path.join(BASE_DIR, ".env"))


class Settings(BaseSettings):
    API_PREFIX = '/api/v1'
    PROJECT_NAME = os.getenv('PROJECT_NAME', 'Money Lover')
    SECRET_KEY = os.getenv('SECRET_KEY', '')
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = ["http://localhost:9000"]
    DATABASE_URL = os.getenv('SQL_DATABASE_URL', '')


settings = Settings()
