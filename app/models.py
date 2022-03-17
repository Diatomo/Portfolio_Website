
from app import db

class Tracks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), index=True)
    genre = db.Column(db.String(64), index=True)
    image = db.Column(db.String(256))
    audio = db.Column(db.String(256))
    url = db.Column(db.String(256))
    score = db.Column(db.Integer())
    date = db.Column(db.DateTime())

    def __repr__(self):
        return '<Track {}'.format(self.title)

