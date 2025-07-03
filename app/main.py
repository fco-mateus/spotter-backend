from fastapi import FastAPI
from app.controllers import ocorrencias_controller
from app.controllers import veiculos_controller
from app.controllers import funcionarios_controller
from app.controllers import health_check_controller

app = FastAPI()

app.inclue_router(health_check_controller.router, prefix="/api")
app.include_router(ocorrencias_controller.router, prefix="/api")
app.include_router(veiculos_controller.router, prefix="/api")
app.include_router(funcionarios_controller.router, prefix="/api")
