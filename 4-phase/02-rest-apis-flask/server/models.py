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

    def __repr__(self):
        return  f"id => {self.id}\n" \
                f"title => {self.title}\n" \
                f"genre => {self.genre}\n" \
                f"length => {self.length}\n" \
                f"plays => {self.plays}\n" \
                f"Created => {self.created_at}\n" \
                f"Updated => {self.updated_at}\n" \
    

# Stretch
# Create the Samples and Join Tables
