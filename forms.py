from flask_wtf import FlaskForm, RecaptchaField
from wtforms import TextField, TextAreaField, SubmitField
from wtforms.validators import *

class InputForm(FlaskForm):
    name = TextField("Name")
    message = TextAreaField("Your kind message", validators=[DataRequired()])
    recaptcha = RecaptchaField()
    submit = SubmitField("Send")

class ViewForm(FlaskForm):
    id = TextField("Please enter post UUID", validators=[DataRequired(), UUID("Not a valid UUID!")])
    submit = SubmitField("View")
    recaptcha = RecaptchaField()

class VoteForm(FlaskForm):
    like = SubmitField("Like")
    dislike = SubmitField("Dislike")

class ReportForm(FlaskForm):
    comments = TextAreaField("Additional comments (optional)", validators=[DataRequired()])
    submit = SubmitField("Report")
    recaptcha = RecaptchaField()
