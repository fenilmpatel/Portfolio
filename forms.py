from flask_wtf import FlaskForm

from wtforms import StringField,PasswordField,SubmitField,BooleanField

from wtforms.validators import DataRequired,Length,Email,EqualTo

class RegistrationForm(FlaskForm):

    username = StringField('username',validators = [DataRequired(),Length(min=2,max=25)])

    email = StringField('Email',validators = [Email(),DataRequired()])

    password = PasswordField('password',validators = [DataRequired()])

    
    confirm_password = PasswordField('confirm password',validators = [DataRequired(),EqualTo('password')])

    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):

    
    email = StringField('Email',validators = [Email(),DataRequired()])

    password = PasswordField('password',validators = [DataRequired()])
    
    remember = BooleanField('Remember Me')

    submit = SubmitField('LogIn')