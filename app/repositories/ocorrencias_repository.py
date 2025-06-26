from app.entities.models import Ocorrencia

def inserir_ocorrencia(db, dados_ocorrencia):
    ocorrencia = Ocorrencia(**dados_ocorrencia)
    db.add(ocorrencia)
    db.commit()
    db.refresh(ocorrencia)
    return ocorrencia

def listar_ocorrencias(db):
    return db.query(Ocorrencia).all()

def buscar_ocorrencia_por_id(db, ocorrencia_id):
    return db.query(Ocorrencia).filter(Ocorrencia.id == ocorrencia_id).first()