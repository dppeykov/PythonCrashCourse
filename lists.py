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
