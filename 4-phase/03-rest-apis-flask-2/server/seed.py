#!/usr/bin/env python3
from app import app
from models import db, Song, Sample, SongSample
from faker import Faker

with app.app_context():
    fake = Faker()
    print("Seeding 🌱...")
    print("Deleted Songs...")
    Song.query.delete()
    print("Deleted Samples...")
    Sample.query.delete()
    print("Deleted SongSamples...")
    SongSample.query.delete()

    print("Creating Songs...")
    s1 = Song(title="Number 41", genre="Rock", length=120, plays=9)
    s2 = Song(title="Mambo Number 6", genre="Funk", length=300, plays=400)
    s3 = Song(title="Never Gonna Give You Up", genre="Classic", length=500, plays=99999)
    s4 = Song(title="Rich Girl", genre="Yacht Rock", length=180, plays=5)
    s5 = Song(title="Music From Cats", genre="Musical", length=5)

    db.session.add_all([s1,s2,s3,s4, s5])
    db.session.commit()  

    print("Creating Samples...")
    sa1 = Sample(name="Big Kick",instrument="Bass Drum",length=100,times_used=100)
    sa2 = Sample(name="Trap Horns",instrument="Horn",length=5,times_used=100000000)
    sa3 = Sample(name="Damn Son, Where'd you find this",instrument="Vox",length=42,times_used=1246890)
    sa4 = Sample(name="Orchestra Hit",instrument="Strings",length=1,times_used=9)

    db.session.add_all([sa1,sa2,sa3,sa4])
    db.session.commit()

    print("Creating Joins...")
    ss1 = SongSample(song_id=s1.id, sample_id=sa1.id, volume=1.0)
    ss2 = SongSample(song_id=s2.id, sample_id=sa2.id, volume=1.0)
    ss3 = SongSample(song_id=s3.id, sample_id=sa2.id, volume=1.0)
    ss4 = SongSample(song_id=s1.id, sample_id=sa3.id, volume=1.0)

    db.session.add_all([ss1,ss2,ss3,ss4])
    db.session.commit()
    print("DONE!")
   
# 9.✅ Create some seeds for production and commit them to the database. 
# 10.✅ Run in terminal:
    # `python seed.py`
# 11.✅ run `flask shell` in the terminal 
    # from app import app
    # from models import Production
    # Check the seeds by querying Production
# 12.✅ Navigate back to app.py  