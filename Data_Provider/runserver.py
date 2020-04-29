"""
This script runs the Data_Provider application.
"""

from os import environ
from Data_Provider.data_main import app
from datetime import timedelta

if __name__ == "__main__":
    app.config["JWT_SECRET_KEY"] = "a_secret_key" #test key, change for deployment
    app.config["JWT_TOKEN_LOCATION"] = "json"
    app.config["JWT_JSON_KEY"] = "access_tkn"
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=7)
    app.run(host="localhost", port=1337, debug=False)
