from pydantic import BaseModel


class UsuarioBase(BaseModel):
    nome: str
    email: str


class UsuarioCreate(UsuarioBase):
    pass


class Usuario(UsuarioBase):
    id: int

    class Config:
        from_attributes = True


class TarefaBase(BaseModel):
    titulo: str
    descricao: str
    usuario_id: int

class TarefaCreate(TarefaBase):
    pass

class Tarefa(TarefaBase):
    id:int

class Config:
    from_attributes = True

