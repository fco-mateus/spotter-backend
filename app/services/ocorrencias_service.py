from app.repositories import ocorrencias_repository

def criar_ocorrencia(db, dados):
    return ocorrencias_repository.inserir_ocorrencia(db, dados)
