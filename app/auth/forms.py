# from flask_wtf import FlaskForm
# from wtforms import ValidationError, StringField,PasswordField,SubmitField,BooleanField
# from app.models import User

# from tests.user_test import UserTest
# # from wtforms.validators import Required,Email,EqualTo
# # from ..models import User

# class LoginForm(FlaskForm):
#     username = StringField('Username')
#     password = PasswordField('Password')
#     remember = BooleanField('Remember Me!')
#     submit = SubmitField('Login')

# class RegForm(FlaskForm):
#     email = StringField('Your Email Address')
#     username = StringField('Enter Your Username')
#     password = PasswordField('Password')
#     password_confirm = PasswordField('Confirm Passwords')
#     submit = SubmitField('Sign Up')

#     def validate_email(self,data_field):
#         if UserTest.query.filter_by(email = data_field.data).first():
#             raise ValidationError("The Email has already been taken!")
    
#     def validate_username(self, data_field):
#         if User.query.filter_by(username = data_field.data).first():
#             raise ValidationError("The username has already been taken")