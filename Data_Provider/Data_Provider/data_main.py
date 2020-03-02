"""
Routes and views for the flask application.
"""

from flask import Flask, request
app = Flask(__name__)

@app.route('/',  methods=['GET'])
def home():
    return "Server Online"

@app.route('/request', methods=['GET'])
def get_request():
    pass

@app.route('/send', methods=['POST'])
def post_request():
    pass

@app.route('/update', methods=['PUT'])
def put_request():
    pass

@app.route('/delete', methods=['DELETE'])
def delete_request():
    pass
