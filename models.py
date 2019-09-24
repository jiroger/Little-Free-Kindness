from app import db
import datetime
from random import randint
import uuid
from sqlalchemy.dialects.postgresql import UUID

class Note(db.Model):
    __tablename__ = "notes"

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(100), nullable="False")
    name = db.Column(db.String(50))
    createdAt = db.Column(db.DateTime)
    numViews = db.Column(db.Integer())
    lookupId = db.Column(db.String(36))
    numLikes = db.Column(db.Integer())
    numDislikes = db.Column(db.Integer())

    def __init__(self, message, name="Anonymous"):
        self.message = message
        self.name = name
        self.createdAt = datetime.datetime.utcnow()
        self.numViews = 0
        self.lookupId = str(uuid.uuid4())
        self.numLikes = 0
        self.numDislikes = 0

    def add(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for attribute, value in data.items():
            setattr(self, attribute, value)
        db.session.commit()

    #note to self; need to implement method that makes sure that the note getrandomnote retrives
    #passes a certain upvote threshold so mean notes are hidden
    @staticmethod
    def getRandomNote():
        idNum = randint(1, Note.query.count() - 1) if Note.query.count() > 1 else Note.query.count()
        Note.query.get(idNum).numViews = Note.query.get(idNum).numViews + 1
        db.session.commit()
        return Note.query.get(idNum)

    @staticmethod
    def viewNote(inputUUID):
        """
        Returns
            String : information about the note
        """
        if Note.query.filter_by(lookupId = inputUUID).first() is not None:
            return (Note.query.filter_by(lookupId = inputUUID).first().message + ", it has been viewed "  + str(Note.query.filter_by(lookupId = inputUUID).first().numViews))
        else:
            return "Could not find the Note statistics"

    @staticmethod
    def returnNote(inputUUID):
        """
        Returns
            Note : the Note object
        """
        if Note.query.filter_by(lookupId = inputUUID).first() is not None:
            return Note.query.filter_by(lookupId = inputUUID).first()
        else:
            return "Could not find the Note"

    @staticmethod
    def getTopRanks():
        return;

    def __repr__(self): #repr returns the object
        return "<Message: {} & Name: {} & id: {} & numLikes: {} & numDislikes: {} & numViews: {}>".format(self.message, self.name, self.id, self.numLikes, self.numDislikes, self.numViews)
