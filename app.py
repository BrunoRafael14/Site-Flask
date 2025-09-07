from flask import Flask
from flask import request
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
#configurando o banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///penguin.db'

#inicializando o banco de dados
db = SQLAlchemy(app)

#criando o banco de dados
with app.app_context():
    db.create_all()

#criando a tabela Pessoa
class Pessoa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    mensagem = db.Column(db.Text, nullable=True)


@app.route("/hello")
def hello_world():
	return "Hello World"

json_caminho = "dados/pessoas.json"

@app.route("/", methods=["GET","POST"])
def form():
    #Abaixo verifica se o metodo é POST para pegar os dados do formulario
    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        mensagem = request.form.get("mensagem")

        #Salvando os dados no banco de dados
        pessoa = Pessoa(nome = nome, email = email, mensagem = mensagem)
        db.session.add(pessoa)
        db.session.commit()

        return f"Usuario {nome} registrado con exito"

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)