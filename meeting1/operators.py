##Operators:

#Operators allow us to perform various operations on variables and values.

#Arithemetic(mathematical) Operators:
"""
Operators:
    +	Addition            x + y
    -	Subtraction	        x - y
    *	Multiplication	    x * y
    /	Division            x / y
    %	Modulus	            x % y
    **	Exponentiation	    x ** y
    //	Floor division	    x // y

"""
#Example: (adding two variables)
#INPUT:
a = 5;
b = 2;
print(a + b) #OUTPUT: 7

#Assignment Operators:
"""
    Operator    Example         
        =          x = 2   (x = 2) 
        +=         x += 2  (x = x + 2)
        -=         x -= 2  (x = x - 2)
        *=         x *= 2 (x = x * 2)
        
        similarly the following operators are also utilized: /=, %=, //=, **=, &=.
"""


#Comparision Operators:
#These operators are used to compare any two declared values.
"""
Operators:
    ==	    Equal	                            x == y	
    !=	    Not equal	                        x != y	
    >	    Greater than	                    x > y	
    <	    Less than	                        x < y	
    >=	    Greater than or equal to	        x >= y	
    <=	    Less than or equal to	            x <= y

"""


#Logical Operators:
"""
Operator:
1. and ->  Returns true if BOTH statements are true
    
    Example:
        x = 10
        INPUT: x > 5 and x < 20
        OUTPUT: true
    
2. or ->   Returns true if AT LEAST one statement is true

    Example:
        x = 10
        INPUT: x < 5 or x < 20
        OUTPUT: true

3. not ->  Reverses the result (returns false if value is true) 

    Example:
        x = 10
        INPUT: not(x > 5 and x < 20)
        OUTPUT: false
"""


#Identity Operators:
"""
Operators:
1. is       ->  returns true if x = y (both variables are same object)
2. is not   ->  returns true if x != y (variables are distinct objects)

"""

#Membership Operators:

"""
Operators:

1. in       ->  Returns True if a sequence with the specified value is present in the object (x in y)

2. not in   -> Returns True if a sequence with the specified value is not present in the object (x not in y)

"""