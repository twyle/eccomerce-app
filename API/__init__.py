"""
Empty module docstring
"""
import os

from flask import Flask

from API.config import DevelopmentConfig


app = Flask(__name__)

def set_flask_environment() -> str:
    """Sets the flask development environment

    Raises
    ------
    KeyError

    Returns
    -------
    str:
        Flask operating environment i.e development 
    """

    if os.environ['FLASK_ENV'] == 'development':  # pragma: no cover
        app.config.from_object(DevelopmentConfig)

    return os.environ['FLASK_ENV']


set_flask_environment()

from API import routes