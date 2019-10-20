import os
from config import Config
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_talisman import Talisman
from flask_mail import Mail, Message
from forms import InputForm, ViewForm, VoteForm, ReportForm
import json

app = Flask(__name__)

talisman = Talisman(
    app,
    content_security_policy = {
        'default-src': ['\'self\'',],
        'style-src': ['\'self\'', '*.bootstrapcdn.com'],
        'script-src': ['\'self\'', 'https://www.google.com/recaptcha/', 'https://www.gstatic.com/recaptcha/', '*.bootstrapcdn.com', 'https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js', 'https://code.jquery.com/jquery-3.3.1.min.js', 'http://www.geoplugin.net/'],
        'frame-src': "https://www.google.com/recaptcha/",
    },
    content_security_policy_nonce_in=['script-src', 'style-src']
)

app.config.from_object(Config)
app.config.from_object(os.environ['APP_SETTINGS']) #changes when environment changes (e.g. testing to staging)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app) #initalizes a connection to the db
mail = Mail(app)

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
    return render_template("view.html", form=form, numPosts=Note.getAllNotes(), totalNumLikes = Note.getTotal("likes"), totalNumDislikes = Note.getTotal("dislikes"), totalNumViews = Note.getTotal(), mostLiked = Note.getTopRanks("likes")[0].numLikes, mostDisliked = Note.getTopRanks("dislikes").numDislikes)

@app.route('/smile', methods=['GET', 'POST'])
def smile():
    form = VoteForm()
    if "randomNote" not in session: #this is temporary; once site gets up and going, will find better way to counter botting
        session["randomNote"] = toJSON(Note.getRandomNote())
    if form.validate_on_submit():
        tempNote = Note.getNote(session["randomNote"]["lookupId"])
        if form.like.data:
            tempNote.update({"numLikes": tempNote.numLikes + 1})
        elif form.dislike.data:
            tempNote.update({"numDislikes": tempNote.numDislikes + 1})
        session.clear()
        return redirect('/smile')
    return render_template("smile.html", notez = Note.getNote(session["randomNote"]["lookupId"]), form=form)

@app.route('/rankings', methods=['GET'])
def rankings():
    return render_template("rankings.html", notes=Note.getTopRanks("likes"))

@app.route('/report', methods=['GET', 'POST'])
def report():
    form = ReportForm()
    ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    #print(request.environ.get('HTTP_X_REAL_IP', request.remote_addr))
    if form.validate_on_submit(): #form.method == 'POST'
         #request.get_json()["ip"]
        id = Note.getNote(session["randomNote"]["lookupId"]).lookupId
        comments = ""
        if request.form:
            comments = request.form["comments"]
        session.clear()
        msg = Message("Someone reported a post!", sender="roger.ji.32021@gmail.com", recipients=["gomeme.bob@gmail.com"])
        msg.body = "Note UUID: " + id + "\n" + "Comments: " + comments + "\n" + "IP Address: " + ip
        mail.send(msg)
        return render_template("success.html")
    try:
        return render_template("report.html", form=form, note=Note.getNote(session["randomNote"]["lookupId"]), ip=ip)
    except:
        return render_template("error/403.html"), 403

@app.route('/about', methods=['GET'])
def about():
    return render_template("about.html")

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
    return render_template('error/404.html'), 404

@app.errorhandler(403)
def access_forbidden(error):
    return render_template('error/403.html')

if __name__ == '__main__': #only runs if you actually call app.py (if importing app.py to another file and run, __name__ != '__main__')
    app.run()
