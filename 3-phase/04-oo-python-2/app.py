# Our Run File

import ipdb
from lib.pet import *

chauncy = Pet('Chauncy', 11, "mutt", "crazy")
cosmo = Pet('cosmo', 11, "beardie", "dumb")
kevin = Pet('kevin', 11, "orange cat", "really dumb")

chauncy.print_pet_details()
cosmo.print_pet_details()

chauncy.tell_pet_i_said_hello(kevin)
chauncy.tell_pet_i_said_hello(cosmo)
# chauncy.tell_pet_i_said_hello("Cosmo")

ipdb.set_trace()
print("DONE!")