# from flask_uploads import IMAGES,UploadSet,configure_uploads
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
# from flask_mail import Mail
from flask import Flask
import sqlalchemy
# from . import app
from config import config_option

# mail=Mail()
bootstrap=Bootstrap()
login_manager=LoginManager()
login_manager.session_protection='strong'
login_manager.login_view='auth.login'

def create_app(config_name):
    app=Flask(__name__)
    
       # set the database uniform resource identifier for the database
    app.config["SQLALCHEMY_DATABASE_URI"]='sqlite:///pitches.db'
    # db=sqlalchemy()

    # from app import models  
    # from app import views

    app.config.from_object(config_option[config_name])
    from .auth import auth as authentication_blueprint
    from .main import main as main_blueprint
    app.register_blueprint(authentication_blueprint)
    app.register_blueprint(main_blueprint)

    login_manager.init_app(app)
    # db.init_app(app)


    return app