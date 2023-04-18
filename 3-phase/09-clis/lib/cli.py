from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import Item, Store
# from helpers import (*)

engine = create_engine('sqlite:///db/grocery_stores.db')
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
