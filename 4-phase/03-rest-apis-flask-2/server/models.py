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
    # Create a DateTime on creation
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    # Create and Update the DateTime on update
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    # song_samples = db.relationship("SongSample", backref="song")
    song_samples = db.relationship("SongSample", back_populates="song")

    serialize_rules = ('-created_at', '-updated_at', '-song_samples.song')
    
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
    times_used = db.Column(db.Integer)

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    # song_samples = db.relationship("SongSample", backref="sample")
    
    # TODO FIX RELATIONSHIP RECURSION
    # song_samples = db.relationship("SongSample", back_populates="sample")

    serialize_rules = ('-created_at', '-updated_at', '-song_samples.sample')

    def __repr__(self):
        return  f"id => {self.id}\n" \
                f"name => {self.name}\n" \
                f"instrument => {self.instrument}\n" \
                f"length => {self.length}\n" \
                f"times_used => {self.times_used}\n" \


class SongSample(db.Model, SerializerMixin):
    __tablename__ = "song_samples"

    id = db.Column(db.Integer, primary_key=True)
    volume = db.Column(db.Float)
    song_id = db.Column(db.Integer, db.ForeignKey("songs.id"))
    sample_id = db.Column(db.Integer, db.ForeignKey("samples.id"))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    sample = db.relationship("Sample", back_populates="song_sample")
    song = db.relationship("Song", back_populates="song_sample")
    serialize_rules = ('-created_at', '-updated_at')

    def __repr__(self):
        return  f"id => {self.id}\n" \
                f"song_id => {self.song_id}\n" \
                f"sample_id => {self.sample_id}\n" \
                f"volume => {self.volume}\n" \


# Stretch
# Create the Samples and Join Tables
