from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired

class SignInForm(FlaskForm):
  username = StringField('Username', validators=[DataRequired()])
  pwd = PasswordField('Password', validators=[DataRequired()])
