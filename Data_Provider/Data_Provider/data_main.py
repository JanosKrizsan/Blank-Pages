"""
Routes and views for the flask application.
"""

from flask import Flask
from Data_Provider.Handlers import article_handler, author_handler, source_handler
from Data_Provider.Static.creds import psql_creds
from Data_Provider.Static.utils import response_creator
import requests

app = Flask(__name__)

creds = psql_creds()

authors = author_handler.Author_Handler(creds[0], creds[1], creds[2])
articles = article_handler.Article_Handler(creds[0], creds[1], creds[2])
sources = source_handler.Source_Handler(creds[0], creds[1], creds[2])


@app.route('/',  methods=['GET'])
def home():
    if authors.check_connection():
        return response_creator()
    return response_creator()

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
