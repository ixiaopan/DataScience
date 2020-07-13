from flask import Flask, Blueprint

bp = Blueprint('views', __name__)

from . import error, auth, blog, profile
