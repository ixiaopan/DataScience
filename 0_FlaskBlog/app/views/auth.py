from flask import Blueprint, session, redirect, request, url_for, render_template, flash

from ..exts import db
from ..models import Role, User
from ..forms.signin import SignInForm
from . import bp

# bp = Blueprint('auth', __name__)

@bp.route('/register', methods=['GET', 'POST'])
def register():
  if request.method == 'GET':
    return render_template('register.html')
  
  if request.method == 'POST':
    username = request.form['username']
    email = request.form['email']
    pwd = request.form['pwd']

    user = User.query.filter_by(name=username).first()

    if user is None:
      user_role = Role.query.filter_by(name='User').first()
      user_new = User(name=username, email=email, pwd=pwd, role=user_role)
      db.session.add(user_new)
      db.session.commit()

      session['name'] = username
      return redirect(url_for('views.index'))
    else:
      flash('You have already registered')
      return render_template('register.html')


@bp.route('/signin', methods=['GET', 'POST'])
def signin():
  form = SignInForm()

  if form.validate_on_submit():
    username = request.form['username']
    pwd = request.form['pwd']

    user = User.query.filter_by(name=username).first()

    if user is None:
      flash('Username is not exist')
      return render_template('signin.html', form=form)

    elif user.verify_pwd(pwd):
      session['name'] = username
      user.ping()
      return redirect(url_for('views.index'))

    else:
      flash('Password is not correct')
      return render_template('signin.html', form=form)

  return render_template('signin.html', form=form)


@bp.route('/logout')
def logout():
  # remove the username from the session if it's there
  session.pop('name', None)

  return redirect(url_for('views.index'))
