from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import hashlib

from .exts import db

class Post(db.Model):
  __tablename__ = 'posts'

  id = db.Column(db.Integer, primary_key=True)
  content = db.Column(db.Text)
  timestamp = db.Column(db.DateTime, default=datetime.utcnow)
  author_id = db.Column(db.Integer, db.ForeignKey('users.id'))


class Role(db.Model):
  # the name of the table
  __tablename__ = 'roles'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(64), unique=True, nullable=False)

  users = db.relationship('User', backref='role')


  # for debugging purpose
  def _repr_(self):
    return '<Role %r>' % self.name


class User(db.Model):
  # the name of the table
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(64), unique=True, nullable=False)
  email = db.Column(db.String(64), unique=True)
  pwd_hash = db.Column(db.String(128))
  role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
  memeber_since = db.Column(db.DateTime, default=datetime.utcnow)
  last_seen = db.Column(db.DateTime, default=datetime.utcnow)
  avatar_hash = db.Column(db.String(32))

  # TODO: 不加lazy报错 has no attribute 'order_by'
  posts = db.relationship('Post', backref='author', lazy='dynamic')

  def __init__(self):
    if self.email is not None and self.avatar_hash is None:
      self.avatar_hash = self.generate_avatar_hash()
  
  def generate_avatar_hash(self):
    return hashlib.md5(self.email.lower().encode('utf-8').hexdigest())

  def gravatar(self, size, default='identicon', rating='g'):
    url = 'https://secure.gravatar.com/avatar'
    # proxy
    # url = 'https://gravatar.loli.net/avatar'
    hash = self.avatar_hash or self.generate_avatar_hash()

    return '{url}/{hash}?s={size}&d={default}r={rating}'.format(url=url, hash=hash, size=size, default=default, rating=rating)

  @property
  def pwd(self):
    raise AttributeError('password is not a readable attribute')

  @pwd.setter
  def pwd(self, pwd):
    self.pwd_hash = generate_password_hash(pwd)

  def verify_pwd(self, pwd):
    return check_password_hash(self.pwd_hash, pwd)

  def ping(self):
    self.last_seen = datetime.utcnow()
    db.session.add(self)
    db.session.commit()

  # for debugging purpose
  def _repr_(self):
    return '<User %r>' % self.name
