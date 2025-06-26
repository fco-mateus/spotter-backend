from app.repositories import ocorrencias_repository
from fastapi import HTTPException
from datetime import datetime
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