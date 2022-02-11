import requests
import json
from flask import Flask, jsonify, request

app = Flask('metaspam', static_folder='./web', static_url_path='/')

spams = []
@app.route('/', methods=['GET'])
def homePage():
    return app.send_static_file('index.html')

@app.route('/spams', methods=['GET'])
def getSpams():
    return jsonify(spams)

@app.route('/spam', methods=['POST'])
def postSpam():
    #ip_address = request.remote_addr
    #print(ip_address)
    body = json.loads(request.data)
    #obj = {'ip': ip_address, 'message': body['message']}
    spams.append(body['message'])
    return 'added post', 200

app.run(port=8080)
