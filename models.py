from app import db
import datetime
from random import randint

class Note(db.Model):
    __tablename__ = "notes"

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(100), nullable="False")
    name = db.Column(db.String(50))
    createdAt = db.Column(db.DateTime)

    def __init__(self, message, name="Anonymous"):
        self.message = message
        self.name = name
        self.createdAt = datetime.datetime.utcnow()

    def add(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def getRandomNote():
        return Note.query.get(randint(1, Note.query.count()))

    def __repr__(self): #repr returns the object
        return "<Message: {} & Name: {} & id: {}>".format(self.message, self.name, self.id)
