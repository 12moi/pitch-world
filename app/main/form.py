
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
# from wtforms.validators import Required

class PitchForm(FlaskForm):
    title=StringField('Title')
    

class UpdateProfile(FlaskForm):
       bio=TextAreaField('Write a brief bio about you.... ')
       submit=SubmitField('save')

class CommentForm(FlaskForm):
    comment = TextAreaField('Leave a comment')
    submit = SubmitField('Comment')
