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
from flask import Flask, jsonify, make_response, request
from flask_migrate import Migrate
from flask_restful import Api, Resource
from models import db, Song


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

# @app.route("/songs")
# def index():
#     from ipdb import set_trace
#     all_songs = Song.query.all()

#     songs = []
#     for song in all_songs:
#         res = {
#             'id': song.id,
#             'title': song.title,
#             'genre': song.genre,
#             'length': song.length,
#             'plays': song.plays,
#             'created_at': song.created_at
#         }
#         songs.append(res)
        
#     return make_response(jsonify(songs), 200)

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
        

api.add_resource(Songs, "/songs")

class SongByID(Resource):

    # ! SHOW ROUTE
    # self, var_name from the route
    # def get(self, id, other):
        # return {"id": id, "other": other}
    def get(self, song_id):
        set_trace()
        found_song = Song.query.filter_by(id=song_id).first().to_dict()
        return make_response(found_song, 200)

    # ! TEST POST 
    def post(self, song_id):
        return song_id
    
# HTTP DYNAMIC ROUTING
# /song/:id
# ? IN js
# /songs/${song.id}

# in add_resource, the dynamic path is <type:var_name>
# api.add_resource(SongByID, '/songs/<int:id>/<string:other>')
api.add_resource(SongByID, '/songs/<int:song_id>')


# 4. ✅ Create a GET (All) Route
    # 4.1 Make a `get` method that takes `self` as a param.
    # 4.2 Create a `songs` array.
    # 4.3 Make a query for all songs. For each `song`, create a dictionary 
    # containing all attributes before appending to the `songs` array.
    # 4.4 Create a `response` variable and set it to: 
    #  make_response(
    #       jsonify(songs),
    #       200
    #  )
    # 4.5 Return `response`.
    # 4.6 After building the route, run the server and test in the browser.
  
# 5. ✅ Serialization
    # This is great, but there's a cleaner way to do this! Serialization will allow us to easily add our 
    # associations as well.
    # Navigate to `models.py` for Steps 6 - 9.

# 10. ✅ Use our serializer to format our response to be cleaner
    # 10.1 Query all of the songs, convert them to a dictionary with `to_dict` before setting them to a list.
    # 10.2 Invoke `make_response`, pass it the song list along with a status of 200. Set `make_response` to a 
    # `response` variable.
    # 10.3 Return the `response` variable.
    # 10.4 After building the route, run the server and test your results in the browser.
 
# 11. ✅ Create a POST Route
    # Prepare a POST request in Postman. Under the `Body` tab, select `form-data` and fill out the body 
    # of a song request. 
    
    # Create the POST route 
    # 📚 Review With Students: request object
    
    # 11.1 Create a `post` method and pass it `self`.
    # 11.2 Create a new song from the `request.form` object.
    # 11.3 Add and commit the new song.
    # 11.4 Convert the new song to a dictionary with `to_dict`
    # 11.5 Set `make_response` to a `response` variable and pass it the new song along with a status of 201.
    # 11.6 Test the route in Postman.

   
# 12. ✅ Add the new route to our api with `api.add_resource`

# 13. ✅ Create a GET (One) route
    # 13.1 Build a class called `songByID` that inherits from `Resource`.
    # 13.2 Create a `get` method and pass it the id along with `self`. (This is how we will gain access to 
    # the id from our request)
    # 13.3 Make a query for our song by the `id` and build a `response` to send to the browser.


# 14. ✅ Add the new route to our api with `api.add_resource`