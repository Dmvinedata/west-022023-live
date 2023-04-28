from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
db = SQLAlchemy()

class Song(db.Model, SerializerMixin):
    __tablename__  = "songs"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    genre = db.Column(db.String)
    length = db.Column(db.Integer)
    plays = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    samples = db.relationship("Sample", backref="song")

    # serialize_rules = ('-created_at', '-updated_at', '-song_samples.song')
    
    def __repr__(self):
        return  f"id => {self.id}\n" \
                f"title => {self.title}\n" \
                f"genre => {self.genre}\n" \
                f"length => {self.length}\n" \
                f"plays => {self.plays}\n" \

    
class Sample(db.Model, SerializerMixin):
    __tablename__ = "samples"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    instrument = db.Column(db.String)
    length = db.Column(db.Integer)
    volume = db.Column(db.Float)

    song_id = db.Column(db.Integer, db.ForeignKey("songs.id"))
    
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    
    serialize_rules = ('-created_at', '-updated_at', '-song_samples.sample')

    def __repr__(self):
        return  f"id => {self.id}\n" \
                f"name => {self.name}\n" \
                f"instrument => {self.instrument}\n" \
                f"length => {self.length}\n" \
                f"volumne => {self.volume}\n" \


