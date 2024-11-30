from pydantic import BaseModel

class Cliente(BaseModel):
    id: int
    nome: str
    email: str
    telefone: str
    endereco: str
    tipo: str
