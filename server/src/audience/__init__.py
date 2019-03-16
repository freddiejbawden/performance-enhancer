from flask import Flask

audience_app = Flask(__name__)

from audience_app import routes
