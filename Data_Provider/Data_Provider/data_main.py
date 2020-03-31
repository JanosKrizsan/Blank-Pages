"""
Routes of the app defined here.
"""

import Data_Provider.Handlers.communication_handler as comm
import Data_Provider.Models.exceptions as exc
from flask_jwt import JWT, jwt_required, current_identity
from flask import Flask, request

app = Flask(__name__)

@app.route("/",  methods=["GET"])
def home():
    if request.method != "GET":
        return comm.create_error_response(400)
    if not comm.authors.check_connection():
        return comm.create_error_response(503)
    return comm.create_response(200)

@app.route("/register", methods=["POST"])
def register_user():
    pass

@app.route("/login", methods=["POST"])
def login_user():
    pass

@app.route("/request/<table>/<string:seach>/<data>", methods=["GET"])
@app.route("/request/<table>/<string:search>")
@app.route("/request/<table>/all/")
@app.route("/request/<table>/")
def get_request(table, search = None, data = None):
    if comm.get_check(request.method, table, search, data):
        return comm.create_error_response(400)
    else:
        try:
            mass_dat = True if "all" in request.url else False
            requested_data = comm.get_req_handler(table, search, data, mass_dat)
        except exc.Error as e:
            return comm.create_error_response(e.error_code)
    return requested_data

@app.route("/send", methods=["POST"])
def post_request():
    if comm.endpoint_check(request, "POST"):
        return comm.create_error_response(400)
    else:
        data = request.get_json()
        if comm.post_req_handler(data["table"], data["values"]):
            return comm.create_response(201)
        return comm.create_error_response(202)

@app.route("/update", methods=["PUT"])
def put_request():
    if comm.endpoint_check(request, "PUT"):
        return comm.create_error_response(400)
    else:
        data = request.get_json()
        if comm.put_req_handler(data["table"], data["values"], data["column"], data["phrase"]):
            return comm.create_response(211)
        return comm.create_error_response(202)

@app.route("/delete", methods=["DELETE"])
def delete_request():
    if comm.endpoint_check(request, "DELETE"):
        return comm.create_error_response(400)
    else:
        data = request.get_json()
        if comm.del_req_handler(data["table"], data["phrase"], data["mass_dat"]):
            return comm.create_response(219)
        return comm.create_error_response(202)