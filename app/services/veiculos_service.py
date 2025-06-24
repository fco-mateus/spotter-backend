from app.repositories import veiculos_repository

def criar_veiculo(db, veiculo_data):
    return veiculos_repository.inserir_veiculo(db, veiculo_data)

def buscar_veiculos(db):
    return veiculos_repository.listar_veiculos(db)
