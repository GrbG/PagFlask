import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = 'my_secret_key'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_SSL = False
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'nointeresaelnick@gmail.com'
    MAIL_PASSWORD = os.environ.get('PASSWORD_EMAIL_CF')


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:ji25grohe@localhost/pageflask'
    # SQLALCHEMY_DATABASE_URI = 'mysql://root:password@localhost/flask'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')
# motor://usuario:password@servidor/bd
