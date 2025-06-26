from fastapi import FastAPI
from app.controllers import ocorrencias_controller
from app.controllers import veiculos_controller
from app.controllers import funcionarios_controller

app = FastAPI()

# Garante que as tabelas serão criadas no banco
# from app.entities.models import Base
# from app.config.database import engine
# Base.metadata.create_all(bind=engine)

app.include_router(ocorrencias_controller.router)
app.include_router(veiculos_controller.router)
app.include_router(funcionarios_controller.router)
