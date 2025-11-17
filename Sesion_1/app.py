from flask import Flask

# Creamos una instancia de la aplicación Flask

app = Flask(__name__)

# Definimos una ruta para la URL raíz
@app.route("/")
def hello():
    return "Hola, Flask desde PyCharm."

# Punto de entrada de la aplicación
if __name__ == "__main__":
    app.run(debug=True)
