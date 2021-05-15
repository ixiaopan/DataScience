"""
Restful Entry
"""

import os
from flask import Flask

from app.api import create_app

app = create_app(os.getenv('FLASK_CONFIG') or 'dev_api')

if __name__ == '__main__':
  app.run()
