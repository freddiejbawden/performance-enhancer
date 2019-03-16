from flask import Flask

api = Flask(__name__)

from api import routes

api.run("0.0.0.0")
