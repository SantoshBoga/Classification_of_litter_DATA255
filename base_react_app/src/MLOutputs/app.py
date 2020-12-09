import tensorflow as tf
from tensorflow import keras
from keras.preprocessing import image
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import cv2
from keras.preprocessing.image import ImageDataGenerator, img_to_array, array_to_img, load_img
import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from keras.models import Sequential, load_model
from flask_cors import CORS
import json

import time
import base64


model_path = '../../../trained_model1.h5'


model = keras.models.load_model(model_path)
labels = {0: 'cardboard', 1: 'glass', 2: 'metal', 3: 'paper', 4: 'plastic', 5: 'trash'}

def predict(file):
    #img_path = '/content/drive/My Drive/Garbage_Classification/Garbage classification/Garbage classification/plastic/plastic75.jpg'
    dict = {}
    results = []
    dict['file_path'] = file
    results.append(file)
    img = image.load_img(file, target_size=(300, 300))
    img = image.img_to_array(img, dtype=np.uint8)
    img=np.array(img)/255.0

    plt.title("Loaded Image")
    plt.axis('off')
    plt.imshow(img.squeeze())

    p=model.predict(img[np.newaxis, ...])
    dict['Maximum_Probability'] = np.max(p[0], axis =-1)
    results.append(str(np.max(p[0], axis =-1)))
    print("Maximum Probability: ",np.max(p[0], axis=-1))
    predicted_class = labels[np.argmax(p[0], axis=-1)]
    dict['Classified'] = predicted_class
    results.append(str(predicted_class))
    print("Classified:",predicted_class)

    return dict, results

app = Flask(__name__)
cors = CORS(app, resources ={r"/": {"origins": "*"}})
@app.route('/', methods = ['GET', 'POST'])
def upload_file():
    #if request.method == 'GET':
     #   print("In Get")
      #  return "Get out"
    if request.method == 'POST':

        print("Fuck you!")
        import time
        start_time = time.time()
        file = request.files['file']

        file_path = secure_filename(file.filename)
        print('*'*30)
        
        dict, result = predict(file_path)
        print("----%s seconds----" %str(time.time() - start_time))
        print(result)

        #print(json.dumps(str(result)))
 


        return (json.dumps(str(result)))


if __name__ == "__main__":
    app.debug=True
    app.run(host = 'localhost', port = 8080, threaded = False)
