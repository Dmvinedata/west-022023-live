# 📚 Review With Students:
    # Review models
    # Review MVC

""" 
    Request Response Cycle?
    - Client makes a request to a server,
    - Server Reponds with some data
        - On Browser it's all GET requests
    
    MVC
    - Model
        - Server Side
        - Database/models.py
        - How an Object is structured
            - Any attributes, functions, methods, etc...
        - Blueprint of what makes a thing a thing
    - View
        - Client Side Visual
        - React/VanillaJS/Terminal
        - What displays the models to the user
    - Controller
        - Routing arm that utilzies the models and/or views
        - ReactRouter
            - POST /songs => that will hit a ROUTE defined by action and path, then will excecute a given model method
            - GET /songs => will tell the app to display all songs

    Web Servers
    - any of our localhost:port, ip 127.0.1:port...
    - A active cpu / software ready to respond to remote clients
        - json-server
        - External APIs
        - Flask run
        - React
        - Live Server

 """

#SQLAlchemy import
from flask_sqlalchemy import SQLAlchemy

# 📚 Review With Students:
    # What SQLAlchemy() is replacing from SQLAlchemy in phase 3

# essentially give us ALL of SQLAlchemy inside of this `db` variable
db = SQLAlchemy()
# ? Optional Destructing
# Model, Column, String, Integer, DateTime = db.Model, db.Column, db.String, db.Integer, db.DateTime
# Model, Column, String, Integer, DateTime = db

# 1. ✅ Create a Song Model
	# tablename = 'Songs'
    # With Columns of title:string, genre:string, length:int, plays:int, created_at:datetime, updated_at:datetime

class Song(db.Model):
    __tablename__  = "songs"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    genre = db.Column(db.String)
    length = db.Column(db.Integer)
    plays = db.Column(db.Integer, default=0)
    # Create a DateTime on creation
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    # Create and Update the DateTime on update
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return  f"id => {self.id}" \
                f"title => {self.title}" \
                f"genre => {self.genre}" \
                f"length => {self.length}" \
                f"plays => {self.plays}" \
                f"Created => {self.created_at}" \
                f"Updated => {self.updated_at}" \
    

# Stretch
# Create the Samples and Join Tables

# 2. ✅ navigate to app.py