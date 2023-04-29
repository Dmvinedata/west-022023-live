#!/usr/bin/env python3

# Running React Together 
    # Verify that gunicorn and honcho have been added to the pipenv
    # Create Procfile.dev in root
        # in Procfile.dev add:
            # web: PORT=3000 npm start --prefix client
            # api: gunicorn -b 127.0.0.1:5000 --chdir ./server app:app
        # In Terminal, cd into root and run:
            # `honcho start -f Procfile.dev`


from ipdb import set_trace
from flask import Flask, make_response, request, abort
from flask_migrate import Migrate
from flask_restful import Api, Resource
from models import db, Song, Sample

# from flask_cors import CORS
from werkzeug.exceptions import NotFound

# Import CORS from flask_cors, invoke it and pass it app
#   Start up the server / client and navigate to client/src/App.js


app = Flask(__name__)
# CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app,db)
db.init_app(app)

api = Api(app)

@app.route('/api/hello')
def hello():
    return {"Hello": "World"}

class Songs(Resource):

    # ! INDEX ROUTE
    def get(self):
        songs = [s.to_dict() for s in Song.query.all()]
        # songs = []
        # for s in Song.query.all():
            # songs.append("title": s.title, "genre": s.)
        
        return make_response(songs, 200)

    # ! CREATE
    def post(self):
        form_data = request.get_json()
        #4.✅ Add a try except, try to create a new song. 
        # If a ValueError is raised call abort with a 422 and pass it the validation errors.
        try: 
            new_song = Song(
                title=form_data["title"],
                genre=form_data["genre"],
                length=int(form_data["length"]),
            )
        except (NameError, ValueError) as err:
            # set_trace()
            abort(422, err.args[0])

        db.session.add(new_song)
        db.session.commit()
        return make_response(new_song.to_dict(), 201)
    

api.add_resource(Songs, "/songs")

class SongByID(Resource):

    # ! SHOW ROUTE
    def get(self, song_id):
        found_song = Song.query.filter_by(id=song_id).first()
        if not found_song:
            abort(404, f"Couldn't find song of id: {song_id}")
        return make_response(found_song.to_dict(), 200)


    # ! UPDATE ROUTE
    def patch(self, song_id):
        found_song = Song.query.filter(Song.id == song_id).first()
        if not found_song:
            abort(404, f"Couldn't find song of id: {song_id}")
        form_data = request.get_json()
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
        return make_response({}, 204)
    
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
