from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

# Para aplicação na máquina: 
# DATABASE_URL = DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/spotter"

# Para aplicação e banco dentro de container:
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@postgres-spotter:5432/spotter")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
