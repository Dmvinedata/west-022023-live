#1.✅ Build out Model
# Import from sqlalchemy: PrimaryKeyConstraint, Column, String, Integer
# Import from sqlalchemy.ext.declarative, declarative_base  
from sqlalchemy import (PrimaryKeyConstraint, Column, String, Integer, ForeignKeyConstraint)
from sqlalchemy.ext.declarative import declarative_base

#1.a ✅ Initialize declarative_base and save it to a variable called Base
Base = declarative_base()
#  Creating our connection to MAP our schema we are about to create to our database


#1.b ✅ Create a class Pet that inherits from Base
    # So now the Pet Model has all the properties/methods of the declarative_base()
class Pet(Base):

    # Set the "__tablename__" to 'pets
    __tablename__ = "pets"
    # * CREATE TABLE IF NOT EXISTS pets ()

    # setting a class attribute to the tablename of "pets"

    # Add table args for a primary key constraint based off the id
    __table_args__ = (PrimaryKeyConstraint("id"),)
    # __table_args__ = (PrimaryKeyConstraint("id"),ForeignKeyConstraint("owner_id"))

    #Create the following columns
    # * id INTEGER PRIMARY KEY, name TEXT, species, TEXT, owner_id INTEGER ...
    # * self.name = name ....
    id = Column(Integer()) 
    # id = Column(Integer(), primary_key=True) 
    # id -> type integer
    # name -> type string
    name = Column(String())
    # species -> type string
    species = Column(String())
    # breed -> type string
    breed = Column(String())
    # temperament -> type string
    temperament = Column(Integer())
    # owner_id -> integer 
    owner_id = Column(Integer())


    #add a __repr__ method that returns a string containing the id, name, species, breed and temperament of our class
    def __repr__(self):
        # replaces the print out of an instance to anything you want
        return f"""
            id:\t\t{self.id}
            Name:\t{self.name}
            Species:\t{self.species}
            Breed:\t{self.breed}
            Temp:\t{self.temperament}
        """
    
# print(Pet(name="bill", species="human", breed="dog?", temperament=7, owner_id=1))
#Note: Nothing further goes in this file.
# The following will generate a number of folders and files

#2.✅ Migrations 
#  What are Migrations?
#   - The communication between sqlalchemy and our tables
#       - The process of moving data between our databases
# In the app directory run `alembic init migrations`
# Your directory structure should look like the following 
# └── migrations
#     └── versions
#     ├── env.py
#     ├── README
#     ├── script.py.mako
# ├── alembic.ini
# ├── console.py
# └── models.py

#2.b Configuration
    # In alembic.ini, find `sqlalchemy.url`` and set it to `sqlalchemy.url = sqlite:///pet_app.db`
    # In env.py, find `target_metadata` and add `from models import Base` above it. Next, set target_metadata to `target_metadata = Base.metadata`

#2.c ✅ Generate a migration by running `alembic revision --autogenerate -m "Added Pet model"`
    # pet_app.db should have been added to your file structure

# Run `alembic upgrade head` to migrate all of our tables to the database

    # Take the time to review the migration and verify the database with SQLite Explorer or DB Browser

# 3✅ Head to debug.py to test out CRUD actions. 
