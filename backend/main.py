from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import engine, Base, SessionLocal
import models, crud, schemas
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.get("/")
def home():
    return {"mensagem": "API funcionando!"}


@app.post("/usuarios/", response_model=schemas.Usuario)
def criar_usuario(
    usuario: schemas.UsuarioCreate,
    db: Session = Depends(get_db)
):
    return crud.criar_usuario(db, usuario)


@app.get("/usuarios/", response_model=list[schemas.Usuario])
def listar_usuarios(
    db: Session = Depends(get_db)
):
    return crud.listar_usuarios(db)

@app.delete("/usuario/{usuario_id}")
def deletar_usuario(
    usuario_id: int,
    db: Session = Depends(get_db)
):
    return crud.deletar_usuario(db, usuario_id)

@app.put("/usuarios/{usuario_id}", response_model=schemas.Usuario)
def atualizar_usuario(
    usuario_id: int,
    usuario: schemas.UsuarioCreate,
    db: Session = Depends(get_db)
):
    return crud.atualizar_usuario(
        db,
        usuario_id,
        usuario
    )


@app.get("/usuarios/{usuario_id}", response_model=schemas.Usuario)
def buscar_usuario(
    usuario_id: int,
    db: Session = Depends(get_db)
):
    return crud.buscar_usuario(db, usuario_id)

@app.post("/tarefas/", response_model=schemas.Tarefa)
def criar_tarefa(
    tarefa: schemas.TarefaCreate,
    db: Session = Depends(get_db)
):
   return crud.criar_tarefa(db, tarefa)

@app.get("/tarefas/", response_model=list[schemas.Tarefa])
def listar_tarefas(
    db: Session = Depends(get_db)
):
    return crud.listar_tarefas(db)

@app.get("/usuarios/{usuario_id}/tarefas", response_model=list[schemas.Tarefa])
def listar_tarefa_usuario(
    usuario_id: int,
    db: Session = Depends(get_db)
):
    return crud.listar_tarefas_por_usuario(db, usuario_id)

@app.delete("/tarefas/{tarefa_id}")
def deletar_tarefa(tarefa_id: int, db: Session = Depends(get_db)):
    return crud.deletar_tarefa(db, tarefa_id)