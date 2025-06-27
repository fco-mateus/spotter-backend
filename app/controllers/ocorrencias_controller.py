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
    # Lê o conteúdo da imagem
    conteudo = await file.read()
    nome_arquivo = f"{uuid.uuid4()}.jpg"

    # Simulação de upload no S3
    url_imagem = f"https://bucket-ficticio.s3.amazonaws.com/{nome_arquivo}"

    # Quando tiver o bucket real, você pode usar:
    # import boto3
    # s3 = boto3.client('s3')
    # bucket_name = 'nome-do-seu-bucket'
    # s3.put_object(Bucket=bucket_name, Key=nome_arquivo, Body=conteudo, ContentType=file.content_type)
    # url_imagem = f"https://{bucket_name}.s3.amazonaws.com/{nome_arquivo}"

    nova_ocorrencia = ocorrencias_service.criar_ocorrencia(db, placa, motivo, url_imagem)

    return {"mensagem": "Ocorrência registrada com sucesso", "ocorrencia": nova_ocorrencia}

@router.get("/", response_model=List[OcorrenciaResponse])
def listar_ocorrencias(db: Session = Depends(get_db)):
    return ocorrencias_service.listar_ocorrencias(db)

@router.get("/{ocorrencia_id}", response_model=OcorrenciaResponse)
def buscar_ocorrencia(ocorrencia_id: str, db: Session = Depends(get_db)):
    return ocorrencias_service.buscar_ocorrencia_por_id(db, ocorrencia_id)