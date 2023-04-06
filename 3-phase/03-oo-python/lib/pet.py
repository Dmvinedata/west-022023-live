#!/usr/bin/env python3

""" 
  Warmup Questions!

  1. What's the difference between a Tuple/List/Set?
    - Tuple => Immutable (Unchangeable), ordered
    - List  => Mutatable, can change, add, delete...
    - Set   => Immutable, each val is unique, Unordered

  2. What are the ways to get a value out of the Dict?
    - Bracket Notation  => 
      - dict["bad_key"]  => returns => KeyError
      - CAN use to update a key/value
        -dict["name"] = "new_name"
    - dict.get("key")   => 
      - dict.get("bad_key")  => returns => None
      - CAN'T update key/value
        - dict.get("name") = "Cant_make_new_name"
          - ex eval to => "wally" = "cant_new_name"
 """

""" 

  What is Object Oriented Programming (OOP)?

  - Programming principals, taht focus on data / data structures
  - Allows you to call methods on classes
  - Can initialize new objects with predeteremined properties
  - It models the program based on the Real World Associations and objects

  Classes
    - Are meant to emulate a real world thing
    - Create a Blueprint for a given 'real world' object

  Tech Company Class EX:Accounting
  - classes
    - User
      - init with a username, email, word, (opt) account?
      - Add funds to my account
      - Change account info
      - See all their investments
    - Account

 """


# Demonstrate classes 
# 1. ✅ Create a Pet class
# 2. ✅ Instantiate a few pet instance 
    # Compare the pet instances to demonstrate they are not the same object
    # Note: add 'pass' to the pet class 
import ipdb

class Pet:
    
    # Init with a name, age, breed, temperament
    # Have read AND Write access to all python attributes
    def __init__(self, name, age, breed, temperament):
        # in the init, self is ref the Pet Instance as a whole
        # we need to set all of our attributes to the self using the init args
        self.name = name
        self.age = age
        self.breed = breed
        self.temperament = temperament
        self.is_cool = True
        Pet.is_super_cool = True
        # ipdb.set_trace()
  
# 3. ✅ Demonstrate __init__ 
    # Add arguments to instances  
    # use dot notation to access their attributes 
    # update attributes with new values 

    def print_pet_details(self):
        # slf in the instance that we called this method on
        print(f'name => {self.name}')
        print(f'age => {self.age}')
        print(f'temperament => {self.temperament}')

# 4.✅ Demonstrate instance methods by creating a print_pet_details function that will print the pet attributes
#     Review the self keyword 
#     Invoke the print_pet_details on an instance 

    def high_five(self):
        print(f"{self.name} gives you a High Five!")

    def change_temper(self, new_temperament):
        self.temperament = new_temperament
        self.print_pet_details()

    def go_back_in_time(self):
        self.age -= 1
        print(f'Happy UnBirthday {self.name}, you are now {self.age}')

    def tell_pet_i_said_hello(self, other_pet_instance):
        # "cosmo".name error out
        # If a Pet Instance is passed in, then it has ALL of it's own functionality
        print(f"Hi, {other_pet_instance.name}, It's ya boi {self.name}")
        # ipdb.set_trace()
    

# Demonstrate instances 
    # Different Instances are Different Objects
# Demonstrate __init__
# Demonstrate instance method
# Demonstrate the self keyword 
# Stretch Goals
# Demonstrate object properties

# Instances 

# Run in ipdb session
# rose == cookie
#   False

#Read Attributes 
# rose.name -> rose
# rose.age -> 11

#Update
# rose.age -> 11
# rose.age = 12
# rose.age -> 12

# chauncy = Pet()....