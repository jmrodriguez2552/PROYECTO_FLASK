from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Pagina principal"


@app.route("/saludo")
def saludo():
    return "Hola desde la ruta /saludo"


@app.route("/despedida")
def despedida():
    return "Adios desde la ruta /despedida"


@app.route("/saluda/<nombre>")
def saluda_nombre(nombre):
    return f"Encantado de conocerte, {nombre}"


if __name__ == "__main__":
    app.run(debug=True)