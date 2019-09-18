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
# add (+), subtract (-), multiply (*), divide (/), exponent/power (**)
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
