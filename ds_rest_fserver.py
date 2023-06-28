import os
from flask import Flask, request, jsonify, json
from werkzeug.utils import secure_filename
import textract 
import requests


ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'csv', 'xlsx', 'docx'])



def allowed_file(filename):
    file_allowed = ('.' in filename) and (filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS)
    return file_allowed

class MyAPI:
    app = None
    def __init__(self):
      #UPLOAD_FOLDER = 'statics/files'
      self.app = Flask(__name__)
      self.app.secret_key = "secret key"
      #self.app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
      self.app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
      
    # def run(self):
    #     self.app.run(debug=True, host="0.0.0.0")
        
app = MyAPI().app


@app.route('/', methods=['POST'])
def check_file():
    # check if the post request has the file part
    if 'file_to_process' not in request.files:
        resp = jsonify({'message' : 'No file part in the request'})
        resp.status_code = 400
        return resp
    file = request.files['file_to_process']
    if file.filename == '':
        resp = jsonify({'message' : 'No file selected for uploading'})
        resp.status_code = 400
        return resp
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        resp = jsonify({'message' : 'File successfully uploaded' })
        resp.status_code = 201
        return resp 
    else:
        resp = jsonify({'message' :'Allowed file types are txt, pdf, csv, xlsx, docx'})
        resp.status_code = 400
        return resp

@app.route('/extract', methods=['GET'])
def extract_text():
    file = request.files['file_to_process']
    filename = file.filename
    file.save(filename)
    extracted_text = textract.process(filename).decode('utf-8')
    os.remove(filename)
   

    return jsonify({'extracted text': extracted_text})

    
@app.route('/process-file', methods=['POST'])
def process_file():
    dados = {'id': '2', 'name': 'joão', 'age': '38', 'email': 'joaojoao@joao.com' }
    api_url = 'http://127.0.0.1:5001/'
    
    response = requests.post(api_url, json=dados)
    if response.status_code == 200:
        
        return response.json()
    
    else:
        return jsonify({'error': 'Error in the request to the other application'})
    


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

