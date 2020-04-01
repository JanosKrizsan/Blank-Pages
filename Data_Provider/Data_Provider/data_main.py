"""
Routes of the app defined here.
TODO -> after JWT make sure only the admin can edit author / user information 
TODO -> IP addresses being saved and can be blacklisted
Actually, you can save IP addresses in the DB and highlight users as blacklisted. If so their data is removed and 
they remain blacklisted.
"""

import Data_Provider.Handlers.communication_handler as comm
import Data_Provider.Models.exceptions as exc
from datetime import timedelta
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from flask import Flask, request, jsonify

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "a_secret_key" #development key, change for deployment
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=1)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=7)
app.config["JWT_QUERY_STRING_NAME"] = "access_tkn"
jwt = JWTManager(app)

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
def access_denied():
    return comm.create_error_response(401)

@app.route("/",  methods=["GET"])
def home():
    if request.method != "GET":
        return comm.create_error_response(400)
    if not comm.authors.check_connection():
        return comm.create_error_response(503)
    return comm.create_response(200)

@app.route("/register", methods=["POST"])
def register_user():
    if comm.endpoint_check(request, "POST"):
        return comm.create_error_response(400)
    else:
        pass

@app.route("/login", methods=["POST"])
def login_user():
    if comm.endpoint_check(request, "POST"):
        return comm.create_error_response(400)
    else:
        user_name = request.get_json()["username"]
        pass_word = request.get_json()["password"]
        if not comm.check_user(user_name, pass_word):
            token = {"access_tkn" : create_access_token(user_name)}
        return comm.create_response(200, token)

@app.route("/request/<table>/<string:seach>/<data>", methods=["GET"])
@app.route("/request/<table>/<string:search>")
@app.route("/request/<table>/all/")
@app.route("/request/<table>/")
@jwt_required
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
@jwt_required
def post_request():
    if comm.endpoint_check(request, "POST"):
        return comm.create_error_response(400)
    else:
        data = request.get_json()
        if comm.post_req_handler(data["table"], data["values"]):
            return comm.create_response(201)
        return comm.create_error_response(202)

@app.route("/update", methods=["PUT"])
@jwt_required
def put_request():
    if comm.endpoint_check(request, "PUT"):
        return comm.create_error_response(400)
    else:
        data = request.get_json()
        if comm.put_req_handler(data["table"], data["values"], data["column"], data["phrase"]):
            return comm.create_response(211)
        return comm.create_error_response(202)

@app.route("/delete", methods=["DELETE"])
@jwt_required
def delete_request():
    if comm.endpoint_check(request, "DELETE"):
        return comm.create_error_response(400)
    else:
        data = request.get_json()
        if comm.del_req_handler(data["table"], data["phrase"], data["mass_dat"]):
            return comm.create_response(219)
        return comm.create_error_response(202)