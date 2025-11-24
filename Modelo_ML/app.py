from flask import Flask, render_template, request
import numpy as np
import pickle
import joblib


# Función de predicción
def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1, 4)
    # loaded_model = pickle.load(open("model.pkl", "rb"))
    loaded_model = joblib.load("model.pkl") # Cargamos el modelo
    result = loaded_model.predict(to_predict)
    return result[0]

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        result = ValuePredictor(to_predict_list)  # Llamada la función predictora

        if int(result) == 0:
            prediction = 'IRIS SETOSA'
        elif  int(result) == 1:
            prediction = 'IRIS VERSICOLOR'
        else:
            prediction = 'IRIS VIRGINICA'


        return render_template("result.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)

    ##https://4geeks.com/es/lesson/implementar-modelo-usando-flask-y-heroku