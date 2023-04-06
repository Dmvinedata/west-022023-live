# Our Run File

import ipdb
from lib.pet import *
from lib.cat import *
from lib.dog import *

# chauncy = Dog('Chauncy', 11, "mutt", "crazy", "rawhide", False)
# cosmo = Dog('cosmo', 11, "beardie", "dumb", "Big Ball", False)

# chauncy.print_pet_details()
# cosmo.print_pet_details()

# chauncy.tell_pet_i_said_hello(kevin)
# chauncy.tell_pet_i_said_hello(cosmo)
# chauncy.tell_pet_i_said_hello("Cosmo")

# print(Pet.pet_count
# Pet.show_all_pets()
# kevin = Cat('kevin', 11, "orange cat", "really dumb", True)
# Pet.get_average_age()

# ! DECORATORS
# 1. ✅ Demonstrate First Class Functions
    # What is a First Class Function?
    # Create functions to be used as callbacks 
    # Create a higher-order function that will take a callback as an argument




# 2. ✅ Create a higher-order function that returns a function
# CLOSURE IN JS
def taskForPet():
  def feed(pet):
      return f'{pet} has been feed'
  return feed

def feed_outside(pet):
      return f'{pet} has been feed'

task = taskForPet() # is the same as just defining the feed func
# task("phil") == feed("phil")  => true
# taskForPet()("phil")

def add_to_x(x):
    def add_to_y(y):
        return x + y
    return add_to_y

def add_together(x, y):
    return x + y

# x_together = add_to_x(1,2)
# x_together = add_to_x(1,3)
# x_together = add_to_x(1,4)

x_1 = add_to_x(1) # returns a func of add_to_y, with x = 1
# x_1 = add_to_x(2) 
# x_1 = add_to_x(4) 
# add_2 = x_1(2)

# 3. ✅ Demonstrate a decorator
# Create a function that takes a function as an argument, has an inner function, and returns the inner function
# Demo examples of the decorator with and without pie syntax '@'

def coupon_calc(func, bool):
    def wrapper1():
        print("HERE")

    def wrapper(price):
        print("Base Price is $35.00/hour")
        new_price = func(price) # will get filled in with the half_off func
        print(f'Price After Coupon is ${new_price}/hour')
    return wrapper if bool else wrapper1

# Without pie syntax 
def half_off(price):
    return price / 2

# half_off_price = coupon_calc(half_off)
# half_off_price(35.00)
# With pie syntax

# @coupon_calc
# def ten_off(price):
#     return price * .9

""" 
  In JS

  const firstFunc = (x) => {
    const secondFunc = (y) => {
      return x + y
    }
    return secondFunc
  }

  const firstFunc = x => {
    return (y) => {
      x + y
    }
  }
 """

ipdb.set_trace()
print("DONE!")