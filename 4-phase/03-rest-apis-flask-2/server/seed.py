#!/usr/bin/env python3
from app import app
from models import db, Song
from faker import Faker

with app.app_context():
    fake = Faker()
    print("Seeding 🌱...")
    Song.query.delete()
    print("Deleted Songs...")

    print("Creating Songs...")
    s1 = Song(title="Number 41", genre="Rock", length=120, plays=9)
    s2 = Song(title="Mambo Number 6", genre="Funk", length=300, plays=400)
    s3 = Song(title="Never Gonna Give You Up", genre="Classic", length=500, plays=99999)
    s4 = Song(title="Rich Girl", genre="Yacht Rock", length=180, plays=5)
    s5 = Song(title="Music From Cats", genre="Musical", length=5)

    db.session.add_all([s1,s2,s3,s4, s5])
    db.session.commit()

    for song in [s1,s2,s3,s4, s5]:
        print(song)
    print("DONE!")
   
# 9.✅ Create some seeds for production and commit them to the database. 
# 10.✅ Run in terminal:
    # `python seed.py`
# 11.✅ run `flask shell` in the terminal 
    # from app import app
    # from models import Production
    # Check the seeds by querying Production
# 12.✅ Navigate back to app.py  