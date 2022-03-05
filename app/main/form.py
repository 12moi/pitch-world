
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import Required

class PitchForm(FlaskForm):
    title=StringField('Title',validators=[Required()])
    

class UpdateProfile(FlaskForm):
       bio=TextAreaField('Write a brief bio about you.... ',validators=[Required()])
       submit=SubmitField('save')

class CommentForm(FlaskForm):
    comment = TextAreaField('Leave a comment',validators=[Required()])
    submit = SubmitField('Comment')
