from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, ValidationError, Regexp, Length
from models import User


class LoginForm(FlaskForm):
    username = StringField('Username:', validators=[DataRequired()])
    password = PasswordField('Password:', validators=[DataRequired()])
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Username:', validators=[DataRequired(),
                                                    Regexp('^[A-Za-z0-9]+(?:[_-][A-Za-z0-9]+)*$', message="Incorrect username."),
                                                    Length(max=64)])
    password = PasswordField('Password:', validators=[DataRequired()])
    password2 = PasswordField('Repeat password:', validators=[DataRequired(),EqualTo('password'), Length(max=128)])
    submit = SubmitField('Add User')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('User already exist.')


class DeleteUserButton(FlaskForm):
    submit = SubmitField('Remove')
