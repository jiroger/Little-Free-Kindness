import os
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS']) #changes when environment changes (e.g. testing to staging)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app) #initalizes a connection to the db

from models import Note

@app.route('/', methods=["GET", "POST"])
def hello():
    return render_template("index.html")

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

if __name__ == '__main__': #only runs if you actually call app.py (if importing app.py to another file and run, __name__ != '__main__')
    app.run()
