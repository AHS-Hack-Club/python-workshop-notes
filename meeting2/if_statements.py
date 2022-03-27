# If Statements
# Check for a condition and do certain code based on given condition
# Its like a filter

x = 4
if x == 5:
    print("x = 5")
#Will not print anything because x does not equal 5
if x == 4:
    print("x = 4")
#prints "x = 4"

#else is, if the if condition isn't satisfied, then it automatically does else
if x == 7:
    print("x = 7")
else:
    print("x does not equal 7")
#Do not put a condition in the else part, it will give an error
# OUTPUT: x does not equal 7

x = 5
#elif, a secondary if statement for if the if portion isn't satisfied
if x == 4:
    print("x is 4")
elif x == 5:
    print("x is 5")
#elifs need a conditions, this will print x is 5

if x == 5:
    print("x is 5")
elif x == 4:
    print("x is 4")
# this will print x is 5, because the if statement is satisfied, it won't even check if the elif is correct or not

if x == 0:
    print("x is 0")
elif x == 2:
    print("x is 2")
else:
    print("x isn't 0 or 2")
    #the else would be run because all ifs and elifs are incorrect
# I have used integers for all of these, but it works with every data type
x = "no"
if x == "yes":
    print("yes")
elif x == "maybe":
    print("maybe")
else:
    print("no")
#prints no because variable x does not equal "yes" or "maybe"
