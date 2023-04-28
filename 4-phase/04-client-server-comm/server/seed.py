#!/usr/bin/env python3
from app import app
from models import db, Song, Sample

with app.app_context():
    print("Seeding 🌱...")
    print("Deleted Songs...")
    Song.query.delete()
    print("Deleted Samples...")
    Sample.query.delete()

    print("Creating Songs...")
    s1 = Song(title="Number 41", genre="Rock", length=120, plays=9)
    s2 = Song(title="Mambo Number 6", genre="Funk", length=300, plays=400)
    s3 = Song(title="Never Gonna Give You Up", genre="Classic", length=500, plays=99999)
    s4 = Song(title="Rich Girl", genre="Yacht Rock", length=180, plays=5)
    s5 = Song(title="Music From Cats", genre="Musical", length=5)

    db.session.add_all([s1,s2,s3,s4, s5])
    db.session.commit()  

    print("Creating Samples...")
    sa1 = Sample(name="Big Kick",instrument="Bass Drum",length=100, volume=1.0, song_id=s1.id)
    sa2 = Sample(name="Trap Horns",instrument="Horn",length=5, volume=1.0, song_id=s2.id)
    sa3 = Sample(name="Damn Son, Where'd you find this",instrument="Vox",length=42, volume=1.0, song_id=s2.id)
    sa4 = Sample(name="Orchestra Hit",instrument="Strings",length=1, volume=1.0, song_id=s3.id)

    db.session.add_all([sa1,sa2,sa3,sa4])
    db.session.commit()

    print("DONE!")
   
