# Our Run File
import ipdb
from lib.pet import Pet, CONN, CURSOR
# from lib.owner import Owner

# First need to drop tables/database
# Pet.drop_table()

# Create the Pet table with the class method
# Pet.create_table()

# Create a new instance of Pet
chauncy = Pet("Chauncy", "Dog", "Mutt", 7)
cosmo = Pet("Cosmo", "Dog", "Beardie", 3)
# Save new Pet instance to DB
chauncy.save()
cosmo.save()

print(Pet.show_all())

Pet.find_by_name("Chauncy")

ipdb.set_trace()

print("DONE!")
