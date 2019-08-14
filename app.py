import os
from config import Config
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
#from flask_seasurf import SeaSurf
from flask_talisman import Talisman
from forms import InputForm, ViewForm

app = Flask(__name__)
#csrf = SeaSurf(app)
talisman = Talisman(
    app,
    content_security_policy = {
        'default-src': ['\'self\'', '*.bootstrapcdn.com'],
        'script-src': ['\'self\'', 'https://www.google.com/recaptcha/', 'https://www.gstatic.com/recaptcha/'],
        'frame-src': "https://www.google.com/recaptcha/"
    },
    content_security_policy_nonce_in=['script-src']
)

app.config.from_object(Config)
app.config.from_object(os.environ['APP_SETTINGS']) #changes when environment changes (e.g. testing to staging)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app) #initalizes a connection to the db

from models import Note

@app.route('/', methods = ["GET", "POST"])
def hello():
    form = InputForm()
    if form.validate_on_submit():
        message = request.form["message"]
        name = request.form["name"]
        note = Note(message=message, name=name)
        note.add()
        return redirect(url_for("success", message=message, name=name, lookupId = note.lookupId))
    return render_template("index.html", form=form)

@app.route('/success')
def success():
    return render_template("success.html", message=request.args.get("message"), name=request.args.get("name"), lookupId = request.args.get("lookupId"))

@app.route('/view', methods = ["GET", "POST"])
def view():
    form = ViewForm()
    if form.validate_on_submit():
        return Note.viewNote(request.form["id"])
    return render_template("view.html", form=form)

@app.route('/notez')
def view_notes():
    return render_template("notez.html", notez = Note.getRandomNote())

if __name__ == '__main__': #only runs if you actually call app.py (if importing app.py to another file and run, __name__ != '__main__')
    app.run()
