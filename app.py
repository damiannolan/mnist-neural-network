from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from PIL import Image

import keras as kr
import numpy as np 

app = Flask(__name__)
CORS(app)

# Pip3 install h5py
# Load the model from the h5 file
model = kr.models.load_model('mnist-neural.h5')

# Print the model summary to the terminal
model.summary()

@app.route('/upload', methods = ['POST'])
def mnist_prediction():
    # Load the image file into an object using PIL Image lib
    # Use .convert('L') to convert the file to (8-bit pixels, black and white) - grayscale
    # Use .resize() to resize the width & height to 28 x 28
    img = Image.open(request.files['file'].stream).convert('L')
    img = img.resize((28, 28))
    
    # Convert the PIL Image to a pixel array by passing it to np.array()
    # And change the dtype to np.float32
    pixel_array = np.array(img).astype(np.float32)
    pixel_array = pixel_array.reshape(784)
    
    # The models accepts an array of images to make predictions, so will return an array of predictions
    # Use np.argmax() to find the prediction value in the One-Hot vector
    prediction = list(model.predict(np.array([pixel_array])))
    print(prediction[0])
    prediction = np.argmax(prediction[0])
    print(prediction)

    return jsonify(str(prediction))

if __name__ == '__main__':
    app.run()
