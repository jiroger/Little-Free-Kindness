import os
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_seasurf import SeaSurf
from flask_talisman import Talisman

app = Flask(__name__)
csrf = SeaSurf(app)
talisman = Talisman(
    app,
    content_security_policy = {
        'default-src': ['\'self\'', '*.bootstrapcdn.com'],
        'script-src': '\'self\''
    },
    content_security_policy_nonce_in=['script-src']
)

app.config.from_object(os.environ['APP_SETTINGS']) #changes when environment changes (e.g. testing to staging)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app) #initalizes a connection to the db

from models import Note

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/success', methods=["GET", "POST"])
def success():
    if request.method == "POST":
        message = request.form["message"]
        name = request.form["name"]
        note = Note(message=message, name=name)
        note.add()
    return render_template("success.html", message=request.form["message"], name=request.form["name"], lookupId = note.lookupId)

@app.route('/notez')
def view_notes():
    return render_template("notez.html", notez = Note.getRandomNote())

if __name__ == '__main__': #only runs if you actually call app.py (if importing app.py to another file and run, __name__ != '__main__')
    app.run()
