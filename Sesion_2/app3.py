from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    nombre_curso = "Desarrollo web con Flask"
    return render_template("index2.html", curso = nombre_curso) # pasando la variable a la plantilla

@app.route("/saludo")
def saludo():
    return "Hola desde la ruta /saludo"

@app.route("/info")
def info():
    curso = "Desarrollo web con Flask"
    docente = "Jordi Pozo"
    horas = 40
    return render_template(
        "info.html",
        curso=curso,
        docente=docente,
        horas=horas
    )

if __name__ == "__main__":
    app.run(debug=True)