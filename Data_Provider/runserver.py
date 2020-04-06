"""
This script runs the Data_Provider application.
"""

from os import environ
from Data_Provider import data_main
from datetime import timedelta

if __name__ == "__main__":
    data_main.app.config["JWT_SECRET_KEY"] = "a_secret_key" #testing key, change for deployment
    data_main.app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=1)
    data_main.app.config["JWT_QUERY_STRING_NAME"] = "access_tkn"
    data_main.app.run(host="localhost", port=1337, debug=False)
