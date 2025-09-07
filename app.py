from flask import Flask
from flask import request
from flask import render_template
import json
import uuid

app = Flask(__name__)

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

        #Abaixo abre o arquivo json e carrega os dados ja existentes
        try:
            with open(json_caminho, "r") as arquivo:
                pessoas_cadastradas = json.load(arquivo)
        except (FileNotFoundError, json.JSONDecodeError):
            pessoas_cadastradas = {}

        #Abaixo gera um ID unico para cada usuario
        id = str(uuid.uuid4())
        pessoas_cadastradas[id] = {
            "nome": nome,
            "email": email,
            "mensagem": mensagem
        }

        #Abaixo abre o arquivo json e salva os novos dados
        with open(json_caminho, "w") as arquivo:
             json.dump(pessoas_cadastradas, arquivo, indent=4)

        return f"Usuario {nome} registrado con exito"

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)