# For Loops
# Repeats a segment of code a given number of times

for i in range(5): # variable i can be replaced with anything
    # when repeating by a known integer then we use range()
    print('Hello World!')
# OUTPUT:

    # Hello World!
    # Hello World!
    # Hello World!
    # Hello World!
    # Hello World!
#for _ in ___:

for i in range(5):
    print(i) # you can print i (it is like a counter that starts at 0 and ends at the range number - 1)
    # OUTPUT:
        # 0
        # 1
        # 2
        # 3
        # 4
for i in 'Hack Club': # This loops throught hte code based on the number of characters in the string (9)
    # The "Hack Club" string could be replaced with a variable as well (strings and lists)
    print(i)
    # Loops through the string, so i is the character that is in the position i is in
    # OUTPUT:
        # H
        # a
        # c
        # k
        #
        # C
        # l
        # u
        # b

loopList = [7, 9, 'String', 4, 6]
for i in loopList: # When looping over a list, instead of taking each character, it takes each element
    print(i)
    # OUTPUT:
        # 7
        # 9
        # String
        # 4
        # 6

for i in range(3):
    print('Hello')
    for i in range(2): # Nested for loop, you can put loops inside of a loop, this will run somewhat how we expect
        print('Something')
# OUTPUT:
    # Hello
    # Something
    # Something
    # Hello
    # Something
    # Something
    # Hello
    # Something
    # Something
