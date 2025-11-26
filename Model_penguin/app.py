from flask import Flask, render_template, request
import numpy as np
import pickle
import joblib



# Función de predicción
def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1, 4)

    # .fit_transform(to_predict) calcula la media y la desviación estándar solo a partir de la única fila de datos que le estás pasando en ese momento.
    # Esto estandariza los datos de manera incorrecta, ya que el modelo de Machine Learning espera datos estandarizados con respecto a la media y desviación estándar
    # de el total del conjunto de datos de entrenamiento, no solo de la muestra individual que estás prediciendo.
    # Para ello: 1.Entrenar y guardar el StandardScaler junto con el modelo model_penguin.pkl. (joblib.dump(scaler, 'scaler_penguin.pkl'))
    # 2.Cargar el StandardScaler guardado dentro de la función ValuePredictor
    loaded_scaler = joblib.load("scaler_penguin.pkl")
    # 3.Usar solo transform (no fit_transform) en los datos nuevos.
    to_predict_scaled = loaded_scaler.transform(to_predict)
    # loaded_model = pickle.load(open("model.pkl", "rb"))
    loaded_model = joblib.load("model_penguin.pkl") # Cargamos el modelo
    result = loaded_model.predict(to_predict_scaled)
    return result[0]
    # Al cargar el escalador pre-entrenado, garantizas que los datos nuevos se transformen utilizando exactamente la misma media y desviación estándar que se usaron cuando
    # se entrenó el modelo. Esto asegura que la entrada a la función predict() sea consistente con lo que el modelo "espera" ver, y debería darte las predicciones correctas
    # para las diferentes especies.

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