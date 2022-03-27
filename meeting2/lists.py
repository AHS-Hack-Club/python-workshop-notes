# Lists
# A list of multiple values assigned to one variable (a list of cars would be name cars but include Volvo, Toyota, Honda, etc.)

list = [] # creates a blank list (no values)
list = ['String', 1, 0.3, False] # An list can contain any data types in it (Boolean, String, Integer, Float)

# list[0] is "String"
# list[2] is 0.3

list.append('Hello') # This adds hello as the last "element" in the list
print(list) # OUTPUT: ["String", 1, 0.3, False, "Hello"]

list.pop(3) # Removes the element in the given position (the 4th element)
print(list) # OUTPUT: ["String", 1, 0.3, "Hello"]

list.remove('String') # Removes the value specified from the list
print(list) # OUTPUT: [ 1, 0.3, "Hello"]
