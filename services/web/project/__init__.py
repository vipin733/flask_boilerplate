from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#imports routes
from .routes import home_blueprint

# from .database.model import *

def create_app():
    app = Flask(__name__)

    #load config file
    app.config.from_object("project.config.Config")

    #routes
    app.register_blueprint(home_blueprint, url_prefix='/api/v1/home')

    #init database
    db.init_app(app)
    return app
