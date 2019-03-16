from flask import Flask

producer_app = Flask(__name__)

from producer_app import routes
