#!/usr/bin/env python3
# 📚 Review With Students:
    # Request-Response Cycle
    # Web Servers and WSGI/Werkzeug

# 1. ✅ Navigate to `models.py`

# 2. ✅ Set Up Imports
	# `Flask` from `flask`
	# `Migrate` from `flask_migrate`
	# db and `Song` from `models`
from flask import Flask, jsonify, make_response
from flask_migrate import Migrate
from models import db, Song



# 3. ✅ Initialize the App
    # Add `app = Flask(__name__)`
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # Configure the database by adding`app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'`
    # and `app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False` 
    
    # Set the migrations with `migrate = Migrate(app, db)`
migrate = Migrate(app,db)
db.init_app(app)
    # Finally, initialize the application with `db.init_app(app)`

 # 4. ✅ Migrate 
	# `cd` into the `server` folder
	
    # Run in Terminal
		# export FLASK_APP=app.py
		# export FLASK_RUN_PORT=5555
    # printenv FLASK_APP FLASK_RUN_PORT
    # => app.py \ 5555
    # ! Now we will use `flask db` in place of `alembic` for our terminal commands
        # # alembic init migration
		# flask db init
        # # alembic revision --autogenerate -m Create Songs..
		# flask db revision --autogenerate -m 'Create tables songs'
        # # alembic
		# flask db upgrade

    
    # Review the database to verify your table has migrated correctly

# 5. ✅ Navigate to `seed.rb`

# 12. ✅ Routes
    # Create your route

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
        
    # if found return 200 and the data
    # else return 404 and error message
    return make_response(jsonify(songs), 200)
    # return make_response(jsonify({'error': "Bad Request"}), 404)




# 13. ✅ Run the server with `flask run` and verify your route in the browser at `http://localhost:5555/`

# 14. ✅ Create a dynamic route
# `@app.route('/songs/<string:title>')
#  def song(title):
#     return f'<h1>{title}</h1>'`


# 15.✅ Update the route to find a `song` by its `title` and send it to our browser
    
    # Before continuing, import `jsonify` and `make_response` from Flask at the top of the file.
    
    # 📚 Review With Students: status codes
        # `make_response` will allow us to make a response object with the response body and status code
        # `jsonify` will convert our query into JSON

    # `@app.route('/songs/<string:title>')
    # def song(title):
    #     song = Song.query.filter(Song.title == title).first()
    #     song_response = {
    #         "title":song.title,
    #         "genre":song.genre,
    #         }
    #     response = make_response(
    #         jsonify(song_response),
    #         200
    #     )`    

# 16.✅ View the path and host with request context

# 17.✅ Use the before_request request hook, what this hook does is up to you. You could hit a breakpoint, print something to server console or anything else you can think of.

# Note: If you'd like to run the application as a script instead of using `flask run`, uncomment the line below 
# and run `python app.py`

# if __name__ == '__main__':
#     app.run(port=5000, debug=True)