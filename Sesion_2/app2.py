from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    nombre_curso = "Desarrollo web con Flask"
    return render_template("index2.html", curso = nombre_curso) # pasando la variable a la plantilla

@app.route("/saludo")
def saludo():
    return "Hola desde la ruta /saludo"

if __name__ == "__main__":
    app.run(debug=True)