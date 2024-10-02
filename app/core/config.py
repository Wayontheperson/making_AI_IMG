# app/core/config.py
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # PostgreSQL 데이터베이스 URL 설정
    DATABASE_URL: str = "postgresql://postgres:postgres@211.168.94.202:5432/fastapidb"

    class Config:
        env_file = ".env"  # 환경 변수를 .env 파일에서 로드


settings = Settings()
