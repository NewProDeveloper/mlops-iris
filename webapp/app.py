from flask import Flask, render_template, request
import pickle
import numpy as np
import os
import requests
from waitress import serve
# Comment 1
app = Flask(__name__)

DB_URL = "http://db_container:5001/records"

model_path = os.path.join(os.path.dirname(__file__), 'model.pkl')
with open(file="model.pkl", mode='rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = [
        float(request.form['sepal_length']),
        float(request.form['sepal_width']),
        float(request.form['petal_length']),
        float(request.form['petal_width'])
    ]
    
    features = np.array(features)
    features = features.reshape(1, -1)
    pred = model.predict(features)
    flower_name = pred[0]
    requests.post(DB_URL, json={"sl": features[0][0], "sw": features[0][1], "pl": features[0][2], "pw": features[0][3], "prediction": flower_name})
    
    return render_template('index.html', prediction=flower_name)

@app.route("/records", methods=['GET'])
def disp_rec():
    records = requests.get(DB_URL)

    return render_template('data.html', records=records.json())

if __name__ == '__main__':
    serve(app, host="0.0.0.0", port="5000")