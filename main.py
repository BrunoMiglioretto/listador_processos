from flask import Flask, render_template, request
from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from typing import Any
from sqlalchemy.orm import DeclarativeBase

# SQLAlchemy
instance = f"mysql+pymysql://root:vBst&Ebb5hw@localhost:3306/escritorio"

engine = create_engine(url=instance, echo=True)
session = Session(bind=engine, autocommit=False, autoflush=True)


class Base(DeclarativeBase):
    def __init__(self, **kw: Any):
        super().__init__(**kw)


class Pessoa(Base):
    __tablename__ = "pessoas"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String, nullable=False)
    cliente: Mapped[int] = mapped_column(Integer, nullable=False)
    cpf_cnpj: Mapped[str] = mapped_column(String, nullable=False)
    endereco: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String)


class Processo(Base):
    __tablename__ = "processos"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    advogado_id: Mapped[int] = mapped_column(Integer)
    cliente_id: Mapped[int] = mapped_column(Integer)
    numero_processo: Mapped[int] = mapped_column(Integer)
    proximo_prazo: Mapped[str] = mapped_column(String)
    arquivo: Mapped[int] = mapped_column(Integer)


# Flask
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/lista_processo/")
def lista_processo():
    processos = session.query(
        Processo,
        Processo.advogado_id,
        Processo.cliente_id,
        Processo.numero_processo,
        Processo.proximo_prazo,
        Processo.arquivo,
    ).all()

    return render_template("lista_processos.html", processos=processos)
