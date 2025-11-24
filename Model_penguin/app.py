from flask import Flask, render_template, request
import numpy as np
import pickle
import joblib
from sklearn.preprocessing import StandardScaler


# Función de predicción
def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1, 4)
    scaler = StandardScaler()
    to_predict = scaler.fit_transform(to_predict)
    # loaded_model = pickle.load(open("model.pkl", "rb"))
    loaded_model = joblib.load("model_penguin.pkl") # Cargamos el modelo
    result = loaded_model.predict(to_predict)
    return result[0]

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        result = ValuePredictor(to_predict_list)  # Llamada la función predictora

        if int(result) == 0:
            prediction = 'Adelie'
        elif int(result) == 1:
            prediction = 'Chinstrap'
        else:
            prediction = 'Gentoo'

        return render_template("result.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)