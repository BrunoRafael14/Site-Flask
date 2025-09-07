from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route("/hello")
def hello_world():
	return "Hello World"

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)