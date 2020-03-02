"""
This script runs the Data_Provider application using a development server.
"""

from os import environ
from Data_Provider import data_main

if __name__ == '__main__':
    data_main.app.run(host='0.0.0.0', port=8080, debug=True)
