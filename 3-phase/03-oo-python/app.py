# Our Run File

# Need to import the class of pet
# ? JS import Pet from "./lib/pet.py"
# ONE CLASS PER FILE
from lib.pet import * # * means to import everything from file
# from lib.dog import * 

import ipdb

chauncy = Pet('Chauncy', 11, "mutt", "crazy")
cosmo = Pet('cosmo', 11, "beardie", "dumb")
kevin = Pet('kevin', 11, "orange cat", "really dumb")

# print(chauncy.name)
# print(chauncy.age)
# print(chauncy.breed)

chauncy.print_pet_details()
cosmo.print_pet_details()

chauncy.tell_pet_i_said_hello(kevin)
chauncy.tell_pet_i_said_hello(cosmo)
# chauncy.tell_pet_i_said_hello("Cosmo")

ipdb.set_trace()
print("DONE!")