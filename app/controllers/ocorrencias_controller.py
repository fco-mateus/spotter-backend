from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.ocorrencia_schema import OcorrenciaCreate
from app.services import ocorrencias_service
from app.config.database import get_db

router = APIRouter(prefix="/ocorrencias", tags=["Ocorrências"])

@router.post("/")
def criar(ocorrencia: OcorrenciaCreate, db: Session = Depends(get_db)):
    return ocorrencias_service.criar_ocorrencia(db, ocorrencia)
