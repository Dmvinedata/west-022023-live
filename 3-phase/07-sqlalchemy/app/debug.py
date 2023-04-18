
# 3.✅ CRUD practice
# To run the file run `python3 debug.py` in the app directory
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ipdb import set_trace

from models import (Base, Pet)

if __name__ == '__main__':
    #3.1 ✅ Uncomment bellow to create the engine
    engine = create_engine('sqlite:///pet_app.db')
    Base.metadata.create_all(engine)
    #3.2 ✅ Uncomment bellow to create sessions and bind o the engine
    Session = sessionmaker(bind=engine)
    session = Session()

    #3.3 ✅  -- Creating records
        # Create a pet and save it to the data base with session.add and session.commit
    chauncy = Pet(name="Chauncy", species="Dog", breed="Mutt", temperament=7, owner_id=1)
    cosmo = Pet(name="Cosmo", species="Dog", breed="Beardie", temperament=1, owner_id=2)

    # session.add(chauncy)
    # session.add(cosmo)
    #     # Create multiple pets and bulk save them with  session.bulk_save_objects and session.commit
    # session.bulk_save_objects([chauncy, cosmo])
    # session.commit()
 

        #session.add(rose)
        #Note: bulk save will not contain the id

        #verify by checking the db 
    #3.4 ✅ Read
        # Get all with session.query
        # Print the pets 
    pets = session.query(Pet)
    # print(pets)
    print([pet for pet in pets])

        #Get all of the pet names and print them with session.query
    names = session.query(Pet.name)
    print([name for name in names])
        #Get all the pet names and print them in order with session.query and order_by
    names_in_order = session.query(Pet.name).order_by(Pet.name)
    print(f"\nQUERY: {names_in_order}\n")
    print([name for name in names_in_order])

        #Get the first pet with session.query and first
    first_pet = session.query(Pet).first()
    print(first_pet)

        #Filter pet by temperament with session.query and filter 
    temp_filter = session.query(Pet).filter(Pet.temperament == 7)
    print([pet for pet in temp_filter])

    #3.5 ✅ Update 
        # Update the pets name and print the updated pet info
  
        # Update all the pets temperament to 'cool' and print the pets 
   

    #3.6 ✅  Delete
        # Delete one item by querying the first pet, deleting it and committing it

        #delete all the pets with session.query and .delete
  

    # optional Break point for debugging and testing
    set_trace()
