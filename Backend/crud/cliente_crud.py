import sqlite3
from models.cliente import Cliente

def get_clientes():
    conn = sqlite3.connect('crm.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    conn.close()
    return [Cliente(id=cliente[0], nome=cliente[1], email=cliente[2], telefone=cliente[3], endereco=cliente[4], tipo=cliente[5]) for cliente in clientes]
