from sqlalchemy import create_engine, func, ForeignKey, Table, Column, Integer, Float, String

from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Item(Base):
  __tablename__ = "items"

  id = Column(Integer(), primary_key=True)
  name = Column(String())
  quantity = Column(Integer())
  unit_price = Column(Float())

  store_id = Column(Integer(), ForeignKey("stores.id"))

  def __repr__(self):
    return f'Item(id={self.id}, ' + \
        f'name={self.name}, ' + \
        f'quan={self.quantity}, ' + \
        f'price={self.unit_price})'



class Store(Base):
  __tablename__ = "stores"

  id = Column(Integer(), primary_key=True)
  name = Column(String())
  address = Column(String())

  items = relationship("Item", backref=backref("store"))
    

  def __repr__(self):
    return f'Store(id={self.id}), ' + \
        f'name={self.name}'

