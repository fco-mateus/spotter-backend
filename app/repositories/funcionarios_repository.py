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
