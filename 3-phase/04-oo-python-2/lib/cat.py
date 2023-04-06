""" 
  What is Object Inheritance?
    - Takinig a functionality and importing into other class
      - Real World
        - Cat is TYPE/SubClass to a Pet

 """
from lib.pet import *


class Cat(Pet):

    def __init__(self, name, age, breed, temperament, indoor):
        # # self.name = name
        # Go to the SuperClass, and re-initialize with all of the SuperClasses Properties
        # super() == Pet
        super().__init__(name, age, breed, temperament)
        # ipdb.set_trace()
        self.indoor = indoor
        # pass

    def is_indoor(self):
        print(f'{self.name} is not allowed outside') if self.indoor else print(
            f'{self.name} isnt allowed inside.')

    def print_pet_details(self):
        # super() == PetInstance
        # this print_pet_details is referencing the PARENT's method
        super().print_pet_details()
        print(f'''
            indoor:{self.indoor}
        ''')


# 6✅. Create a subclass of Pet called Cat
    # import Pet from lib.pet
    # Update the instance in debug.py to rose = Cat('rose', 11, 'domestic longhair', 'sweet', 'rose.jpg', True)

# 8✅. Create __init__ that takes all the parameters from Pet and a parameter called indoor
    # Use super to pass the Pet parameters to the super class
    # Add an indoor attribute

# 7✅. Create a method unique to the Cat subclass called talk which returns the string "Meowwwwwww"

# 9✅. Stretch: Create a method called print_pet_details, to match the print_pet_details in Pet
        # Add super().print_pet_details() and print the indoor attribute
