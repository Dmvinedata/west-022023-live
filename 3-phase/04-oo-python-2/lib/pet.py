#!/usr/bin/env python3

class Pet:
    
    def __init__(self, name, age, breed, temperament):
        self.name = name
        self.age = age
        self.breed = breed
        self.temperament = temperament
        self.is_cool = True

    def print_pet_details(self):
        print(f'''
            name:{self.name}
            age:{self.age}
            breed:{self.breed}
            temperament:{self.temperament}
            image_url:{self.image_url}
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
    

