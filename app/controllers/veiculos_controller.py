from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.veiculo_schema import VeiculoCreate, VeiculoOut
from app.services import veiculos_service
from app.config.database import get_db

router = APIRouter(prefix="/veiculos", tags=["Veículos"])

@router.post("/", response_model=VeiculoOut)
def criar(veiculo: VeiculoCreate, db: Session = Depends(get_db)):
    return veiculos_service.criar_veiculo(db, veiculo)

@router.get("/", response_model=list[VeiculoOut])
def listar(db: Session = Depends(get_db)):
    return veiculos_service.buscar_veiculos(db)
