#!/usr/bin/env python3
""" 
    RESTful Routing
    - Representaional State Transfer
    - A Convention for naming routes
        - To give the devs a base understanding of the API
    - Removes the confusion of route names
       # - '/all_the_songs' 

       NAME     |   HTTP VERB    |   PATH       |   Desc
        INDEX       GET             /songs      READ all the songs
        SHOW        GET             /songs/:id  READ song of :id
        CREATE      POST            /songs      CREATE a song
        UPDATE      PATCH/PUT       /songs/:id  UPDATES the song of :id with the given data
        DELETE      DELETE          /songs/:id  DELETES the song

        # Our views on the Fronted
        NEW         GET             /songs/new  DISPLAYS the form to create a new song
        EDIT        GET             /songs/:id/edit  DISPLAYS the form to EDIT a song

 """
from ipdb import set_trace
from flask import Flask, jsonify, make_response, request, abort
from flask_migrate import Migrate
from flask_restful import Api, Resource
from models import db, Song, Sample, SongSample

from werkzeug.exceptions import NotFound

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app,db)
db.init_app(app)

# 2. ✅ Initialize the Api
    # `api = Api(app)`
api = Api(app)

@app.route('/api/hello')
def hello():
    return {"Hello": "World"}

# 3. ✅ Create a song class that inherits from Resource
# * from flask import Flask, jsonify, make_response, request
# * from flask_migrate import Migrate
# * from flask_restful import Api, Resource
# import flask
#   flask.make_response()

class Songs(Resource):

    # ! INDEX ROUTE
    def get(self):
        # ! UST IMPORT the SERIALMIXIN on the models
        songs = [s.to_dict() for s in Song.query.all()]
        return make_response(songs, 200)

    # ! CREATE
    def post(self):
        # Find all our form data
        # Create a new Song Instance
        new_song = Song(
            title=request.form["title"],
            genre=request.form["genre"],
            length=int(request.form["length"]),
        )
        # add new song to db
        db.session.add(new_song)
        db.session.commit()
        # return the created song to our client
        return make_response(new_song.to_dict(), 201)
    
    def options(self):
        return "OPTIONS?"
    
    # def link(self):
    #     return "LINK"
        

api.add_resource(Songs, "/songs")

class SongByID(Resource):

    # ! SHOW ROUTE
    # self, var_name from the route
    # def get(self, id, other):
        # return {"id": id, "other": other}
    def get(self, song_id):
        found_song = Song.query.filter_by(id=song_id).first()
        if not found_song:
            # abort(404, f"Couldn't find song of id: {song_id}")
            raise NotFound
        return make_response(found_song.to_dict(), 200)


    # ! UPDATE ROUTE
    def patch(self, song_id):
        found_song = Song.query.filter(Song.id == song_id).first()
        if not found_song:
            abort(404, f"Couldn't find song of id: {song_id}")
            # == return make_response({message: "BAD ID"}, 404)
        form_data = request.get_json()
        # found_song.title = form_data["title"], etc...
        for key in form_data:
            setattr(found_song, key, form_data[key])

        db.session.add(found_song)
        db.session.commit()

        return make_response(found_song.to_dict(), 200)

    # ! DELETE ROUTE
    def delete(self, song_id):
        found_song = Song.query.filter(Song.id == song_id).first()
        if not found_song:
            abort(404, f"Couldn't find song of id: {song_id}")

        db.session.delete(found_song)
        db.session.commit()
        # set_trace()
        
        # OPTION 1 RETURN NOTHING
        return make_response({}, 204)
    
        # OPTION 2 RETURN THE DELETED INSTANCE
        # return make_response(found_song.to_dict(), 200)

    
# HTTP DYNAMIC ROUTING
# /song/:id
# ? IN js
# /songs/${song.id}

# in add_resource, the dynamic path is <type:var_name>
# api.add_resource(SongByID, '/songs/<int:id>/<string:other>')
api.add_resource(SongByID, '/songs/<int:song_id>')


class Samples(Resource):
    # ! INDEX
    def get(self):
        set_trace()
        samples = [ s.to_dict() for s in Sample.query.all()]
        return make_response(samples, 200)


api.add_resource(Samples, '/samples')

@app.errorhandler(NotFound)
def handle_not_found(err):
    return make_response({"err": err.description}, 404)
