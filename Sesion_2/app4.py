from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    nombre_curso = "Desarrollo web con Flask"
    return render_template("index3.html", curso = nombre_curso) # pasando la variable a la plantilla

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
@app.route("/info2")
def info2():
    curso = "Desarrollo web con Flask"
    alumno = "Jose Manuel"
    horas = 40
    return render_template(
        "info2.html",
        curso=curso,
        alumno=alumno,
        horas=horas
    )

@app.route("/alumnos")
def alumnos():
    lista_alumnos = ["Ana", "Carlos", "Marina", "Jordi"]
    return render_template("alumnos.html", alumnos=lista_alumnos)
@app.route("/alumnos2")
def alumnos2():
    lista_alumnos = ["Pedro", "Daniel", "María", "Jose"]
    return render_template("alumnos2.html", alumnos2=lista_alumnos)

@app.route("/estado_curso")
def estado_curso():
    curso_activo = True
    return render_template("estado_curso.html", activo=curso_activo)

@app.route("/estado_curso2")
def estado_curso2():
    curso_activo = False
    return render_template("estado_curso2.html", activo=curso_activo)

@app.route("/tareas")
def tareas():
    tareas_curso = [
        " Configurar el entorno en PyCharm ",
        " Crear la primera aplicacion Flask ",
        " Practicar con plantillas y Jinja2 "
        ]
    return render_template("tareas.html", tareas=tareas_curso)

if __name__ == "__main__":
    app.run(debug=True)