#!/usr/bin/env python3

""" 
  Warm up questions

  1. What is self?
    - An instance of a class, that we are CALLING a method on
      - Instance Methods
"""

""" 
    What are Class methods?
      - Methods that can only be called on the Class itself
      - ex:
        - Pet.count_pets()
    What are Class Variables?
      - Properties belonging to the ENTIRE CLASS

    What are Instance variables?
      - Properties of each individual instance
        - self.variable
"""




import ipdb
class Pet:

    # Class Variables = inital_value
    print("Init Pet")
    # # pet_count = 0
    # Don't need because..........We can get the count from the all_pets list
    # !!! SINGLE SOURCE OF TRUTH
    #   Reasons for having ONE TRUE SOURCE
    #     - Keeps your data consistent
    #       - Don't have to count AND and to list
    #     - Reduces number of operations by at least 2
    #     - Reduces the amount of memory needed to store

    # Class Variables
    all_pets = []

    def __init__(self, name, age, breed, temperament):
        self.name = name
        self.age = age
        self.breed = breed
        self.temperament = temperament
        self.is_cool = True
        # Pet.pet_count += 1
        # Pet.increase_pets() # == self.increase_pets()
        # Pet.all_pets.append(self)
        Pet.add_pet(self)

    # Class Method
    @classmethod
    def increase_pets(cls):
        # print(cls)
        if cls is Pet:
            cls.pet_count += 1
        else:
            print("INSTANCES CANT CHANGE THIS")

    @classmethod
    def pet_count(cls):
        return len(cls.all_pets)

    @classmethod
    def add_pet(cls, new_pet):
        cls.all_pets.append(new_pet)

    @classmethod
    def show_all_pets(cls):
        for pet in cls.all_pets:
            pet.print_pet_details()

    @classmethod
    def get_average_age(cls):
        # MAP
        ages = list()
        for pet in cls.all_pets:
            ages.append(pet.age)
        print(sum(ages) / len(ages))

    def print_pet_details(self):
        print(f'''
            name:{self.name}
            age:{self.age}
            breed:{self.breed}
            temperament:{self.temperament}
        ''')

    def high_five(self):
        print(f"{self.name} gives you a High Five!")

    def change_temper(self, new_temperament):
        self.temperament = new_temperament
        self.print_pet_details()

    def go_back_in_time(self):
        self.age -= 1
        print(f'Happy UnBirthday {self.name}, you are now {self.age}')

    def tell_pet_i_said_hello(self, other_pet_instance):
        print(f"Hi, {other_pet_instance.name}, It's ya boi {self.name}")
