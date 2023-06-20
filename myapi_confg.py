from flask import Flask

class MyAPI:
    def __init__(self):
      UPLOAD_FOLDER = 'statics/files'
      self.app = Flask(__name__)
      self.app.secret_key = "secret key"
      self.app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
      self.app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
      
    def run(self):
        self.app.run(debug=True, host="0.0.0.0")

if __name__== "__main__":
    my_api = MyAPI()
    my_api.run()
   