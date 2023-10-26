from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.sql.expression import select

class Base(DeclarativeBase):
    pass


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:vBst&Ebb5hw@localhost:3306/escritorio'

db = SQLAlchemy(model_class=Base)
db.init_app(app)


class Pessoa(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String, nullable=False)
    cliente: Mapped[int] = mapped_column(Integer, nullable=False)
    cpf_cnpj: Mapped[str] = mapped_column(String, nullable=False)
    endereco: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String)


class Processo(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    advogado_id: Mapped[int] = mapped_column(Integer)
    cliente_id: Mapped[int] = mapped_column(Integer)
    numero_processo: Mapped[int] = mapped_column(Integer)
    proximo_prazo: Mapped[str] = mapped_column(String)
    arquivo: Mapped[int] = mapped_column(Integer)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/buscar_artigos/")
def buscar_artigos():
    artigos = Processo.query.all()
    return render_template("lista_artigos.html", artigos=artigos)
