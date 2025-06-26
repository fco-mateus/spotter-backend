from pydantic import BaseModel
from datetime import datetime

class OcorrenciaResponse(BaseModel):
    id: str
    criado_em: datetime
    motivo: str
    foto: str  # URL da imagem
    placa: str

    class Config:
        orm_mode = True
