"""
Routes of the app defined here.
"""

import Data_Provider.Handlers.communication_handler as comm
import Data_Provider.Models.exceptions as exc
from flask import Flask
import requests

app = Flask(__name__)

@app.route("/",  methods=["GET"])
def home():
    if request.method != "GET":
        app.handle_exception(400)
    return "OK"

@app.route("/request/<table>/<string:seach>/<data>", methods=["GET"])
@app.route("/request/<table>/<string:search>")
@app.route("/request/<table>/all/")
@app.route("/request/<table>/")
def get_request(table, search = None, data = None):
    if get_checks(request.method, table, search, data):
        app.handle_exception(400)
    else:
        try:
            mass_dat = True if "all" in request.url else False
            requested_data = comm.get_req_handler(table, search, data, mass_dat)
        except exc.Error as e:
            app.handle_exception(e.err_code)
    return requested_data

def get_checks(method, table, search, data):
    rules = [
        method != "GET",
        str.isalpha(search) == False,
        data == "0",
        str.isdigit(data) == False,
        table == None,
        str.isalpha(table) == False
        ]
    if any(rules):
        return False
    return True

@app.route("/send", methods=["POST"])
def post_request():
    if request.method != "POST":
        app.handle_exception(400)
    else:
        data = request.get_json()
        comm.post_req_handler(data["table"], data["values"])
    return "OK"

@app.route("/update", methods=["PUT"])
def put_request():
    if request.method != "PUT":
        app.handle_exception(400)
    return "OK"

@app.route("/delete", methods=["DELETE"])
def delete_request():
    if request.method != "DELETE":
        app.handle_exception(400)
    else:
    return "OK"

@app.errorhandler(202)
def accepted(e):
    return comm.create_error_response(202)

@app.errorhandler(204)
def no_content(e):
    return comm.create_error_response(204)

@app.errorhandler(400)
def bad_request(e):
    return comm.create_error_response(400)

@app.errorhandler(401)
def unauthorized(e):
    return comm.create_error_response(401)

@app.errorhandler(403)
def forbidden(e):
    return comm.create_error_response(403)

@app.errorhandler(404)
def page_not_found(e):
    return comm.create_error_response(404)

@app.errorhandler(409)
def conflict(e):
    return comm.create_error_response(409)

@app.errorhandler(418)
def i_am_a_hal(e):
    return comm.create_error_response(418)

@app.errorhandler(500)
def internal_error(e):
    return comm.create_error_response(500)

@app.errorhandler(501)
def not_implemented(e):
    return comm.create_error_response(501)

@app.errorhandler(503)
def service_unavailable(e):
    return comm.create_error_response(503)