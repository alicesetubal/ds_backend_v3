from flask import Flask, jsonify, request


app = Flask(__name__)

@app.route('/', methods=['POST'])
def handle_request():
    dados = request.get_json()
      
    response_data = {
            'message': 'Data received successfully',
            'processed_data': dados
        }
    print(dados)
    return jsonify(response_data), 200
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001) 


