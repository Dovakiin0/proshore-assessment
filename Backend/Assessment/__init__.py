import os
from flask import Flask
from flask_cors import CORS
from .models import db
from dotenv import load_dotenv, find_dotenv
from .routes.blogs import blogs

def createApp() -> Flask:
    '''
    Function that creates the Flask application with configurations.
    '''
    app = Flask(__name__)
    load_dotenv(find_dotenv())
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
    CORS(app)
    with app.app_context():
        db.init_app(app)
        db.create_all()
    
    app.register_blueprint(blogs, url_prefix="/api/v1/blogs")
    return app
