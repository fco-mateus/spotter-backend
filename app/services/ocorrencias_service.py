from app.repositories import ocorrencias_repository
from fastapi import HTTPException
from datetime import datetime
from app.utils.convert_base64 import converter_imagem_para_base64_formatado
import httpx
import uuid

def criar_ocorrencia(db, placa, motivo, url_imagem):
    dados_ocorrencia = {
        "id": str(uuid.uuid4()),
        "criado_em": datetime.now(),
        "motivo": motivo,
        "foto": url_imagem,
        "placa": placa
    }
    return ocorrencias_repository.inserir_ocorrencia(db, dados_ocorrencia)

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