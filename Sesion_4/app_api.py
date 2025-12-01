from flask import Flask, jsonify, request

app = Flask(__name__)

# Datos de ejemplo en memoria
alumnos = [
    {"id": 1, "nombre": "Ana", "curso": "Flask", "activo": True},
    {"id": 2, "nombre": "Carlos", "curso": "Flask", "activo": True},
    {"id": 3, "nombre": "Marina", "curso": "IA", "activo": False},
]

cursos = [
    {"id": 1, "nombre": "Flask basico", "duracion_horas": 20},
    {"id": 2, "nombre": "IA introductoria", "duracion_horas": 30},
]


@app.route("/api/status")
def status():
    datos = {
        "status": "ok",
        "version": "1.0",
        "mensaje": "API de ejemplo funcionando"
    }
    return jsonify(datos)


def buscar_alumno_por_id(alumno_id):
    for alumno in alumnos:
        if alumno["id"] == alumno_id:
            return alumno
    return None


@app.route("/api/alumnos", methods=["GET"])
def obtener_alumnos():
    return jsonify(alumnos)


@app.route("/api/alumnos/<int:alumno_id>", methods=["GET"])
def obtener_alumno(alumno_id):
    alumno = buscar_alumno_por_id(alumno_id)
    if alumno is None:
        return jsonify({"error": "Alumno no encontrado"}), 404
    return jsonify(alumno)


@app.route("/api/alumnos_filtrados", methods=["GET"])
def alumnos_filtrados():
    curso = request.args.get("curso")
    if not curso:
        return jsonify(alumnos)
    filtrados = [a for a in alumnos if a["curso"].lower() == curso.lower()]
    return jsonify(filtrados)


@app.route("/api/alumnos", methods=["POST"])
def crear_alumno():
    datos = request.get_json()
    if not datos:
        return jsonify({"error": "JSON no valido"}), 400

    nombre = datos.get("nombre")
    curso_nombre = datos.get("curso")
    activo = datos.get("activo", True)

    errores = []
    if not nombre:
        errores.append("El campo 'nombre' es obligatorio.")
    if not curso_nombre:
        errores.append("El campo 'curso' es obligatorio.")

    if errores:
        return jsonify({"errores": errores}), 400

    nuevo_id = max([a["id"] for a in alumnos]) + 1 if alumnos else 1

    nuevo_alumno = {
        "id": nuevo_id,
        "nombre": nombre,
        "curso": curso_nombre,
        "activo": bool(activo)
    }

    alumnos.append(nuevo_alumno)
    return jsonify(nuevo_alumno), 201


def buscar_curso_por_id(curso_id):
    for curso in cursos:
        if curso["id"] == curso_id:
            return curso
    return None


@app.route("/api/cursos", methods=["GET"])
def obtener_cursos():
    return jsonify(cursos)


@app.route("/api/cursos/<int:curso_id>", methods=["GET"])
def obtener_curso(curso_id):
    curso = buscar_curso_por_id(curso_id)
    if curso is None:
        return jsonify({"error": "Curso no encontrado"}), 404
    return jsonify(curso)


@app.route("/api/cursos", methods=["POST"])
def crear_curso():
    datos = request.get_json()
    if not datos:
        return jsonify({"error": "JSON no valido"}), 400

    nombre = datos.get("nombre")
    duracion = datos.get("duracion_horas")

    errores = []
    if not nombre:
        errores.append("El campo 'nombre' es obligatorio.")
    if duracion is None:
        errores.append("El campo 'duracion_horas' es obligatorio.")
    else:
        try:
            duracion = int(duracion)
        except ValueError:
            errores.append("El campo 'duracion_horas' debe ser un entero.")

    if errores:
        return jsonify({"errores": errores}), 400

    nuevo_id = max([c["id"] for c in cursos]) + 1 if cursos else 1

    nuevo_curso = {
        "id": nuevo_id,
        "nombre": nombre,
        "duracion_horas": duracion
    }

    cursos.append(nuevo_curso)
    return jsonify(nuevo_curso), 201


if __name__ == "__main__":
    app.run(debug=True)
##
## Ejemplos para probar la API:
## http://127.0.0.1:5000/api/status
## http://127.0.0.1:5000/api/alumnos
## http://127.0.0.1:5000/api/alumnos/1
## http://127.0.0.1:5000/api/alumnos_filtrados?curso=Flask
## http://127.0.0.1:5000/api/cursos
##