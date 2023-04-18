#1.✅ Update our models to include a One to Many association
# Pet >- Owner

#Import ForeignKey
from sqlalchemy import (PrimaryKeyConstraint, Column, String, Integer, Float,  DateTime, ForeignKey)

# import relationship and backref from sqlalchemy.orm 
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Pet(Base):
    __tablename__ = 'pets'
    __table_args__ = (PrimaryKeyConstraint('id'),)

    id = Column(Integer())
    name = Column(String())
    species = Column(String())
    breed = Column(String())
    temperament = Column(String())
    
    #1.a✅ Add  ForeignKey('owners.id') to owner)id
    # THe pet BELONGS_TO the owner
    owner_id = Column(Integer(), ForeignKey("owners.id"))
   
    def __repr__(self):
        return f"Id: {self.id}, " \
            + f"Name:{self.name}, " \
            + f"Species {self.species}, "\
            + f"Breed {self.breed}, "\
            + f"Species {self.temperament}"
    
    jobs = relationship("Job", backref=backref("pet"))


# ? Review
#2.✅ Migrations 
# In the app directory run `alembic init migrations`

#2.b Configuration
    # In alembic.ini, find `sqlalchemy.url`` and set it to `sqlalchemy.url = sqlite:///pet_app.db`
    # In env.py, find `target_metadata` and add `from models import Base` above it. Next, set target_metadata to `target_metadata = Base.metadata`

#2.c ✅ Generate a migration by running `alembic revision --autogenerate -m "Added Pet model"`
    # pet_app.db should have been added to your file structure


#1.b✅ Add an Owners table 

class Owner(Base):
    __tablename__  = "owners"

    # def __init__(self, ....):

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    email = Column(String())
    phone = Column(Integer())
    address = Column(String())

    def __repr__(self):
        return f"Id: {self.id}" \
            + f"Name: {self.name}" \
            + f"Email: {self.email}" \
            + f"Phone: {self.phone}" \
            + f"Address: {self.address}"
    
    #1.c✅ Associate the Pet model with the owner Model
        # relationship('Pet', backref=backref('pet'))
    # SQL => "SELECT * FROM pets WHERE pets.owner_id = {self.id}"
    pets = relationship("Pet", backref=backref("owner"))
    
    #add a __repr__ method that returns a string containing the id, name, email, phone and address of our class

#2.✅ Update your migrations by running `alembic revision --autogenerate -m` and `alembic upgrade head` 

    # Note: If you still have your database from the previous lecture, you'll need to create a migration to update the pets table 
    # After running your migrations, go build out some seeds and test your one-to-many with debug.py
# -------------------------------

#4.✅ Update our Model to have a Many to Many association
# Pet-< Jobs >- Handlers

# Create a Handlers table 
class Handler(Base):
    __tablename__ = "handlers"
    __table_args__ = (PrimaryKeyConstraint("id"),)

    id = Column(Integer())
    name = Column(String())
    email = Column(String())
    phone = Column(Integer())
    hourly_rate = Column(Float())

    def __repr__(self):
        return f"Id: {self.id}" \
            + f"Name: {self.name}" \
            + f"Email: {self.email}" \
            + f"Phone: {self.phone}" \
            + f"Address: {self.hourly_rate}"

    jobs = relationship("Job", backref=backref("handler"))

 
#Create a "jobs" table to serve as our join
class Job(Base):
    __tablename__ = "jobs"

    #Create the following columns
    id = Column(Integer(), primary_key=True)
    request = Column(String())
    date = Column(String())
    fee = Column(Float())

    pet_id = Column(Integer(), ForeignKey("pets.id"))
    handler_id = Column(Integer(), ForeignKey("handlers.id"))

    # pet = relationship("Pet", backref=backref("pets"))
    # handler = relationship("Handler", backref=backref("handlers"))
    
    def __repr__(self):
        return f"Id: {self.id}" \
            + f"request: {self.request}" \
            + f"date: {self.date}" \
            + f"fee: {self.fee}"


    #Associate the models with relationship(<ModelNameHere>, backref=backref(<TableNameHere>))
   

    #Add a __repr__ method that returns a string containing the id, request, date, notes, fee, pet_id and handler_id of our class
   
    
#5.✅ Update your migrations by running `alembic revision --autogenerate -m` and `alembic upgrade head` 

#After running your migrations, go build out some seeds and test your many to many with debug.py