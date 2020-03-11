"""
Routes and views for the flask application.
"""

from flask import Flask, request
from Data_Provider.Handlers.query_handler import Query_Handler

app = Flask(__name__)

#Instantiate handlers here
#_queries = Query_Handler()

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
