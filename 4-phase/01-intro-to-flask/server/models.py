# 📚 Review With Students:
    # Review models
    # Review MVC
#SQLAlchemy import
from flask_sqlalchemy import SQLAlchemy

# 📚 Review With Students:
    # What SQLAlchemy() is replacing from SQLAlchemy in phase 3
     
db = SQLAlchemy()
# ? Optional Destructuring

# 1. ✅ Create a Song Model
	# tablename = 'Songs'
class Song(db.Model):
    __tablename__ = "songs"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    genre = db.Column(db.String)
    length = db.Column(db.String)
    plays = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    created_at = db.Column(db.DateTime, onupdate=db.func.now())

# Stretch
# Create the Samples and Join Tables

# class Song()
# 2. ✅ navigate to app.py