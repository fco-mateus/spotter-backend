from pydantic import BaseModel

class FuncionarioCreate(BaseModel):
    matricula: str
    nome: str
    cpf: str
    telefone: str

class FuncionarioOut(BaseModel):
    matricula: str
    nome: str
    cpf: str
    telefone: str

    class Config:
        orm_mode = True
