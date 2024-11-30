# app/db.py ou backend/db.py
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import QueuePool

# URL do banco de dados (SQLite ou outro banco, como PostgreSQL)
DATABASE_URL = "sqlite:///./crm.db"  # Ou outra URL se for outro banco como PostgreSQL

# Criando o engine com pooling
engine = create_engine(
    DATABASE_URL,
    poolclass=QueuePool,  # Usando QueuePool para pooling de conexões
    pool_size=5,  # Defina o tamanho do pool
    max_overflow=10  # Número máximo de conexões extras
)

# Base para os modelos
Base = declarative_base()

# Criando a sessão
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Função para criar as tabelas
def init_db():
    Base.metadata.create_all(bind=engine)
