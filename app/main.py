from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"mensagem": "API de OCR de estacionamento está funcionando!"}
