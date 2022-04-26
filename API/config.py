"""
Empty module docstring
"""
import os


class BaseConfig():
    """
    Empty class docstring
    """

    DEBUG = False
    TESTING = False
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    MONGODB_CONNECT = True


class DevelopmentConfig(BaseConfig):
    """
    Empty class docstring
    """

    DEBUG = True
    TESTING = False

    MONGODB_DB = os.environ['DEVELOPMENT_DB']
    MONGODB_HOST = os.environ['DEVELOPMENT_DB_HOST']
    MONGODB_PORT = os.environ['MONGO_PORT']
    MONGODB_USERNAME = os.environ['DEVELOPMENT_DB_USER']
    MONGODB_PASSWORD = os.environ['DEVELOPMENT_DB_PASSWORD']


class TestingConfig(BaseConfig):
    """Empty class docstring"""

    DEBUG = True
    TESTING = True

    MONGODB_DB = os.environ['TEST_DB']
    MONGODB_HOST = os.environ['TEST_DB_HOST']
    MONGODB_PORT = os.environ['MONGO_PORT']
    MONGODB_USERNAME = os.environ['TEST_DB_USER']
    MONGODB_PASSWORD = os.environ['TEST_DB_PASSWORD']


class ProductionConfig(BaseConfig):
    """
    Empty class docstring
    """

    DEBUG = False
    TESTING = False

    MONGODB_DB = os.environ['PRODUCTION_DB']
    MONGODB_HOST = os.environ['PRODUCTION_DB_HOST']
    MONGODB_PORT = os.environ['MONGO_PORT']
    MONGODB_USERNAME = os.environ['PRODUCTION_DB_USER']
    MONGODB_PASSWORD = os.environ['PRODUCTION_DB_PASSWORD']
