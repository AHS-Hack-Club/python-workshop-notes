# Review on conditions
x = 4
print(x == 5) # OUTPUT: False
print(x > 5) # OUTPUT: False
print(x < 5) # OUTPUT: True

# While Loops
# Repeat until a condition becomes false
x = 2
while x < 5:
    print('x < 5')
    x += 1
    #this will run 3 times, because x has incremented by 1 each time we loop over the code, when x = 5, it stops repeating
    #if x is 5, x is not less than 5, so it stops
    #Takes the condition and checks if it results in True or False

variable = "hello"
while variable == "hello":
    print("hi")
    # DO NOT RUN THIS, this will go on forever, because variable will always = hello, your computer will hate you
    # Known as an infinite loop
while True:
    print("Hi")
    #the condition mentioned here is True, so it means it will iterate over it
    #this is also an infinite loop, it will print Hi forever

while True:
    print("Hi")
    break # when a computer runs break, it immediately ends the loop
    #This would only print Hi one time
