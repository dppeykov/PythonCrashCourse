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
