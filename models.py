from app import db
import datetime
from random import randint
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID

class Note(db.Model):
    __tablename__ = "notes"

    id = db.Column(db.Integer, primary_key=True)

    message = db.Column(db.String(100), nullable="False")
    name = db.Column(db.String(50))
    createdAt = db.Column(db.DateTime)
    numViews = db.Column(db.Integer())
    lookupId = db.Column(UUID(as_uuid=True), default=uuid4)

    def __init__(self, message, name="Anonymous"):
        self.message = message
        self.name = name
        self.createdAt = datetime.datetime.utcnow()
        self.numViews = 0

    def add(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for attribute, value in data.items():
            setattr(self, attribute, value)
        db.session.commit()

    @staticmethod
    def getRandomNote():
        return Note.query.get(randint(1, Note.query.count()))

    @staticmethod
    def viewNote(input):
        if input == self.lookupId:
            return self.message
        else:
            return "wrong input"

    def __repr__(self): #repr returns the object
        return "<Message: {} & Name: {} & id: {}>".format(self.message, self.name, self.id)
