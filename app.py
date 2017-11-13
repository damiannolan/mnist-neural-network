from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@app.route('/upload', methods = ['POST'])
def upload_file():
    file = request.files['file']
    file.save((file.filename))
    return jsonify('file saved')

if __name__ == '__main__':
    app.run()
