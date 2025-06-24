from pydantic import BaseModel

class OcorrenciaCreate(BaseModel):
    motivo: str
    foto: str
    placa: str
