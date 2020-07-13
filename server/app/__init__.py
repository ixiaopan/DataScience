"""
Aplication Factory
"""

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
  db.init_app(app)

  # seperate file
  # from .views import auth, blog, error
  # app.register_blueprint(auth.bp)
  # app.register_blueprint(blog.bp)
  # app.register_blueprint(error.bp)

  # single file
  from .views import bp
  app.register_blueprint(bp)

  return app
