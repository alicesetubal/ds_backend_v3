import os
#import urllib.request
from myapi_confg import MyAPI
from flask import Flask, request, jsonify, url_for
from werkzeug.utils import secure_filename
import textract 
from class_file_extractor import FileExtrator

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'csv', 'xlsx', 'docx'])
app = MyAPI().app

def allowed_file(filename):
    file_allowed = ('.' in filename) and (filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS)
    return file_allowed

@app.route('/', methods=['POST'])
def upload_file():
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
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        resp = jsonify({'message' : 'File successfully uploaded' })
        resp.status_code = 201
        return resp 
    else:
        resp = jsonify({'message' :'Allowed file types are txt, pdf, csv, xlsx, docx'})
        resp.status_code = 400
        return resp

@app.route('/', methods=['GET'])
def extract_to_text():
    file = request.files['file_to_process']
    filename = file.filename
    file.save(filename)
    extracted_text = textract.process(filename).decode('utf-8')
    os.remove(filename)
    return jsonify({'extracted text': extracted_text})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
