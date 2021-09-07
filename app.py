from flask import Flask, jsonify
from flask_restful import Resource, Api


import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model

from predict_crop import  get_crop_predict, download_get_crop_predict

app = Flask(__name__)
api = Api(app)

@app.route('/person/')
def hello():
    return jsonify({'name':'Jimit',
                    'address':'India'})      


@app.route('/predict_crop_url')
def predict_crop():
    class_index, class_value = get_crop_predict('./WhatsApp Image 2021-09-06 at 6.23.15 PM.jpeg')
    response = {'crop':class_index, 'prediction':class_value}
    return jsonify(response)

@app.route('/predict_crop_nutrient/<path:path>')
def predict_crop_nutrient(path):
    print(path)
    class_index, class_value, crop_name =  download_get_crop_predict(path)
    response = {'prediction_index':class_index, 'prediction_value':class_value, 'predicted_crop':crop}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)