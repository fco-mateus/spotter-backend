from app.entities.models import Ocorrencia

def inserir_ocorrencia(db, placa, motivo, url_imagem):
    nova_ocorrencia = Ocorrencia(
        placa=placa,
        motivo=motivo,
        foto=url_imagem
    )
    db.add(nova_ocorrencia)
    db.commit()
    db.refresh(nova_ocorrencia)
    return nova_ocorrencia

def listar_ocorrencias(db):
    return db.query(Ocorrencia).all()

def buscar_ocorrencia_por_id(db, ocorrencia_id):
    return db.query(Ocorrencia).filter(Ocorrencia.id == ocorrencia_id).first()