
from app import db

class Tracks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True)
    genre = db.Column(db.String(64), index = True)
    image = db.Column(db.String(64), index = True)
    audio = db.Column(db.String(64), index = True)

    def __repr__(self):
        return '<Track {}'.format(self.title)

