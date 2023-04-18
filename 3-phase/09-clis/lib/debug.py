from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ipdb import set_trace
from models import Item, Store

from helpers import see_items_from_store

if __name__ == '__main__':

  engine = create_engine('sqlite:///grocery_stores.db')
  Session = sessionmaker(bind=engine)
  session = Session()
  print("Session Created...")

  all_items = session.query(Item).all()
  all_stores = session.query(Store).all()

  # CLI ACTIONS
  #   See all items from a given store
  #   Add an item to a store
  #   Delete an item froma store
  #   update a store (change the name or address)
  #   Add a new Store

  # When this option is picked
  # run this helper
  see_items_from_store(all_stores[0])

  set_trace()