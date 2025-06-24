from sqlalchemy.orm import Session
from app.entities.models import Veiculo

def inserir_veiculo(db: Session, veiculo_data):
    veiculo = Veiculo(**veiculo_data.dict())
    db.add(veiculo)
    db.commit()
    db.refresh(veiculo)
    return veiculo

def listar_veiculos(db: Session):
    return db.query(Veiculo).all()
