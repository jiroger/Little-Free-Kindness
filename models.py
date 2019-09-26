from app import db
import datetime
from random import randint
import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import func, desc

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

    def getStringTime(self):
        return self.createdAt.strftime("%B %d, %Y")

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
    def getNote(inputUUID):
        """
        Returns
            Note : the Note object
        """
        if Note.query.filter_by(lookupId = inputUUID).first() is not None:
            return Note.query.filter_by(lookupId = inputUUID).first()
        else:
            return "Could not find the Note"

    @staticmethod
    def getTopRanks(pref):
        """
        Returns
            Note : the 5 most liked or disliked notes
        """
        try:
            if pref == "likes":
                return Note.query.order_by(desc(Note.numLikes)).limit(5).all()
            else:
                return Note.query.order_by(desc(Note.numDislikes)).first_or_404(description='There is no data with numDislikes')
        except:
            try:
                if pref == "likes":
                    return Note.query.order_by(desc(Note.numLikes)).all()
                else:
                    return Note.query.order_by(desc(Note.numDislikes)).first_or_404(description='There is no data with numDislikes')
            except:
                return "No notes available!"

    @staticmethod
    def getAllNotes():
        return Note.query.all()

    @staticmethod
    def getTotal(pref="total"):
        notes = Note.getAllNotes()
        count = 0
        for note in notes:
            if pref == "likes":
                count += note.numLikes
            elif pref == "dislikes":
                count += note.numDislikes
            else:
                count += note.numViews
        return count

    def __repr__(self): #repr returns the object
        return "<Message: {} & Name: {} & id: {} & numLikes: {} & numDislikes: {} & numViews: {}>".format(self.message, self.name, self.id, self.numLikes, self.numDislikes, self.numViews)
