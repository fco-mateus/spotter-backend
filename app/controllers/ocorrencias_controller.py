from fastapi import APIRouter, UploadFile, File, HTTPException, Depends, Form
from app.schemas.ocorrencia_schema import OcorrenciaResponse
from sqlalchemy.orm import Session
from app.services import ocorrencias_service
from app.config.database import get_db
from typing import List
from app.utils.convert_base64 import converter_imagem_para_base64_formatado
import uuid


router = APIRouter(prefix="/ocorrencias", tags=["Ocorrencias"])

@router.post("/ocr/easyocr")
async def processar_ocr(file: UploadFile = File(...)):
    placa = await ocorrencias_service.enviar_para_ocr(file, "easyocr")
    return {"placa_detectada": placa}

@router.post("/ocr/pytesseract")
async def processar_ocr(file: UploadFile = File(...)):
    placa = await ocorrencias_service.enviar_para_ocr(file, "pytesseract")
    return {"placa_detectada": placa}

@router.post("/")
async def criar_ocorrencia(
    file: UploadFile = File(...),
    placa: str = Form(...),
    motivo: str = Form(...),
    db: Session = Depends(get_db)
):
    nova_ocorrencia = await ocorrencias_service.criar_ocorrencia(db, placa, motivo, file)
    return {"mensagem": "Ocorrência registrada com sucesso", "ocorrencia": nova_ocorrencia}

@router.get("/", response_model=List[OcorrenciaResponse])
def listar_ocorrencias(db: Session = Depends(get_db)):
    return ocorrencias_service.listar_ocorrencias(db)

@router.get("/{ocorrencia_id}", response_model=OcorrenciaResponse)
def buscar_ocorrencia(ocorrencia_id: str, db: Session = Depends(get_db)):
    return ocorrencias_service.buscar_ocorrencia_por_id(db, ocorrencia_id)