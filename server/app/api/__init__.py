from flask import Flask

from .exts import db
from config import config

def create_app(config_mode):
  app = Flask(__name__)

  # load config file
  app.config.from_object(config[config_mode])

  # simple test
  @app.route('/user/<name>')
  def user(name):
    return '<h1>Hello {}'.format(name)

  # bind db to app
  # db.init_app(app)

  from .views import api
  app.register_blueprint(api, url_prefix="/api/v1")

  return app
