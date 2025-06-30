from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
if not DATABASE_PASSWORD:
    raise Exception("DATABASE_PASSWORD não configurada!")

DATABASE_ENDPOINT = os.getenv("DATABASE_ENDPOINT")
if not DATABASE_ENDPOINT:
    raise Exception("DATABASE_ENDPOINT não configurado!")

DATABASE_URL = f"postgresql://postgres:{DATABASE_PASSWORD}@{DATABASE_ENDPOINT}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
