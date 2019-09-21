import os
from config import Config
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_talisman import Talisman
from forms import InputForm, ViewForm, VoteForm

app = Flask(__name__)

talisman = Talisman(
    app,
    content_security_policy = {
        'default-src': ['\'self\'',],
        'style-src': ['\'self\'', '*.bootstrapcdn.com'],
        'script-src': ['\'self\'', 'https://www.google.com/recaptcha/', 'https://www.gstatic.com/recaptcha/', '*.bootstrapcdn.com', 'https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js', 'https://code.jquery.com/jquery-3.3.1.slim.min.js'],
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
        #return redirect(url_for("success", message=message, name=name, lookupId = note.lookupId))
        return render_template("success.html", message=message, name=name, lookupId = note.lookupId)
    return render_template("index.html", form=form)

@app.route('/view', methods = ["GET", "POST"])
def view():
    form = ViewForm()
    if form.validate_on_submit():
        return render_template("statistics.html", info=Note.viewNote(request.form["id"]))
    return render_template("view.html", form=form)

@app.route('/smile', methods=['GET', 'POST'])
def smile():
    form = VoteForm()
    if "randomNote" not in session:
        session["randomNote"] = toJSON(Note.getRandomNote())
    if form.validate_on_submit():
        tempNote = Note.returnNote(session["randomNote"]["lookupId"])
        if form.like.data:
            tempNote.update({"numLikes": tempNote.numLikes + 1})
        elif form.dislike.data:
            tempNote.update({"numDislikes": tempNote.numDislikes + 1})
        session.clear()
        return redirect('/smile')
    return render_template("smile.html", notez = Note.returnNote(session["randomNote"]["lookupId"]), form=form)

@app.route('/rankings', methods=['GET'])
def rankings():
    return render_template("rankings.html", rankings=Note.getTopRanks())

def toJSON(obj):
    return jsonify(message = obj.message,
                    name = obj.name,
                    createdAt = obj.createdAt,
                    numViews = obj.numViews,
                    lookupId = obj.lookupId,
                    numLikes = obj.numLikes,
                    numDislikes = obj.numDislikes).get_json()

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__': #only runs if you actually call app.py (if importing app.py to another file and run, __name__ != '__main__')
    app.run()
