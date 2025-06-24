from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.funcionario_schema import FuncionarioCreate, FuncionarioOut, FuncionarioUpdate
from app.services import funcionarios_service
from app.config.database import get_db

router = APIRouter(prefix="/funcionarios", tags=["Funcionários"])

@router.post("/", response_model=FuncionarioOut)
def criar(funcionario: FuncionarioCreate, db: Session = Depends(get_db)):
    return funcionarios_service.criar_funcionario(db, funcionario)

@router.get("/", response_model=list[FuncionarioOut])
def listar(db: Session = Depends(get_db)):
    return funcionarios_service.buscar_funcionarios(db)

@router.get("/{matricula}", response_model=FuncionarioOut)
def buscar(matricula: str, db: Session = Depends(get_db)):
    funcionario = funcionarios_service.buscar_funcionario(db, matricula)
    if not funcionario:
        raise HTTPException(status_code=404, detail="Funcionário não encontrado")
    return funcionario

@router.put("/{matricula}", response_model=FuncionarioOut)
def atualizar(matricula: str, funcionario: FuncionarioUpdate, db: Session = Depends(get_db)):
    funcionario_atualizado = funcionarios_service.atualizar_funcionario(db, matricula, funcionario)
    if not funcionario_atualizado:
        raise HTTPException(status_code=404, detail="Funcionário não encontrado")
    return funcionario_atualizado

@router.delete("/{matricula}")
def deletar(matricula: str, db: Session = Depends(get_db)):
    funcionario_deletado = funcionarios_service.deletar_funcionario(db, matricula)
    if not funcionario_deletado:
        raise HTTPException(status_code=404, detail="Funcionário não encontrado")
    return {"mensagem": "Funcionário deletado com sucesso"}
