from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    recaptcha = RecaptchaField()
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired()])
    email = StringField('Email',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired()])
    password2 = PasswordField('Repeat Password',validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username')
    
    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address')

class NewProjectForm(FlaskForm):
    project_name = StringField('Project Name', validators=[DataRequired()])
    project_number = StringField('Project Number', validators=[DataRequired()])
    recipient = StringField('Recipient', validators=[DataRequired()])
    disturbed_area = StringField('Disturbed Area in Square Feet', validators=[DataRequired()])
    rpa_present = BooleanField('Are RPAs (Resource Protection Areas) present?')
    rma_present = BooleanField('Are RMAs (Resource Management Areas) present?')
    wmp_present = BooleanField('Is the WMP (Watershed Management and Protection Area) present?')
    wetlands_present = BooleanField('Are wetlands present?')
    bmp_recording_reqd = BooleanField('Do BMP Maintenance Agreements need to be recorded?')
    submit = SubmitField('Submit')

class ProjectListForm(FlaskForm):
    pass

class ChecklistForm(FlaskForm):
    pass
