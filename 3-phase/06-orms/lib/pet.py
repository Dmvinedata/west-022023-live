# Stretch Goal: Include Association with Owner

# Pet Attributes:
# name: TEXT
# species: TEXT
# breed: TEXT
# temperament: TEXT

# Stretch Goal
# owner_id: INTEGER

""" 
    Warmup Questions:

    1. What is Object Inheritance?
        - A subclass/child class, takes attributes from the parent class

    2. How does the __init__ method look on the inherited class? I.e. Dog inherits from Pet
        - def __init__(self, name, age, breed, favorite_toy):
            super() is the Pet or Parent Class
            super().__init__(name, age, breed)
            # self.name = name
            # self.age = age
            self.favorite_toy = favorite_toy

    3. What are some reasons to use SQL/Databases?
        - Data to Persist
        - Relationships between different classes/tables/models
            - Foreign Keys on relationships
        - High Performance, simple to use

    4. What are some SQL Keywords and Uses?
        - CREATE TABLE IF NOT EXISTS table_name()
            - creates a table 
        - SELECT ? FROM ?
            - Read all the columns from the table(s)
        - INSERT values INTO table
            - Creates row instances
        - JOIN table_a ON some comparison
            - Usually comparing foriegn keys to primary keys
            - ?Return? of the JOIN is: 
                - Will return a COMBINED table of all the rows WITH the association
        - WHERE comparision
            - WHERE artists.name = "Black Sabbath"
        - ALTER TABLE table
        - DROP TABLE IF EXISTS table


 """

""" 
    Object Relational Mapping (ORM)

    -  Convert Database records into python (or any languages) objects / instances
    - Why?
        - Mainly for Devs to write their code in their fav langauge instead of having to always write out SQL queries
        - Makes our code more modular and reusable (DRY code)


 """


# Create Connection to DB

import sqlite3
import ipdb
CONN = sqlite3.connect("./resources.db")
CURSOR = CONN.cursor()


class Pet:
    # PRAGMA table_info(pets);
    all = []

    # ✅ 1. Add "__init__" with "name", "species", "breed", "temperament", and "id" (Default: None) Attributes
    def __init__(self, name, species, breed, temperament, id=None):
        # All of the attr are aligned with the columns in the database
        self.name = name
        self.species = species
        self.breed = breed
        # OUr id starts at None because we will update this instance with the ID from the database
        self.temperament = temperament
        self.id = id

    # ✅ 2. Add "create_table" Class Method to Create "pets" Table If Doesn't Already Exist

    @classmethod
    def create_table(cls):
        # single_line = "CREATE TABLE IF NOT EXISTS pets ( id INTEGER PRIMARY KEY, name TEXT, species TEXT, breed TEXT, temperament )"
        create_table_sql = """ 
            CREATE TABLE IF NOT EXISTS pets (
                id INTEGER PRIMARY KEY,
                name TEXT,
                species TEXT,
                breed TEXT,
                temperament INTEGER
            )
           """
        # print(create_table_sql)
        # ipdb.set_trace()
        # Take the sql string and Execute on the db
        CURSOR.execute(create_table_sql)
        print("Created Table...")

    @classmethod
    def show_all_pets(cls):
        CURSOR.execute("SELECT * FROM pets")

    # ✅ 3. Add "drop_table" Class Method to Drop "pets" Table If Exists

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS pets
        """
        CURSOR.execute(sql)
        print("Dropped Pets...")

    # ✅ 4. Add "save" Instance Method to Persist New "pet" Instances to DB

    def save(self):
        save_sql = """
            INSERT INTO pets (name, species, breed, temperament)
            VALUES (?, ?, ?, ?);
        """
        # Question Marks in the HEREDOC Strings are placeholders for args in the execute
        # ipdb.set_trace()
        CURSOR.execute(save_sql, (self.name, self.species,
                       self.breed, self.temperament))

        self.id = CURSOR.lastrowid
        Pet.all.append(self)
        print(f"Saved with id: {self.id}...")

    # ✅ 5. Add "create" Class Method to Initialize and Save New "pet" Instances to DB

    # ✅ 6. Add "new_from_db" Class Method to Retrieve Newest "pet" Instance w/ Attributes From DB

    @classmethod
    def new_from_db(cls, row):
        # Take in a row from the database
        # and Translate the row into an instance of the class
        pet_inst = cls(
            name=row[1],
            species=row[2],
            breed=row[3],
            temperament=row[4],
            id=row[0]
        )
        return pet_inst

    # ✅ 7. Add "get_all" Class Method to Retrieve All "pet" Instances From DB
    # ! For when the Database is already active, and you are just rebooting the application (python start)
    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM pets
        """
        # All_pets is a list of TUPLES directly from the DB
        all_pets = CURSOR.execute(sql).fetchall()
        # Map all pets to our class as instances
        print(all_pets)
        # Returns a list of the INSTANCES of Pet
        return [Pet.new_from_db(row) for row in all_pets]

    # ✅ 7.5 show_all
    @classmethod
    def show_all(cls):
        sql = """
            SELECT * FROM pets
        """
        # All_pets is a list of TUPLES directly from the DB
        all_pets = CURSOR.execute(sql).fetchall()
        return all_pets
 

    # ✅ 8. Add "find_by_name" Class Method to Retrieve "pet" Instance by "name" Attribute From DB

    @classmethod
    def find_by_name(cls, search):
        sql = """
            SELECT * FROM pets
            WHERE name = ?
            LIMIT 1
        """
        row = CURSOR.execute(sql, (search,)).fetchone()
        print(row)
        return row if row else None

        # If No "pet" Found, return "None"

    # ✅ 9. Add "find_by_id" Class Method to Retrieve "pet" Instance by "id" Attribute From DB
    @classmethod
    def find_by_id(cls, search_id):
        sql = """
            SELECT * FROM pets
            WHERE id = ?
            LIMIT 1
        """
        row = CURSOR.execute(sql, (search_id,)).fetchone()
        # print(row)
        return row if row else None

    # ✅ 10. Add "find_or_create_by" Class Method to:

        #  Find and Retrieve "pet" Instance w/ All Attributes

        # If No "pet" Found, Create New "pet" Instance w/ All Attributes

    # ✅ 11. Add "update" Class Method to Find "pet" Instance by "id" and Update All Attributes
