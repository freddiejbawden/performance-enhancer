from flask import Flask

things_app = Flask(__name__)

from things_app import routes
