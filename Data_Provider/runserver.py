"""
This script runs the Data_Provider application.
"""

from os import environ
from Data_Provider import data_main

if __name__ == "__main__":
    data_main.app.run(host="localhost", port=1337, debug=True)
