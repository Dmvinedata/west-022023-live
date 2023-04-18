from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import (Base, Pet, Owner, Handler, Job)
# from faker import Faker 

if __name__ == "__main__":
  # fake = Faker()
  print("Seeding 🌱...")
  print("Connecting to DB....")
  engine = create_engine('sqlite:///pet_app.db')
  Base.metadata.create_all(engine)

  Session = sessionmaker(bind=engine)
  session = Session()
  print("Session Created...")

  session.query(Pet).delete()
  session.query(Owner).delete()
  session.query(Handler).delete()
  session.query(Job).delete()
  session.commit()

  print("CREATING OWNERS....")
  holden = Owner(name="Holden", email="h@h.com", phone="1234", address="13 Elm Street")
  connor = Owner(name="Connor", email="c@c.com", phone="5678", address="14 Elm Street")

  session.add(holden)
  session.add(connor)
  session.commit()

  print("CREATING PETS....")
  p1 = Pet(name="fake.name()", species="Dog", breed="Mutt", temperament="bad", owner_id=holden.id)
  p2 = Pet(name="chauncy", species="Dog", breed="Golden", temperament="good", owner_id=holden.id)
  p3 = Pet(name="Hank", species="Cat", breed="Orange", temperament="really bad", owner_id=holden.id)
  p4 = Pet(name="Derby", species="Aligator", breed="Croc", temperament="snuggly", owner_id=connor.id)

  # seeding_pets = []
  # species_types = ["dog", 'cat', 'aligator']

  # for pet in range(0,100):
  #     seeding_pets.append(Pet(name=fake.name(), species="Dog", breed="Mutt", temperament="bad", owner_id=holden.id))
  # session.add_all(seeding_pets)

  session.add_all([p1,p2,p3,p4])
  session.commit()

  print("CREATING HANDLERS...")
  h1 = Handler(name="wally", email="w@w.com", phone=4321, hourly_rate=1.0)
  h2 = Handler(name="shelbs", email="s@s.com", phone=5432, hourly_rate=4.5)
  h3 = Handler(name="bill", email="b@b.com", phone=4231, hourly_rate=5.7)

  session.add_all([h1,h2, h3])
  session.commit()

  print("CREATING JOBS...")

  j1 = Job(date="Feb 1st", request="Walks", fee=55.0, pet_id=p1.id, handler_id=h1.id)
  j2 = Job(date="Feb 2nd", request="Runs", fee=23.50, pet_id=p1.id, handler_id=h2.id)
  j3 = Job(date="Feb 3rd", request="Sleep", fee=5.6, pet_id=p1.id, handler_id=h3.id)
  j4 = Job(date="April 1st", request="Meds", fee=1.0, pet_id=p3.id, handler_id=h1.id)

  session.add_all([j1, j2, j3, j4])
  session.commit()

  print("DONE!")