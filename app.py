from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from PIL import Image

app = Flask(__name__)
CORS(app)

@app.route('/upload', methods = ['POST'])
def upload_file():
    img = Image.open(request.files['file'].stream).convert('L')
    img = img.resize((28, 28))
    img.show()
    img.save('img/resize.png')

    prediction = 4
    return jsonify(str(prediction))

if __name__ == '__main__':
    app.run()
