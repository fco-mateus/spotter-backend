from pydantic import BaseModel
from enum import Enum

class TipoVeiculo(str, Enum):
    carro = "carro"
    moto = "moto"

class VeiculoCreate(BaseModel):
    placa: str
    modelo: str
    cor: str
    tipo_veiculo: TipoVeiculo
    marca: str
    matricula: str

class VeiculoOut(BaseModel):
    placa: str
    modelo: str
    cor: str

    class Config:
        orm_mode = True
