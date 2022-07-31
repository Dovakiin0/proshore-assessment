import os
from flask import Flask
from flask_cors import CORS
from .models import db, ma
from .routes.blogs import blogs

def createApp(db_uri) -> Flask:
    '''
    Function that creates the Flask application with configurations.
    '''
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    print(db_uri)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
    CORS(app)
    with app.app_context():
        db.init_app(app)
        ma.init_app(app)
        db.create_all()
    
    app.register_blueprint(blogs, url_prefix="/api/v1/blogs")
    return app
