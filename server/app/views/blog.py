from flask import Blueprint, session, redirect, url_for, render_template, request, flash

from . import bp
from ..models import Post, User
from ..exts import db

# bp = Blueprint('blog', __name__)

@bp.route('/')
def index():
  page = request.args.get('page', 1, type=int)

  pagination = Post.query.order_by(Post.timestamp.desc()).paginate(page, per_page=5, error_out=False)

  posts = pagination.items

  return render_template('index.html', name=session.get('name'), posts=posts, pagination=pagination)


@bp.route('/post', methods=['POST'])
def post():
  content = request.form['content']

  if content == '':
    flash('Content is empty, please input something')
    return redirect(url_for('views.index'))

  user = User.query.filter_by(name=session.get('name')).first()  
  post_new = Post(content=content, author_id=user.id)
  db.session.add(post_new)
  db.session.commit()

  return redirect(url_for('views.index'))


@bp.route('/post/<int:id>')
def detail(id):
  post = Post.query.get_or_404(id)
  return render_template('post.html', post=post)
