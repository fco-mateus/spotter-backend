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

def buscar_veiculo_por_placa(db: Session, placa: str):
    return db.query(Veiculo).filter(Veiculo.placa == placa).first()

def atualizar_veiculo(db: Session, placa: str, veiculo_data):
    veiculo = buscar_veiculo_por_placa(db, placa)
    if veiculo:
        for key, value in veiculo_data.dict().items():
            setattr(veiculo, key, value)
        db.commit()
        db.refresh(veiculo)
    return veiculo

def deletar_veiculo(db: Session, placa: str):
    veiculo = buscar_veiculo_por_placa(db, placa)
    if veiculo:
        db.delete(veiculo)
        db.commit()
    return veiculo
