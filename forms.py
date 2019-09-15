from flask_wtf import FlaskForm, RecaptchaField
from wtforms import TextField, TextAreaField, SubmitField
from wtforms.validators import *

class InputForm(FlaskForm):
    name = TextField("Name")
    message = TextAreaField("Your kind message", validators=[DataRequired()])
    recaptcha = RecaptchaField()
    submit = SubmitField("Send")

class ViewForm(FlaskForm):
    id = TextField("Please enter your post's ID to view its statistics", validators=[DataRequired(), UUID(message="Not a valid UUID!")])
    submit = SubmitField("Lezgo!")

class VoteForm(FlaskForm):
    like = SubmitField("Like")
    dislike = SubmitField("Dislike")
