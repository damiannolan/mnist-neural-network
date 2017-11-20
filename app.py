from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from PIL import Image

import keras as kr
import numpy as np 

app = Flask(__name__)
CORS(app)

model = kr.models.load_model('mnist-neural.h5')

model.summary()

@app.route('/upload', methods = ['POST'])
def upload_file():
    img = Image.open(request.files['file'].stream).convert('L')
    img = img.resize((28, 28))
    #img.show()
    pix = np.array(img).astype(np.float32)
    print(pix)
    print(pix.shape)
    print(pix.dtype)

    pix = pix.reshape(784)
    #pix /= 255
    print(pix)
    print(pix.shape)
    #print(img.tobytes())
    #img.save('img/resize.png')
    
    test_image = np.array([pix])
    prediction = list(model.predict(test_image))
    print(prediction[0])
    prediction = np.argmax(prediction[0])

    return jsonify(str(prediction))

if __name__ == '__main__':
    app.run()
