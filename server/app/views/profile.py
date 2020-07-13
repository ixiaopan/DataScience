from flask import Blueprint, render_template, abort, session
from . import bp
from ..models import User, Post

# dp = Blueprint('user', __name__)

@bp.route('/profile/<username>')
def profile(username):
  user = User.query.filter_by(name=username).first()

  if user is None:
    abort(404)
    
  posts = user.posts.order_by(Post.timestamp.desc()).all()

  return render_template('profile.html', user=user, posts=posts, name=session.get('name'))
