from random import random, randint, choice as rc

from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ipdb import set_trace
from models import Item, Store

if __name__ == '__main__':

  print("Seeding 🌱...")
  print("Connecting to DB....")
  engine = create_engine('sqlite:///grocery_stores.db')
  Session = sessionmaker(bind=engine)
  session = Session()
  print("Session Created...")

  fake = Faker()
  
  print("Dropping DB...")
  session.query(Item).delete()
  session.query(Store).delete()
  session.commit()

  print("CREATING Stores....")

  s1 = Store(name=fake.name(), address=fake.address())
  s2 = Store(name=fake.name(), address=fake.address())
  
  session.add_all([s1, s2])
  session.commit()

  print("CREATING Items....")
  i1 = Item(name="Apple", quantity=rc(range(10)), unit_price=1.0, store_id=s1.id)
  i2 = Item(name="Banana", quantity=rc(range(10)), unit_price=2.2, store_id=s1.id)
  i3 = Item(name="Chicken", quantity=rc(range(10)), unit_price=3.3, store_id=s1.id)
  i4 = Item(name="Beer", quantity=rc(range(10)), unit_price=4.4, store_id=s2.id)

  session.add_all([i1,i2,i3,i4])
  session.commit()

  print("DONE!")