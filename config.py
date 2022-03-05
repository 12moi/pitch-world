from distutils.command.config import config
from distutils.debug import DEBUG
import os

from dotenv import load_dotenv
load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URL=os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATION=True
    SECTRECT_KEY=os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST='app/static/photos'
    MAIL_SERVER='smt.gmail.com'
    MAIL_PORT=456
    MAIL_USE_TLS=False
    MAIL_USE_SSL=True
    MAIL_USERNAME=os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD')

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URL=os.environ.get('DATABASE_URL')

class DevConfig(Config):
    DEBUG=True

config_option={
    'development':DevConfig,
    'production':ProdConfig
}