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
# LISTS - LOOPING
####################################################################################
