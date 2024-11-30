import sqlite3

# Conexão com o banco
conn = sqlite3.connect("crm.db")
cursor = conn.cursor()

# Criação da tabela de clientes
cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    telefone TEXT,
    email TEXT,
    tipo TEXT
)
""")

# Criação da tabela de registros offline
cursor.execute("""
CREATE TABLE IF NOT EXISTS registros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER,
    servico TEXT,
    data TEXT,
    sincronizado INTEGER DEFAULT 0,
    FOREIGN KEY(cliente_id) REFERENCES clientes(id)
)
""")

conn.commit()
conn.close()
print("Banco de dados configurado.")
