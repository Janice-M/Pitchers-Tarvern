from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField, BooleanField
from wtforms.validators import Required,Email,EqualTo
from ..models import User
from wtforms import ValidationError


class RegistrationForm(FlaskForm):

    email = StringField('Rafiki, Enter your email address',validators=[Required(),Email()])
    username = StringField( ' Rafiki, enter username',validators = [Required()])
    password = PasswordField('Password',validators = [Required(),
    EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords',validators = [Required()])
    submit = SubmitField('Sign Up')
    
        """ password and email validation """
        
    def validate_email(self,data_field):
            if User.query.filter_by(email =data_field.data).first():
                raise ValidationError('Oopsie rafiki, email is taken.')

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('Oopsie rafiki, the username is taken')


class LoginForm(FlaskForm):
    email = StringField('Rafiki enter your email Address',validators=[Required(),Email()])
    password = PasswordField('Rafiki enter your password',validators =[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')