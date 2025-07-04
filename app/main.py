from fastapi import FastAPI
from app.controllers import ocorrencias_controller
from app.controllers import veiculos_controller
from app.controllers import funcionarios_controller

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ocorrencias_controller.router)
app.include_router(veiculos_controller.router)
app.include_router(funcionarios_controller.router)
