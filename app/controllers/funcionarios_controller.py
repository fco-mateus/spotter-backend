from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.funcionario_schema import FuncionarioCreate, FuncionarioOut
from app.services import funcionarios_service
from app.config.database import get_db

router = APIRouter(prefix="/funcionarios", tags=["Funcionários"])

@router.post("/", response_model=FuncionarioOut)
def criar(funcionario: FuncionarioCreate, db: Session = Depends(get_db)):
    return funcionarios_service.criar_funcionario(db, funcionario)

@router.get("/", response_model=list[FuncionarioOut])
def listar(db: Session = Depends(get_db)):
    return funcionarios_service.buscar_funcionarios(db)
