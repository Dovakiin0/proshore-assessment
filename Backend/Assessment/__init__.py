from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

def createApp():
    '''
    Function that creates the Flask application with configurations.
    '''
    app = Flask(__name__)
    CORS(app)

    return app
