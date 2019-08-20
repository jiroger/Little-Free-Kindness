from flask_wtf import FlaskForm, RecaptchaField
from wtforms import TextField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

class InputForm(FlaskForm):
    name = TextField("Name")
    message = TextAreaField("Your kind message", validators=[DataRequired()])
    recaptcha = RecaptchaField()
    submit = SubmitField("Send")

class ViewForm(FlaskForm):
    id = TextField("Please enter your post's ID to view its statistics", validators=[DataRequired()])
    submit = SubmitField("Lezgo!")

class VoteForm(FlaskForm):
    like = SubmitField("Like",
                        #render_kw={'class':'g-recaptcha', 'data-sitekey':'6Ldy_rMUAAAAAA_0vaf_xb7o9Ta853RjQ_9D1BLU', 'data-callback':'onSubmitCallback'}
                        )
    dislike = SubmitField("Dislike")
    recaptcha = RecaptchaField()
