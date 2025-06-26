from sqlalchemy import Column, String, DateTime, Text, ForeignKey, Enum
from sqlalchemy.orm import relationship, declarative_base
import datetime
import uuid
import enum

Base = declarative_base()

# Enum para tipo de veículo
class TipoVeiculo(str, enum.Enum):
    carro = "carro"
    moto = "moto"

# ============================
# Tabela Funcionário
# ============================
class Funcionario(Base):
    __tablename__ = "funcionarios"

    matricula = Column(String, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    cpf = Column(String(11), unique=True, nullable=False)
    telefone = Column(String(13))

    # Relacionamento com veículos
    veiculos = relationship("Veiculo", back_populates="funcionario")

# ============================
# Tabela Veículos
# ============================
class Veiculo(Base):
    __tablename__ = "veiculos"

    placa = Column(String(7), primary_key=True, index=True)
    modelo = Column(String, nullable=False)
    cor = Column(String, nullable=False)
    tipo_veiculo = Column(Enum(TipoVeiculo), nullable=False)
    marca = Column(String, nullable=False)
    matricula = Column(String, ForeignKey("funcionarios.matricula"))

    # Relacionamento com funcionário
    funcionario = relationship("Funcionario", back_populates="veiculos")
    # Relacionamento com ocorrências
    ocorrencias = relationship("Ocorrencia", back_populates="veiculo")

# ============================
# Tabela Ocorrências
# ============================
class Ocorrencia(Base):
    __tablename__ = "ocorrencias"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    criado_em = Column(DateTime, default=datetime.datetime.utcnow)
    motivo = Column(Text, nullable=False)
    foto = Column(String, nullable=False)  # Link no S3
    placa = Column(String, ForeignKey("veiculos.placa"))

    # Relacionamento com veículo
    veiculo = relationship("Veiculo", back_populates="ocorrencias")
