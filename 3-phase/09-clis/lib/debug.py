from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ipdb import set_trace
from db.models import Item, Store

if __name__ == '__main__':

  engine = create_engine('sqlite:///grocery_stores.db')
  Session = sessionmaker(bind=engine)
  session = Session()
  print("Session Created...")


  set_trace()