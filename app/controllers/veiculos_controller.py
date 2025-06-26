from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from app.schemas.veiculo_schema import VeiculoCreate, VeiculoUpdate, VeiculoOut
from app.services import veiculos_service
from app.config.database import get_db
from app.utils.file_reader import ler_arquivo

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

@router.post("/importar")
def importar_veiculos(file: UploadFile = File(...), db: Session = Depends(get_db)):
    df = ler_arquivo(file)

    colunas_esperadas = {'placa', 'modelo', 'cor', 'tipo_veiculo', 'marca', 'matricula'}
    if not colunas_esperadas.issubset(df.columns):
        raise HTTPException(status_code=400, detail=f"Arquivo inválido. As colunas obrigatórias são: {colunas_esperadas}")

    for _, row in df.iterrows():
        veiculo_data = VeiculoCreate(
            placa=str(row['placa']),
            modelo=str(row['modelo']),
            cor=str(row['cor']),
            tipo_veiculo=row['tipo_veiculo'],  # Enum já aceita string diretamente
            marca=str(row['marca']),
            matricula=str(row['matricula'])
        )
        veiculos_service.criar_veiculo(db, veiculo_data)

    return {"mensagem": "Veículos importados com sucesso", "quantidade": len(df)}
