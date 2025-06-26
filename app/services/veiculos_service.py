from app.repositories import veiculos_repository

def criar_veiculo(db, veiculo_data):
    return veiculos_repository.inserir_veiculo(db, veiculo_data)

def buscar_veiculos(db):
    return veiculos_repository.listar_veiculos(db)

def buscar_veiculo(db, placa: str):
    return veiculos_repository.buscar_veiculo_por_placa(db, placa)

def atualizar_veiculo(db, placa: str, veiculo_data):
    return veiculos_repository.atualizar_veiculo(db, placa, veiculo_data)

def deletar_veiculo(db, placa: str):
    return veiculos_repository.deletar_veiculo(db, placa)
