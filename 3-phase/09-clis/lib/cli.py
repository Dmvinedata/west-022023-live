from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ipdb import set_trace

from models import Item, Store
from helpers import (see_items_from_store, show_all_stores, main_menu)

engine = create_engine('sqlite:///lib/grocery_stores.db')
session = sessionmaker(bind=engine)()


if __name__ == '__main__':
    # Intro: welcome to the CLI, pick a store
    print('''
  ________                                                                       
 /  _____/______  ____   ____  ___________ ___.__.                               
/   \  __\_  __ \/  _ \_/ ___\/ __ \_  __ <   |  |                               
\    \_\  \  | \(  <_> )  \__\  ___/|  | \/\___  |                               
 \______  /__|   \____/ \___  >___  >__|   / ____|                               
        \/                  \/    \/       \/                                    
_________ .__                   __                 __    _________ .____    .___ 
\_   ___ \|  |__   ____   ____ |  | ______  __ ___/  |_  \_   ___ \|    |   |   |
/    \  \/|  |  \_/ __ \_/ ___\|  |/ /  _ \|  |  \   __\ /    \  \/|    |   |   |
\     \___|   Y  \  ___/\  \___|    <  <_> )  |  /|  |   \     \___|    |___|   |
 \______  /___|  /\___  >\___  >__|_ \____/|____/ |__|    \______  /_______ \___|
        \/     \/     \/     \/     \/                           \/        \/    
''')
    print('Hello! Welcome to the grocery checkout CLI.')

  
  # CLI ACTIONS
  #   See all items from a given store
  #   Add an item to a store
  #   Delete an item froma store
  #   update a store (change the name or address)
  #   Add a new Store

    main_menu()

    # print("Choose an option")
    # print("1\t=>\tSee all Stores")
    # print("2\t=>\tSee all Items from the first store")
    # print("3\t=>\tSee all Items from a given Store")
    # first_input = input()
    # print(f"You selected {first_input}")

    # if first_input == "1":
    #     show_all_stores(all_stores)
    # elif first_input == "2":
    #     see_items_from_store(all_stores[0])
    # elif first_input == "3":
    #     which_store = input("Which store")
    #     see_items_from_store(all_stores[int(which_store) - 1])
    # else: 
    #     print("Invalid Input")