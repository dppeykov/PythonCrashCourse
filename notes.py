####################################################################################
# HOW PYTHON WORKS
#################################################################################### 
# Python source code -->> compile step -->> bytecode -->> interpreted by the python virtual machine (virtual CPU) 
# Note: The VM is written in C and when running a python program it gets compiled to machine code, so then it can interpreter and run the bytecode

####################################################################################
# THE ZEN OF PYTHON
#################################################################################### 
# import this

# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!

####################################################################################
# STYLING CONVENTION
#################################################################################### 

# Python Enhancement Proposal (PEP) - PEP 8
# Indentation - 4 spaces -> don't mix spaces and tabs
# Line Length - less than 80 chars recommended / comments = 72 chars per line
# Blank Lines - use to organize the code


####################################################################################
# VARIABLES
####################################################################################

# Naming - can contain only letters, numbers, and underscores; can't start with a number; no spacing - use _; short & descriptive; don't use keywords 
# Just a label to a box (value) in the memory - the variable is referencing the value

message = "Hello World"
print(message)

# multiple assignments
x, y, z = 0, 0, 0 # all = 0

# constants - the value stays the same (not build-in type)
MAX_CONNECTIONS = 5000

####################################################################################
# STRINGS
####################################################################################

string_descr = "could be with ' or \" or \"\"\" for docstrings"

# Some string methods - title(), upper(), lower(), rstrip()
print("clear:", string_descr)
print("title() - capitalizing every word's first letter:", string_descr.title())
print("upper() - capitalizing all the words:", string_descr.upper())
print("lower() - lowercase:", string_descr.lower())

with_space = "   S P A C E S    "
with_space          # '   S P A C E S    '
with_space.strip() # 'S P A C E S' -->> removes the extra spaces --> for removing the spaces on the right - rstrip() or left lstrip()

# f-strings - python 3.6+
first_name = "ada"
last_name = "lovelace"
print(f"F-string: Hello, {first_name.title()} {last_name.title()}!")
print("Format method: Hello, {} {}!".format(first_name.title(), last_name.title()))

# Fomatting - \t = tab, \n = new line

####################################################################################
# NUMBERS
####################################################################################
# integers & floats
# add (+), subtract (-), multiply (*), divide (/), exponent/power (**), module (%)
# floats - any number with a decimal point - if float in the operation, the result is float

universe_age = 14_000_000_000 # can use _ to represent large numbers - python 3.6+
print(universe_age) # 14000000000


####################################################################################
# LISTS
####################################################################################

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])  # the indexes start at 0
print(bicycles[-1])
print(bicycles[::-1])  # reversing the list --> ['specialized', 'redline', 'cannondale', 'trek'] --> temp
bicycles.reverse() # reversing with method --> perm
print(bicycles)

# Changing values
motorcycles = ['honda', 'yamaha', 'suzuki']
print("Original: ", motorcycles)
motorcycles[0] = 'CHANGE'

# Add (append(el)) / Insert (insert(inx, el)) / Delete (del list[inx]) / Remove (pop(inx) & remove(value) / sort()
motorcycles.append('APPEND')

motorcycles.insert(0, 'INDEX')
print("After CHANGE, APPEND, INDEX: ", motorcycles)

del motorcycles[0]  # deletes the element at 0 -> if we want to delete an element and not use it again (otherwise use pop())
print("After DEL: ", motorcycles)

popped_motorcycle = motorcycles.pop() # without index provided, the pop method will return the last element in a list
print("Popping the last element into a variable: ", popped_motorcycle)

motorcycles.remove('suzuki') # removing by value - removes only the first occurence

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Original: ", cars)
print("Temp with sorted:", sorted(cars)) # sorts the list temporary
print("After temp: ", cars)

cars.sort() # sorts the list permanently
print("Sort() = perm: ", cars)

cars.sort(reverse=True) # sorting in reverse order
print(cars)

print("len(cars):", len(cars))

####################################################################################
# LISTS - LOOPING & LIST COMPREHENSIONS
####################################################################################

magicians = ['alice', 'david', 'carolina']
for magician in magicians:  # don't forget the colon
    print(f"{magician.title()}, that was a great trick!")   # remember the indentation
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
print("Thank you, everyone. That was a great magic show!")

for value in range(1, 5): # upper limit is not inclusive - will stop at 4
    print(value)
# range(6) -->> 0,1,2,3,4,5

# creating a list with range -->> range(lower, upper, step)
even_numbers = list(range(2, 11, 2))
print(even_numbers) # [2, 4, 6, 8, 10]

# statistics
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

# List comprehencions
squares = []

for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# list comprehensions --> creates new elements using the for loop and automatically appends them to a list
squares = [value**2 for value in range(1, 11)]
print(squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

####################################################################################
# LISTS - SLICING [begin:end:skip] & COPY
####################################################################################

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3]) # 3 not inclusive --> ['charles', 'martina', 'michael']
# print(players[:3]) # same as above - starts from the beginning = 0
print(players[-3:]) # starts from -3 and goes to the end --> ['michael', 'florence', 'eli']

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
# NOTE: friend_foods = my_foods -->> mutable - will set friend_foods pointer to the existing my_foods list

print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)


####################################################################################
# TUPLES
####################################################################################

# List of items that can't be changed = immutable
# Although you can’t modify a tuple, you can assign a new value to a variable that represents a tuple
# Use them when you want to store a set of values that should not be changed throughout the life of a program
# Tuples are iterables, so you can loop through them

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# dimensions[0] = 250 # TypeError: 'tuple' object does not support item assignment

print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100) # we can assign a new value to the tuple variable
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

my_t = (3,) # tuple with 1 element

####################################################################################
# CONDITIONALS
####################################################################################

# if conditional_test:
#     do something
# elif another_conditional_test:  # once a match is found the rest of the elif statements are not checked 
#     do something else 
# ...
# else:    # catch all statement
#     do something different  

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

#  = --> assign / == --> is equal / != --> is not equal / <=, >= --> less/greater than or equal 
# and / or / not -->> python is using the whole words 

# in / not in - checking for a value in or not in a data structure (lsit in this case)
requested_toppings = ['mushrooms', 'onions', 'pineapple']
'mushrooms' in requested_toppings # True
'mushrooms' not in requested_toppings # False

# If you want only one block of code to run, use an if-elifelse chain. 
# If more than one block of code needs to run, use a series of independent if statements.

# Multiple lists and conditionals - example:
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"\nAdding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")

####################################################################################
# DICTIONARIES
####################################################################################

# A dictionary in Python is a collection of key-value pairs
# A key’s value can be a number, a string, a list, or even another dictionary
# We can use a dictionary to group multiple different users with a similar data or multiple types of data for a single user

alien = {'color': 'green', 'points': 5}
print(alien['color'])
print(alien['points'])
# adding more values
alien['x_position'] = 0
alien['y_position'] = 25
print(alien)

# As of Python 3.7, dictionaries retain the order in which they were defined. When you
# print a dictionary or loop through its elements, you will see the elements in the same
# order in which they were added to the dictionary

alien['points'] = 30 # to change a value
print(alien)
del alien['points'] # to delete a key-value pair
print(alien)

# getting a value with get() - used to hadle errors - if we use ['key'], it returns an error and stops the execution
point_value = alien.get('points', 'No point value assigned.')
print(point_value)  # No point value assigned.   -->> points were deleted from the dictionary

# If you leave out the second argument in the call to get() and the key doesn’t exist, Python will return the value None. 
# The special value None means “no value exists.”
# This is not an error: it’s a special value meant to indicate the absence of a value.

# Looping through all the items with key and a value
for key, value in alien.items():  # could be only k,v
    print(f"\nKey: {key}")
    print(f"Value: {value}")

# Looping through the keys only
for key in alien.keys():
    print(key.title()) # title() makes the first letter capital

# Looping in order through the keys & values --> NOTE: keys() and values() return a list of the keys/values

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.") # Edward, thank you for taking the poll. ... going through all the names(keys)

# looping through all the values from a dictionary
for language in favorite_languages.values():
    print(language)

# NOTE: we can nest lists in a dictionary, dictionaries in lists and so on - to get to the values just combine the technics for the lists and dictionaries
# You should not nest lists and dictionaries too deeply - if needed, most probably a better solution exists

####################################################################################
# SETS
####################################################################################

# A set is a collection in which each item must be unique

set(favorite_languages.values()) # {'ruby', 'c', 'python'} -->> a set is also iterable, so we can loop through it

# It’s easy to mistake sets for dictionaries because they’re both wrapped in braces.
# When you see braces but no key-value pairs, you’re probably looking at a set. 
# Unlike lists and dictionaries, sets do not retain items in any specific order.

####################################################################################
# INPUT
####################################################################################

# Write clear prompts - explain well what needs to be entered

message = input("Tell me something, and I will repeat it back to you: ")
print(message) # repeats the message

# a way to do a prompt on several lines
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print(f"\nHello, {name}!")

# NOTE: the input returns a string - we can change it with int() for example if needed


####################################################################################
# WHILE LOOP + break + continue
####################################################################################

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# The break statement directs the flow of your program; you can use it to control
# which lines of code are executed and which aren’t, so the program only
# executes code that you want it to, when you want it to

# You can use the break statement in any of Python’s loops.

# Rather than breaking out of a loop entirely without executing the rest of its
# code, you can use the continue statement to return to the beginning of the
# loop based on the result of a conditional test.

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)  # prints 1 3 5 7 9 (%2 != 0)

# NOTE: ALWAYS BE VERY CAREFUL NOT TO CAUSE A INFINITE LOOP

# The while loop can be used for moving a data between lists, 
# removing all instances of a specific value from a list, filling a dictionary with user input and so on

####################################################################################
# FUNCTIONS
####################################################################################

def greet_user():
    """Display a simple greeting."""
    print("Hello")

greet_user()

# Docstrings are enclosed in triple quotes, which Python looks for when it generates documentation for the functions 

def greet_user(username): # here username is a PARAMETER (in the definition)
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")

greet_user('jesse') # here jesse is an ARGUMENT (in the function call -->> gets passed as a parameter to the function)

# You can pass arguments to your functions in a number of ways:
#  You can use positional arguments, which need to be in the same order the parameters were written; 
#  keyword arguments, where each argument consists of a variable name and a value; 
#  and lists and dictionaries of values.

# Positional arguments

def describe_pet(animal_type, pet_name): # positional arguments - the order matters
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry') # positional arguments - good to follow the same order

# Keyword arguments - key-value pair - avoids the confusion with the positions

describe_pet(animal_type='dog', pet_name='rex') # in that way the order doesn't matter - the correct values will be passed to the function
# NOTE: IMPORTANT - When you use keyword arguments, be sure to use the exact names of the parameters in the function’s definition.

# Defaul values
def describe_pet_2(pet_name, animal_type='dog'): # ALWAYS list the parameters that have default values at the end
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet_2(pet_name='willie')

# When you use default values, any parameter with a default value needs to be listed after all the parameters that don’t have default values.
#  This allows Python to continue interpreting positional arguments correctly.

#Learning GraphQL
