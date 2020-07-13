class Config:
  CHARSET='utf-8'
  SECRET_KEY = 'whatever'
  SQLALCHEMY_TRACK_MODIFICATIONS = False


class Dev(Config):
  DEBUG = True

  USERNAME = 'root'
  PASSWORD = ''
  HOST = '127.0.0.1'
  PORT = 3306
  DATABASE = 'test'

  DB_URI = 'mysql+pymysql://{username}:{password}@{host}:{port}/{database}'.format(
    username=USERNAME, 
    password=PASSWORD,
    host=HOST,
    port=PORT,
    database=DATABASE
  )
  SQLALCHEMY_DATABASE_URI = DB_URI
  SQLALCHEMY_ECHO = True


class Test(Config):
  TESTING = True
  SQLALCHEMY_DATABASE_URI = ''


class Prod(Config):
  SQLALCHEMY_DATABASE_URI = ''


config = {
  'dev': Dev,
  'test': Test,
  'prod': Prod,

  'default': Dev
}