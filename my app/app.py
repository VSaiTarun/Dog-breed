from flask import Flask, request, jsonify, render_template
from PIL import Image
import io
import numpy as np
import tensorflow as tf
import joblib

app = Flask(__name__)

model = tf.keras.models.load_model('dog_breed_model.h5')

CLASS_NAMES = ['scottish_deerhound','maltese_dog','bernese_mountain_dog']

def preprocess_image(image):
    image = image.resize((224, 224))
    image_array = np.array(image)
    image_array = image_array / 255.0
    image_array = np.expand_dims(image_array, axis=0)
    return image_array

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET','POST'])
def predict():
    file = request.files['file']
    image = Image.open(io.BytesIO(file.read()))
    image_array = preprocess_image(image)
    prediction = model.predict(image_array)[0]
    index = np.argmax(prediction)
    breed = CLASS_NAMES[index]
    return render_template('index.html', breed=breed)

if __name__ == '__main__':
    app.run(debug=True)