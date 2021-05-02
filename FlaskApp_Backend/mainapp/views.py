import os
import tensorflow as tf
import numpy as np
import io

from flasgger import swag_from
from flask.views import MethodView
from flask import Flask,Blueprint,request,render_template,jsonify
from datetime import datetime
from PIL import Image

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image as img
from keras.preprocessing.image import img_to_array
from keras.applications.resnet50 import  ResNet50,decode_predictions,preprocess_input

def identifyImage(img_path):
    image = img.load_img(img_path,target_size=(224,224))
    x = img_to_array(image)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    preds = model.predict(x)
    preds = decode_predictions(preds,top=1)
    print(preds)
    return preds

model = ResNet50(weights="imagenet")
model.make_predict_function()


# pylint: disable=no-self-use, unused-variable
class PredictView(MethodView):
    """Class for MLOD Predictions"""
    @swag_from("swag/predict.yaml")
    def post(self):
        """Post method to predict a given image"""
        if "file" not in request.files:
            return "No file found"
        user_file = request.files["file"]
        temp = request.files["file"]
        if user_file.filename == "":
            return "file name not found …"
        else:
            path=os.path.join(os.getcwd()+"/static/"+user_file.filename)
            user_file.save(path)
            classes = identifyImage(path)
            prediction = {
                "Number":classes[0][0][0],
                "Prediction":classes[0][0][1],
                "Confidence Percentage":str(round(classes[0][0][2]*100,2))+" %",
            }
            return prediction
        
