#!/usr/bin/env python3
from flask import Flask, jsonify, make_response
from flask_migrate import Migrate
from models import db, Song



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app,db)
db.init_app(app)

# `cd` into the `server` folder
# Run in Terminal
# export FLASK_APP=app.py
# export FLASK_RUN_PORT=5555
# printenv FLASK_APP FLASK_RUN_PORT
# => app.py \ 5555
# flask db init
# flask db revision --autogenerate -m 'Create tables songs'
# flask db upgrade

@app.route('/api/hello')
def hello():
    return "Hello World"

@app.route("/songs")
def index():
    from ipdb import set_trace
    all_songs = Song.query.all()

    songs = []
    for song in all_songs:
        res = {
            'id': song.id,
            'title': song.title,
            'genre': song.genre,
            'length': song.length,
            'plays': song.plays,
            'created_at': song.created_at
        }
        songs.append(res)
        
    return make_response(jsonify(songs), 200)



# 2. ✅ Initialize the Api
    # `api = Api(app)`

# 3. ✅ Create a Production class that inherits from Resource

# 4. ✅ Create a GET (All) Route
    # 4.1 Make a `get` method that takes `self` as a param.
    # 4.2 Create a `productions` array.
    # 4.3 Make a query for all productions. For each `production`, create a dictionary 
    # containing all attributes before appending to the `productions` array.
    # 4.4 Create a `response` variable and set it to: 
    #  make_response(
    #       jsonify(productions),
    #       200
    #  )
    # 4.5 Return `response`.
    # 4.6 After building the route, run the server and test in the browser.
  
# 5. ✅ Serialization
    # This is great, but there's a cleaner way to do this! Serialization will allow us to easily add our 
    # associations as well.
    # Navigate to `models.py` for Steps 6 - 9.

# 10. ✅ Use our serializer to format our response to be cleaner
    # 10.1 Query all of the productions, convert them to a dictionary with `to_dict` before setting them to a list.
    # 10.2 Invoke `make_response`, pass it the production list along with a status of 200. Set `make_response` to a 
    # `response` variable.
    # 10.3 Return the `response` variable.
    # 10.4 After building the route, run the server and test your results in the browser.
 
# 11. ✅ Create a POST Route
    # Prepare a POST request in Postman. Under the `Body` tab, select `form-data` and fill out the body 
    # of a production request. 
    
    # Create the POST route 
    # 📚 Review With Students: request object
    
    # 11.1 Create a `post` method and pass it `self`.
    # 11.2 Create a new production from the `request.form` object.
    # 11.3 Add and commit the new production.
    # 11.4 Convert the new production to a dictionary with `to_dict`
    # 11.5 Set `make_response` to a `response` variable and pass it the new production along with a status of 201.
    # 11.6 Test the route in Postman.

   
# 12. ✅ Add the new route to our api with `api.add_resource`

# 13. ✅ Create a GET (One) route
    # 13.1 Build a class called `ProductionByID` that inherits from `Resource`.
    # 13.2 Create a `get` method and pass it the id along with `self`. (This is how we will gain access to 
    # the id from our request)
    # 13.3 Make a query for our production by the `id` and build a `response` to send to the browser.


# 14. ✅ Add the new route to our api with `api.add_resource`