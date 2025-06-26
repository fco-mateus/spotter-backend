from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

# Para aplicação na máquina: 
# DATABASE_URL = DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/spotter"

# Para container:
# host.docker.internal é o endereço para acessar o host local a partir de dentro do container no Docker Desktop (Windows, Mac e WSL2 no Linux).
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@host.docker.internal:5432/spotter_db")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
