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
