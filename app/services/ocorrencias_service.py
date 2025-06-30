from app.repositories import ocorrencias_repository
from fastapi import HTTPException
from datetime import datetime
from app.utils.convert_base64 import converter_imagem_para_base64_formatado
import boto3
import httpx
import uuid
import os

BUCKET_NAME = os.getenv("BUCKET_NAME")
if not BUCKET_NAME:
    raise Exception("BUCKET_NAME não configurado!")

async def criar_ocorrencia(db, placa, motivo, file):
    conteudo = await file.read()
    nome_arquivo = f"{uuid.uuid4()}.jpg"

    s3 = boto3.client('s3')

    try:
        s3.put_object(
            Bucket=BUCKET_NAME,
            Key=nome_arquivo,
            Body=conteudo,
            ContentType=file.content_type
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao enviar imagem para S3: {str(e)}")

    url_imagem = f"https://{BUCKET_NAME}.s3.amazonaws.com/{nome_arquivo}"

    nova_ocorrencia = ocorrencias_repository.inserir_ocorrencia(db, placa, motivo, url_imagem)
    return nova_ocorrencia

def listar_ocorrencias(db):
    return ocorrencias_repository.listar_ocorrencias(db)

def buscar_ocorrencia_por_id(db, ocorrencia_id):
    ocorrencia = ocorrencias_repository.buscar_ocorrencia_por_id(db, ocorrencia_id)
    if not ocorrencia:
        raise HTTPException(status_code=404, detail="Ocorrência não encontrada")
    return ocorrencia

async def enviar_para_ocr(file, ocr_engine):
    conteudo = await file.read()
    mime_type = file.content_type
    imagem_base64_formatada = converter_imagem_para_base64_formatado(conteudo, mime_type)
    ocr_payload = {"image": imagem_base64_formatada}

    url = f"http://ocr:5000/ocr/{ocr_engine}"

    async with httpx.AsyncClient(timeout=120.0) as client:
        response = await client.post(url, json=ocr_payload)
        data = response.json()

        success = bool(data.get("success", False))
        if success:
            return data.get("text")
        else:
            return None