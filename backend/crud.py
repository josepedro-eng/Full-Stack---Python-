from sqlalchemy.orm import Session
import models, schemas

def criar_usuario(db: Session, usuario: schemas.UsuarioCreate):
    db_usuario = models.Usuario(
        nome=usuario.nome,
        email=usuario.email
    )

    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def listar_usuarios(db: Session):
    return db.query(models.Usuario).all()


def deletar_usuario(db, usuario_id: int):
    usuario = db.query(models.Usuario).filter(
        models.Usuario.id == usuario_id
    ).first()

    if usuario:
        db.delete(usuario)
        db.commit()

        return usuario
    
def atualizar_usuario(db, usuario_id: int, usuario_atualizado):
    usuario = db.query(models.Usuario).filter(
        models.Usuario.id == usuario_id
    ).first()

    if usuario:
        usuario.nome = usuario_atualizado.nome
        usuario.email = usuario_atualizado.email

        db.commit()
        db.refresh(usuario)

        return usuario

def buscar_usuario(db, usuario_id: int):
    return db.query(models.Usuario).filter(
        models.Usuario.id == usuario_id
    ).first()


def criar_tarefa(db, tarefa):
    db_tarefa = models.Tarefa(
        titulo=tarefa.titulo,
        descricao=tarefa.descricao,
        usuario_id=tarefa.usuario_id
    )
    db.add(db_tarefa)
    db.commit()
    db.refresh(db_tarefa)
    return db_tarefa

def listar_tarefas(db):
    return db.query(models.Tarefa).all()

def listar_tarefas_por_usuario(db, usuario_id: int):
    return db.query(models.Tarefa).filter(
        models.Tarefa.usuario_id == usuario_id
    ).all()

def deletar_tarefa(db: Session, tarefa_id: int):
    tarefa = db.query(models.Tarefa).filter(models.Tarefa.id == tarefa_id).first()
    if tarefa:
        db.delete(tarefa)
        db.commit()
        return tarefa
    return None