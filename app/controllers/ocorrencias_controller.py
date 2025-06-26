from fastapi import APIRouter, UploadFile, File, HTTPException, Depends, Form
from app.schemas.ocorrencia_schema import OcorrenciaResponse
from sqlalchemy.orm import Session
from app.services import ocorrencias_service
from app.config.database import get_db
from typing import List
import uuid
import base64
import httpx

router = APIRouter(prefix="/ocorrencias", tags=["Ocorrencias"])

@router.post("/ocr")
async def processar_ocr(file: UploadFile = File(...)):
    # Lê o arquivo e converte para base64
    conteudo = await file.read()
    imagem_base64 = base64.b64encode(conteudo).decode('utf-8')

    # Mock da chamada ao OCR (simulando)
    ocr_payload = {"imagem_base64": imagem_base64}

    # Como o OCR ainda não existe, simule a resposta
    # Quando tiver a API pronta, você pode fazer:
    # async with httpx.AsyncClient() as client:
    #     response = await client.post("http://ocr-server/endpoint", json=ocr_payload)
    #     placa = response.json().get("placa")

    # Simulação de resposta
    placa = "ABC1234"

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