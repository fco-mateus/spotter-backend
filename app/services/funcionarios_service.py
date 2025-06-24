from app.repositories import funcionarios_repository

def criar_funcionario(db, funcionario_data):
    return funcionarios_repository.inserir_funcionario(db, funcionario_data)

def buscar_funcionarios(db):
    return funcionarios_repository.listar_funcionarios(db)
