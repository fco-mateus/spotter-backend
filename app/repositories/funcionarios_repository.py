from sqlalchemy.orm import Session
from app.entities.models import Funcionario

def inserir_funcionario(db: Session, funcionario_data):
    funcionario = Funcionario(**funcionario_data.dict())
    db.add(funcionario)
    db.commit()
    db.refresh(funcionario)
    return funcionario

def listar_funcionarios(db: Session):
    return db.query(Funcionario).all()

def buscar_funcionario_por_matricula(db: Session, matricula: str):
    return db.query(Funcionario).filter(Funcionario.matricula == matricula).first()

def atualizar_funcionario(db: Session, matricula: str, funcionario_data):
    funcionario = buscar_funcionario_por_matricula(db, matricula)
    if funcionario:
        for key, value in funcionario_data.dict().items():
            setattr(funcionario, key, value)
        db.commit()
        db.refresh(funcionario)
    return funcionario

def deletar_funcionario(db: Session, matricula: str):
    funcionario = buscar_funcionario_por_matricula(db, matricula)
    if funcionario:
        db.delete(funcionario)
        db.commit()
    return funcionario
