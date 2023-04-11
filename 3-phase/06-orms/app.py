# Our Run File
import ipdb
from lib.pet import Pet, CONN, CURSOR
from lib.owner import Owner

# First need to drop tables/database
Pet.drop_table()
Owner.drop_table()

# Create the Pet table with the class method
Pet.create_table()
Owner.create_table()


phil = Owner("Phil", '125', 'p@p.com')
connor = Owner.create("Connor", '1412', 'c@c.com')
phil.save()
 

# Create a new instance of Pet
chauncy = Pet("Chauncy", "Dog", "Mutt", 7, connor.id)
cosmo = Pet("Cosmo", "Dog", "Beardie", 3, connor.id)
# Save new Pet instance to DB
chauncy.save()
cosmo.save()

print("Get all")
# phil.pets() because off One to MANY
phil.get_all_pets_associated()
connor.get_all_pets_associated()
 
# cosmo.owner() because of Many to ONE
cosmo.get_owner()
chauncy.get_owner()

# Pet.find_by_name("Chauncy")
# Pet.find_or_create_by("Chauncy", "Dog", "Mutt", 7, phil.id)
# Pet.find_or_create_by("Chauncy", "Dog", "Mutt", 4, connor.id)
# third_pet = Pet.find_by_id(3)
ipdb.set_trace()
# third_pet.update("Poppy", "Dog", "Poodle", 10)
# third_pet.update(name="Poppy", temperament=10)
# third_pet.delete_from_db()




print("DONE!")
