"""
Aplication Factory
"""

from flask import Flask, render_template

def create_app():
  app = Flask(__name__)
  
  # simple test
  @app.route('/')
  def hello():
    return render_template('base.html')

  return app
