"""
Routes of the app defined here.
TODO -> after JWT make sure only the admin can edit author / user information 
TODO -> IP addresses being saved and can be blacklisted
Actually, you can save IP addresses in the DB and highlight users as blacklisted. If so their data is removed and 
they remain blacklisted.
"""

import Data_Provider.Handlers.communication_handler as comm
import Data_Provider.Models.exceptions as exc
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from flask import Flask, request, jsonify

app = Flask(__name__)
jwt = JWTManager(app)

@app.errorhandler(500)
def internal_error(e):
    return comm.create_error_response(500)

@app.errorhandler(404)
def not_found_error(e):
    return comm.create_error_response(404)

@app.errorhandler(405)
def wrong_method(e):
    return comm.create_error_response(405)

@jwt.user_claims_loader
def add_token(identity):
    return {"user" : f"{identity}"}

@jwt.claims_verification_failed_loader
def jwt_verification_failed():
    return comm.create_error_response(418)

@jwt.expired_token_loader
def access_expired(expired_tkn):
    return comm.create_response(104, expired_tkn["type"])

@jwt.unauthorized_loader
def access_denied(arg):
    return comm.create_error_response(401)

@app.route("/check-service",  methods=["GET"])
def home():
    try:
        comm.authors.check_connection()
    except exc.Error as e:
        return comm.create_error_response(e.err_code)
    return comm.create_response(203)

@app.route("/register", methods=["POST"])
def register_user():
    user_name = request.get_json()["username"]
    pass_word = request.get_json()["password"]
    address = request.remote_addr
    if comm.check_user_validity(user_name) is False:
        return comm.create_response(108)
    elif comm.check_address_validity(address) is False:
        return comm.create_error_response(401)
    comm.post_n_put_req_handler("authors", (user_name, pass_word))
    return comm.create_response(200)

@app.route("/login", methods=["POST"])
def login_user():
    if comm.endpoint_check(request) is False:
        return comm.create_error_response(400)
    else:
        user_name = request.get_json()["username"]
        pass_word = request.get_json()["password"]
        try:
            if comm.check_password(user_name, pass_word):
                token = {"access_tkn" : create_access_token(user_name)}
                return comm.create_response(200, token)
            return comm.create_response(107)
        except exc.Error as e:
            return comm.create_error_response(e.err_code)

@app.route("/request/<table>/<string:seach>/<data>", methods=["GET"])
@app.route("/request/<table>/<string:search>")
@app.route("/request/<table>/all/")
@app.route("/request/<table>/")
@jwt_required
def get_request(table, search = None, data = None):
    if comm.get_check(table, search, data):
        return comm.create_error_response(400)
    else:
        try:
            mass_dat = True if "all" in request.url else False
            requested_data = comm.get_n_del_req_handler(table, search, data, mass_dat, True)
        except exc.Error as e:
            return comm.create_error_response(e.error_code)
    return requested_data

@app.route("/send", methods=["POST"])
@jwt_required
def post_request():
    if comm.endpoint_check(request):
        return comm.create_error_response(400)
    else:
        data = request.get_json()
        if comm.post_n_put_req_handler(data["table"], data["values"]):
            return comm.create_response(201)
        return comm.create_error_response(202)

@app.route("/update", methods=["PUT"])
@jwt_required
def put_request():
    if comm.endpoint_check(request):
        return comm.create_error_response(400)
    else:
        data = request.get_json()
        if comm.post_n_put_req_handler(data["table"], data["values"], data["column"], data["phrase"]):
            return comm.create_response(211)
        return comm.create_error_response(202)

@app.route("/delete", methods=["DELETE"])
@jwt_required
def delete_request():
    if comm.endpoint_check(request):
        return comm.create_error_response(400)
    else:
        data = request.get_json()
        if comm.get_n_del_req_handler(data["table"], data["search_column"], data["phrase"], data["mass_dat"], False):
            return comm.create_response(219)
        return comm.create_error_response(202)