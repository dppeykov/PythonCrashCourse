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
