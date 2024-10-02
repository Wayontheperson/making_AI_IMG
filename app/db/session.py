# app/db/session.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.config import settings


# SQLAlchemy 데이터베이스 엔진 생성
# psql 이랑 연결
engine = create_engine(settings.DATABASE_URL, pool_pre_ping=True)

# 세션 로컬을 정의 (SessionLocal 클래스는 데이터베이스와의 세션을 관리)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# 종속성 주입용 데이터베이스 세션 함수
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
