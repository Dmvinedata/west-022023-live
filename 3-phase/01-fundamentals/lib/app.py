#!/usr/bin/env python3

# 📚 Review With Students:
# Python environment set up
# Python debugging tools
# Python datatypes

# 🚨 To enable ipdb debugging, first import "ipdb"
import ipdb
# ! Can't use from outside of the virtual env
# import requests

print("Hello World")

# 1. ✅ Create a condition to check a pet's mood
# If "pet_mood" is "Hungry!", "Rose needs to be fed."
# If "pet_mood" is "Rowdy!", "Rose needs a walk."
# In all other cases, "Rose is all good."

# def funcName(parms):
# indent    pass


def check_mood(mood):
    # * LOCAL SCOPE
    # if mood is HUngry, then this
    # else if mood is rowdy, then this
    # else return all good
    if mood == 'Hungry!':
        print("Rose needs to be fed.")
    elif mood == 'Rowdy!':
        print("Rose needs a walk.")
    else:
        print("Rose is all good")

# Note => Feel free to set your own values for "pet_mood" to view various outputs.


# * GLOBAL SCOPE
pet_mood = "Hungry!"
pet_mood2 = "NOT Hungry!"
check_mood(pet_mood)
check_mood('Rowdy!')
check_mood('aghjksf!')


pet_name = "Rose"

# 2. ✅ Create a ternary operator using "pet_mood" as a condition:
# If pet_food is "Hungry!" => "Rose needs to be fed."
# In all other cases => "Rose is all good."

# ? JS "1" == 1  => true
# ? JS "1" === 1  => false
# ONLY the Exact comparasion in Python


def check_mood_ternary():
    # ? js pet_mood ? "Rose needs to be fed." : "Rose is all good."
    out = "Rose needs to be fed." if pet_mood2 == "Hungry!" else "Rose is all good"
    print(out)


check_mood_ternary()

# 3. ✅ Create a function (say_hello) that returns the string "Hello, world!"
# Test invocation of "say_hello" in ipdb using "say_hello()"
# say_hello() => "Hello, world!"


def say_hello():
    print("Hello World")


# 4. ✅ Create a function (pet_greeting) that will return a string with interpolated pet's name
# Test invocation of "pet_greeting" in ipdb using "pet_greeting()"
# pet_greeting("Rose") => "Rose says hello!"
# pet_greeting("Spot") => "Spot says hello!"
def pet_greeting(pet_name):
    # ? JS return `${pet_name} says Hello!`
    # print(f"{pet_name} says hello!")
    return (f"{pet_name} says hello!")


print(pet_greeting("Chauncy"))


# 5. ✅ Move conditional logic from Deliverable 1 into a function (pet_status) so that we may use it with different pets / moods
# Test invocation of "pet_status" in ipdb using "pet_status(pet_name, pet_mood)"
# pet_status("Rose", "Hungry!") => "Rose needs to be fed."
# pet_greeting("Spot", "Rowdy!") => "Spot needs a walk."
# pet_greeting("Bud", "Relaxed") => "Bud is all good."
def pet_status(pet_name, pet_mood):
    if pet_mood == "Hungry!":
        return f"{pet_name} needs to be fed."
    elif pet_mood == "Rowdy!":
        return f"{pet_name} needs a walk."
    else:
        return f'{pet_name} is all good'


print(pet_status("Chauncy", "Hungry!"))
print(pet_status("Chauncy", "Rowdy!"))
print(pet_status("Chauncy", "glasdjgasdjkhgdsj!"))
# Take a moment to note that "pet_name" and "pet_mood" parameters are within Local Scope and take priority over "pet_name" and "pet_mood"
# in Global Scope.

# 6. ✅ Create a function (pet_birthday) that will increment a pet's age up by 1. Use try / except to handle errors.
# If our function is given an incorrect datatype, it should handle the TypeError exception and alert the user
# pet_birthday(10) => "Happy Birthday! Your pet is now 11."
# pet_birthday("oops") => "Type Error Occurred"


def pet_birthday(age):
    try:
        new_age = age + 1
        return f"Happy Birthday! Your pet is now {new_age}"
    except TypeError:
        print("TypeError Occurred...")
    except SyntaxError:
        print("Syntax....")
    except:
        print("else error...")


def pet_birthday_2(age):
    # if age is an int
    new_age = age + 1
    return f"Happy Birthday! Your pet is now {new_age}"
    # if age is NOT an int
    # return as error message


print(pet_birthday(7))
print(pet_birthday("asfjghfghkasf"))

# Note => To view more common Python exceptions, visit https://docs.python.org/3/library/exceptions.html

# 🚨 To create an ipdb breakpoint, comment / uncomment line below:
# r = requests.get("http://example.com")
# ipdb.set_trace() ==> debugger
