"""
Aplication Factory
"""

from os import path
import torch
from flask import Flask, render_template, request, jsonify

from models.lstm import SentimentLSTM
from models import parameters

def create_app():
  app = Flask(__name__)

  model_pkl = torch.load(path.join(path.dirname(__file__), '../models/model.pkl'))

  # homepage
  @app.route('/')
  def hello():
    return render_template('base.html')

  # api
  @app.route('/predict', methods=['POST'])
  def predict():
    pass
    model = SentimentLSTM(**parameters)
    model.load_state_dict(model_pkl)   
    model.eval()

    # print(request.form.values())

    # model(inputs)

  return app
