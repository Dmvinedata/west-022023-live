#6✅. Create a subclass of Pet called Dog

#8✅. Create __init__ that takes all the parameters from Pet and a parameter called indoor 

#7✅. Create a method unique to the Dog subclass called talk which returns the string "Meowwwwwww"

#9✅. Stretch: Create a method called print_pet_details, to match the print_pet_details in Pet    
        #Add super().print_pet_details() and print the indoor attribute

from lib.pet import *

class Dog(Pet):
    
    def __init__(self, name, age, breed, temperament, favorite_toy, hypoallergenic):
        super().__init__(name, age, breed, temperament)
        self.favorite_toy = favorite_toy
        self.hypoallergenic = hypoallergenic

    def print_pet_details(self):
        super().print_pet_details()
        print(f'''
            favorite toy : {self.favorite_toy}
            Hypoallergenic : {"Yes" if self.hypoallergenic else "No"}
        ''')
    