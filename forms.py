from flask_wtf import FlaskForm
from wtforms import TextField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

class InputForm(FlaskForm):
    name = TextField("Name")
    message = TextAreaField("Your kind message", validators=[DataRequired()])
    submit = SubmitField("Send")

class ViewForm(FlaskForm):
    id = TextField("Please enter your post's ID to view its statistics", validators=[DataRequired()])
    submit = SubmitField("Lezgo!")
