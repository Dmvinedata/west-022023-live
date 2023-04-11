# Stretch Goal: Build Out Corresponding Owner Class Methods

# Owner Attributes: 
# name: string 
# phone: string 
# email: string 
# address: string

""" 
    Table Associations!

    - What are relationships between tables/models?
        - Foreign Keys exist on another table

    - Each relatioship is directional
    - EX:
        - Artist HAS_MANY Albums
        - Album BELONGS_TO (HAS_ONE) Artist
        - SQL to get all albums of this artist (id = 1)
            - SELECT * FROM albums WHERE albums.artist_id = 1;
    - ONE TO MANY RELATIONSHIP (Directional, Vector)
        - Genre => Tracks
        - Album => Tracks
        - Media Types => Tracks

    Playlist <=> Tracks
    - MANY TO MANY RELATIONSHIP (Omni-Directional, JOINs)\
    - Tracks HAS_MANY Playlists THROUGH JOIN(playlist_tracks)
    - Playlists HAS_MANY Tracks THROUGH JOIN (playlist_tracks)

    Artists HAS_MANY tracks THROUGH albums


 """


import sqlite3

CONN = sqlite3.connect('./resources.db')
CURSOR = CONN.cursor()

class Owner:

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
        self.id = None
    

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS owners (
                id INTEGER PRIMARY KEY,
                name TEXT,
                phone TEXT,
                email TEXT
            )
        """
        CURSOR.execute(sql)
        print("Created Owners table...")

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS owners
        """
        CURSOR.execute(sql)
        print("Dropped Owners...")

    
    def save(self):
        sql = """
            INSERT INTO owners (name, phone, email)
            VALUES (? , ? , ? )
        """
        CURSOR.execute(sql, (self.name, self.phone, self.email))
        self.id = CURSOR.lastrowid
        CONN.commit()
        print(f"Saved Owner to db with id={self.id}")

    @classmethod
    def create(cls, name, phone, email):
        new_owner = cls(name, phone, email)
        new_owner.save()
        return new_owner

    @classmethod
    def show_all(cls):
        sql = """
            SELECT * FROM owners
        """
        all_owners = CURSOR.execute(sql).fetchall()
        print(all_owners)

    def get_all_pets_associated(self):
        sql = """
            SELECT * FROM pets
            WHERE owner_id = ?
        """
        related_pets = CURSOR.execute(sql, (self.id,)).fetchall()
        print(related_pets)