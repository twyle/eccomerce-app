"""
Empty module docstring
"""
import os

from flask import Flask


app = Flask(__name__)

from API import routes