import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = 'my_secret_key'


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:ji25grohe@localhost/pageflask'
    # SQLALCHEMY_DATABASE_URI = 'mysql://root:password@localhost/flask'
# motor://usuario:password@servidor/bd
