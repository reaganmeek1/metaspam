import requests
from flask import Flask, jsonify, request

app = Flask('metaspam')

@app.route('/', methods=['GET'])
def homePage():
    return "yooooooo", 200


app.run(port=8080)
