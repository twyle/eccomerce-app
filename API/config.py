"""
Empty module docstring
"""
import os


class BaseConfig():
    """
    Empty class docstring
    """

    SECRET_KEY = 'SECRET_KEY'
    DEBUG = False
    TESTING = False
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    MONGODB_CONNECT = True

class TestingConfig(BaseConfig):
    """Empty class docstring"""

    DEBUG = True
    TESTING = True

    MONGODB_DB = os.environ['MONGODB_DB']
    MONGODB_HOST = os.environ['MONGODB_HOST']
    MONGODB_PORT = os.environ['MONGODB_PORT']
    MONGODB_USERNAME = os.environ['MONGODB_USERNAME']
    MONGODB_PASSWORD = os.environ['MONGODB_PASSWORD']


class DevelopmentConfig(BaseConfig):
    """
    Empty class docstring
    """

    DEBUG = True
    TESTING = False

    MONGODB_DB = 'flask-react-blog-simple-dev'
    MONGODB_HOST = '127.0.0.1'
    MONGODB_PORT = 27017
    MONGODB_USERNAME = ''
    MONGODB_PASSWORD = ''
    MONGODB_CONNECT = True


class ProductionConfig(BaseConfig):
    """
    Empty class docstring
    """

    DEBUG = False
    TESTING = False

    MONGODB_DB = 'flask-react-blog-simple-prod'
    MONGODB_HOST = 'mongodb+srv://cluster0.ctzy7.mongodb.net/'
    MONGODB_PORT = 27017
    MONGODB_USERNAME = 'flask-api'
    MONGODB_PASSWORD = 'flask-api'
    MONGODB_CONNECT = True
