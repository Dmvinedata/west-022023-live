# Sequence Types
# Note: use print() to execute the examples. Comment out examples after they've been demoed.
import ipdb
import os

""" 
    ! Data Structures In JavaScript
        1. Strings
        2. Objects
        3. Booleans
        4. Numbers
        5. Undefined
        6. Null
        7. Arrays (Special Objects)

 """

# ? ARRAYS
# Creating Lists
# 1. ✅ Create a list of 10 pet names
pet_names = ['Chauncy', 'Cosmo', 'Rose', 'Meow Meow Beans', 'Mr.Legumes',
             'Luke', 'Lea', 'Princess Grace', 'Spot', 'Tom', 'Mini', 'Paul']
print("\n")
print(pet_names)
print("\n")
# Reading Information From Lists
# 2. ✅ Return the first pet name
print(pet_names[0])  # Same as js

# 3. ✅ Return all pet names beginning from the 3rd index
#   ! can use a RANGE
#   ! Range is INCLUSIVE on the LEFT side and EXCLUSIVE on the Right
#   start at the Third index, and go to the end of the list, no math to find the end needed
print(pet_names[3:])
# THE SAME OUTPUT
print(pet_names[3:len(pet_names) - 1])

# 4. ✅ Return all pet names before the 3rd index
print(pet_names[0:3])
print(pet_names[:3])

# 5. ✅  Return all pet names beginning from the 3rd index and up to the 7th
print(pet_names[3:8])


# 6. ✅ Find the index of a "Luke"
# ? JS pet_names.findIndex(x => x === "Luke")
print(pet_names.index("Luke"))
# iterate through the list, return the index of the FIRST value that stasifys that arg

# 7. ✅ Reverse the original list
print(pet_names.reverse())  # .reverse() has None Return, but modifies the list
print(pet_names)


# 8. ✅ Return the frequency of a given element
li = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 11, 1, 11, 111, 1]
print(li.count(1))


print("\n")
# Updating Lists
# 9. ✅ Change the first element to all uppercase
pet_names[0] = pet_names[0].upper()
print(pet_names)


# 10. ✅ Append a new name to the list
# ? js .push(value)
pet_names.append("Oli")
print(pet_names)

# 11. ✅ Add a new name at a specific index
# ? JS ??? pet_names.splice(3, "wally")
pet_names.insert(3, "Wally")
pet_names.insert(3, "Wally")
pet_names.insert(3, "Wally")
pet_names.insert(3, "Wally")
print(pet_names)


# 12. ✅ Add two lists together
# ? JS new_list = [...pet_names, ...pet_names_2]
pet_names_2 = ["Cole", "Holden"]
new_list = pet_names + pet_names_2
print(new_list)


# 13. ✅ Remove the final element from the list
# ? JS arr.pop()
print(pet_names.pop())  # Return is the deleted element

# 14. ✅ Remove element by specific index
# ? JS ??? sadness, arr.splice(3, -1)
print(pet_names.pop(3))

# 14a. Remove All Wally
# iterate until no more wally
print(pet_names.pop(pet_names.index("Wally")))

# 15. ✅ Remove a specific element
print(pet_names.remove("Wally"))  # REturn is NONE
print(pet_names)

# 15a. ✅ Delete in Range
del (pet_names[0:3])
print(pet_names)


# 16. ✅ Remove all pet names from the list
print(pet_names.clear())  # REturn NONE
print(pet_names)

os.system('clear')

# Tuple
# 📚 Review With Students:
# Mutable, Immutable, Changeable, Unchangeable
# LIST          Tuple
# Mutatble      Immutable => Can't change it once it's created
# Change        Unchangable

# Benefits of the Tuple?
# When we want our information to remain Static
# ex, dates, months, fetching data

# 17. ✅ Create a Tuple of pet 10 ages
pet_ages = (5, 2, 6, 4, 7, 2, 8, 9, 4, 11)
print(pet_ages)


# 18. ✅ Print the first pet age
print(pet_ages[0])


# Testing Changeability
# 19. ✅ Attempt to remove an element with ".pop" (should error)
# pet_ages.pop()
# AttributeError: 'tuple' object has no attribute 'pop'


# 20. ✅ Attempt to change the first element (should error)
# pet_ages[0] = 10
# TypeError: 'tuple' object does not support item assignment

# Tuple Methods
# 21. ✅ Return the frequency of a given element
print(pet_ages.count(4))

# 22. ✅ Return the index of a given element
print(pet_ages.index(4))


# 23. ✅ Create a Range
# Note:  Ranges are primarily used in loops
# ? js for (let i = 0; i < 10; i++ ) {}
# ? js arr.forEach(x => x)
range_1 = range(0, 10)
# range from 0 to 100 by 5
range_2 = range(0, 1000000, 5)
print(range_1)
print([*range_1])
print(range_2)
# print([*range_2])


# Demo Sets (Stretch Goal)
# Set cannot have duplicated elements

# 24. ✅ Create a set of 3 pet foods
pet_foods = {"purina", "kibble", "steak"}

os.system("clear")
# ! OBJECTS
# Dictionaries
# Creating
# 25. ✅  Create a dictionary of pet information with the keys "name", "age" and "breed"
pet_info = {"name": "chauncy", "age": 11, "breed": "mutt"}
print(pet_info)

# 26. ✅  Use dict to create a dictionary of pet information with the keys "name", "age" and "breed"
# name, age, breed = "cosmo", 11, "beardie"
# pet_info_2 = dict(name=name, age=age, breed=breed)
pet_info_2 = dict(name="cosmo", age=11, breed="beardie")
print(pet_info_2)

# Reading
# 27. ✅ Print the pet attribute of "name" using bracket notation
print(pet_info['name'])
# print(pet_info['name2']) # KeyError

# 28. ✅ Print the pet attribute of "age" using ".get"
# Note: ".get" is preferred over bracket notation in most cases because it will return "None" instead of an error
print(pet_info.get("age"))
print(pet_info.get("age2"))

# Updating
# 29. ✅ Update the pets age to 12
pet_info['age'] = 12
print(pet_info)


# 30. ✅ Update the other pets age to 26
pet_info_2.update({'age': 26, "breed": "mutt"})
# pet_info_2.update({'age2': 26}) # adds a new key:val
print(pet_info_2)


# Deleting
# 30. ✅ Delete a pets age using the "del" keyword
del(pet_info["age"])
print(pet_info)


# 31. ✅ Delete the other pets age using ".pop"
pet_info_2.pop("age")
print(pet_info_2)


# 32. ✅ Delete the last item in the pet dictionary using "popitem()"
pet_info_2.popitem()
print(pet_info_2)



# Demo Loops
pet_info = [
    {
        'name': 'rose',
        'age': 11,
        'breed': 'domestic long-haired',
    },
    {
        'name': 'spot',
        'age': 25,
        'breed': 'boxer',
    },
    {
        'name': 'Meow Meow Beans',
        'age': 2,
        'breed': 'domestic long-haired',
    }
]

# 33. ✅ Loop through a range of 10 and print every number within the range


# 34. ✅ Loop through a range between 50 and 60 that iterates by 2 and print every number


# 35. ✅ Loop through the "pet_info" list and print every dictionary


# 36. ✅ Create a function that takes a list as an argument
# The function should use a "for" loop to loop through the list and print every item
# Invoke the function and pass it "pet_names" as an argument


# 37. ✅ Create a function that takes a list as an argument. (simple example)
#   The function should define a counter and set it to 0
#   Create a "while" loop
#   The loop will continue as long as the counter is less than the length of the list
#   Every loop should increase the count by 1
#   Return the counter


# 38. ✅ Create a function that updates the age of a given pet
#   The function should take a list of "dict"s, "name" and "age" as parameters
#   Create am index variable and set it to 0
#   Create a while loop
#   The loop will continue so long as the list does not contain a name matching the "name" param and the index is less then the length of the list
#   Every list will increase the index by 1
#   If the dict containing a matching name is found, update the item's age with the new age
#   Otherwise, return 'pet not found'


# map like
# 39. ✅ Use list comprehension to return a list containing every pet name from "pet_info" changed to uppercase


# find like
# 40. ✅ Use list comprehension to find a pet named spot


# filter like
# 41. ✅ Use list comprehension to find all of the pets under 3 years old


# 43. ✅ Create a generator expression matching the filter above. Compare and contrast the generator to the list comprehension.
