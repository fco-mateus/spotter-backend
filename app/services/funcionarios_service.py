from app.repositories import funcionarios_repository

def criar_funcionario(db, funcionario_data):
    return funcionarios_repository.inserir_funcionario(db, funcionario_data)

def buscar_funcionarios(db):
    return funcionarios_repository.listar_funcionarios(db)

def buscar_funcionario(db, matricula: str):
    return funcionarios_repository.buscar_funcionario_por_matricula(db, matricula)

def atualizar_funcionario(db, matricula: str, funcionario_data):
    return funcionarios_repository.atualizar_funcionario(db, matricula, funcionario_data)

def deletar_funcionario(db, matricula: str):
    return funcionarios_repository.deletar_funcionario(db, matricula)
