import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    FLASK_ENV = 'development'
    SECRET_KEY = os.getenv('SECRET_KEY') or "this:is:a:super:bad:secret:key"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DB_ACCESS_URI') or "mysql+pymysql://root:root@localhost:6603/utopia"
