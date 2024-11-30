from fastapi import FastAPI, HTTPException
import sqlite3
from fastapi.middleware.cors import CORSMiddleware

# Crie a instância da aplicação FastAPI
app = FastAPI()

# Adicione o middleware de CORS para permitir que o frontend acesse a API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Permitir requisições do frontend React
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos os métodos HTTP
    allow_headers=["*"],  # Permitir todos os cabeçalhos
)

# Função para conectar ao banco de dados
def conectar_banco():
    return sqlite3.connect("crm.db")

# Rota para listar clientes
@app.get("/clientes")
def listar_clientes():
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    conn.close()

    # Convertendo os resultados para um formato mais amigável
    clientes_list = [{"id": cliente[0], "nome": cliente[1], "telefone": cliente[2], "email": cliente[3], "tipo": cliente[4]} for cliente in clientes]
    
    return {"clientes": clientes_list}

# Rota para adicionar um cliente
@app.post("/clientes")
def adicionar_cliente(cliente: dict):
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute(""" 
    INSERT INTO clientes (nome, telefone, email, tipo) 
    VALUES (?, ?, ?, ?)
    """, (cliente["nome"], cliente["telefone"], cliente["email"], cliente["tipo"]))
    conn.commit()
    conn.close()
    return {"message": "Cliente adicionado com sucesso!"}
