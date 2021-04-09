import os
from flask import Flask
from flask_migrate import Migrate, MigrateCommand
# from flask_script import Manager

from app import create_app
from app.exts import db
from app.models import User, Role

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

migrate = Migrate(app, db)

# manager = Manager(app)
# manager.add_command('db', MigrateCommand) # 创建数据库映射命令

# if __name__ == '__main__':
#   manager.run()
