import json
from os import path

import models.lstm

with open(path.join(path.dirname(__file__), 'parameters.json')) as f:
    parameters = json.load(f)