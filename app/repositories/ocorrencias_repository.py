from sqlalchemy.orm import Session
from app.entities.models import Ocorrencia

def inserir_ocorrencia(db: Session, dados):
    ocorrencia = Ocorrencia(**dados.dict())
    db.add(ocorrencia)
    db.commit()
    db.refresh(ocorrencia)
    return ocorrencia
