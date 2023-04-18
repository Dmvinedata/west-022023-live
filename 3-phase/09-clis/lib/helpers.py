from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Store, Item
from ipdb import set_trace

engine = create_engine('sqlite:///lib/grocery_stores.db')
session = sessionmaker(bind=engine)()

# CLI ACTIONS
#   See all items from a given store
#   Add an item to a store
#   Delete an item froma store
#   update a store (change the name or address)
#   Add a new Store

all_stores = session.query(Store).all()
all_items = session.query(Item).all()

def main_menu():
    print("Choose an option")
    print("1\t=>\tSee all Stores")
    print("2\t=>\tSee all Items from the first store")
    print("3\t=>\tSee all Items from a given Store")
    print("4\t=>\tAdd Item to a given Store")
    print("Type 'exit' to leave")
    first_input = input()
    print(f"You selected {first_input}")

    if first_input == "1":
        show_all_stores(all_stores)
        main_menu()
    elif first_input == "2":
        see_items_from_store(all_stores[0])
        main_menu()
    elif first_input == "3":
        which_store = input("Which store")
        see_items_from_store(all_stores[int(which_store) - 1])
        main_menu()
    elif first_input == "4":
        which_store = input("Which Store?\n")
        # item_name = input("Item Name: \t")
        # item_quantity = input("Quantity: \t")
        # item_unit_price = input("Unit Price: \t")
        [name, quantity, unit_price] = collect_item_info()

        selected_store = session.query(Store).filter_by(id=int(which_store)).first()
        # is the same as
        # selected_store = all_stores[int(which_store) - 1]
        # ! CREATE THE ITEM INSTANCE WITH THIS INFO
        new_item = Item(name=name, quantity=quantity, unit_price=unit_price, store_id=selected_store.id)
        session.add(new_item)
        session.commit()
        see_items_from_store(selected_store)
        main_menu()
    else: 
        print("Invalid Input")

def see_items_from_store(store):
    print(f"Here are the items from {store.name}\n")
    for item in store.items:
        print("-" * 50)
        print(item)
        print("-" * 50)

def show_all_stores(stores):
    for store in stores:
        print("-" * 50)
        print(store)
        print("-" * 50)

def commit_item(item_info):
    pass

def collect_item_info():
    item_name = input("Item Name: \t")
    item_quantity = input("Quantity: \t")
    item_unit_price = input("Unit Price: \t")
    return [item_name, int(item_quantity), float(item_unit_price)]
