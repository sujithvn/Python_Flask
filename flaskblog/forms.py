from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username:', validators=[DataRequired(), Length(min=3, max=16)])
    email = StringField('EMail:', validators=[DataRequired(), Email()])
    password = PasswordField('Password:', validators=[DataRequired(), Length(min=3, max=16)])
    confirm_password = PasswordField('Confirm Password:', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
       user = User.query.filter_by(username = username.data).first()
       if user:
           raise ValidationError("Username taken, please choose another.") 

    def validate_email(self, email):
       xemail = User.query.filter_by(email = email.data).first()
       if xemail:
           raise ValidationError("EMail taken, please choose another.") 

class LoginForm(FlaskForm):
    email = StringField('EMail:', validators=[DataRequired(), Email()])
    password = PasswordField('Password:', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
    username = StringField('Username:', validators=[DataRequired(), Length(min=3, max=16)])
    email = StringField('EMail:', validators=[DataRequired(), Email()])
    picture = FileField('Upload your picture:', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username = username.data).first()
            if user:
                raise ValidationError("Username taken, please choose another.") 

    def validate_email(self, email):
        if email.data != current_user.email:
            xemail = User.query.filter_by(email = email.data).first()
            if xemail:
                raise ValidationError("EMail taken, please choose another.") 
                