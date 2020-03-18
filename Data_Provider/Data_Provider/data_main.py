"""
Routes and views for the flask application.
"""

from Data_Provider.Handlers.communication_handler import get_req_handler, post_req_handler, put_req_handler, del_req_handler
from flask import Flask
import requests

app = Flask(__name__)

@app.route('/',  methods=['GET'])
def home():
    return "OK"

@app.route('/request/<data>', methods=['GET'])
def get_request(data):
    

    return "Request"

@app.route('/send', methods=['POST'])
def post_request():
    return "Send"


@app.route('/update', methods=['PUT'])
def put_request():
    return "Update"


@app.route('/delete', methods=['DELETE'])
def delete_request():
    return "Delete"
