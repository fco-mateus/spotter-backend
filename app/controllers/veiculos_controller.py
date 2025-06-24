from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.veiculo_schema import VeiculoCreate, VeiculoUpdate, VeiculoOut
from app.services import veiculos_service
from app.config.database import get_db

router = APIRouter(prefix="/veiculos", tags=["Veículos"])

@router.post("/", response_model=VeiculoOut)
def criar(veiculo: VeiculoCreate, db: Session = Depends(get_db)):
    return veiculos_service.criar_veiculo(db, veiculo)

@router.get("/", response_model=list[VeiculoOut])
def listar(db: Session = Depends(get_db)):
    return veiculos_service.buscar_veiculos(db)

@router.get("/{placa}", response_model=VeiculoOut)
def buscar(placa: str, db: Session = Depends(get_db)):
    veiculo = veiculos_service.buscar_veiculo(db, placa)
    if not veiculo:
        raise HTTPException(status_code=404, detail="Veículo não encontrado")
    return veiculo

@router.put("/{placa}", response_model=VeiculoOut)
def atualizar(placa: str, veiculo: VeiculoUpdate, db: Session = Depends(get_db)):
    veiculo_atualizado = veiculos_service.atualizar_veiculo(db, placa, veiculo)
    if not veiculo_atualizado:
        raise HTTPException(status_code=404, detail="Veículo não encontrado")
    return veiculo_atualizado

@router.delete("/{placa}")
def deletar(placa: str, db: Session = Depends(get_db)):
    veiculo_deletado = veiculos_service.deletar_veiculo(db, placa)
    if not veiculo_deletado:
        raise HTTPException(status_code=404, detail="Veículo não encontrado")
    return {"mensagem": "Veículo deletado com sucesso"}
