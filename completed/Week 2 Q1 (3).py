#Write the pseudocode for a function which returns the highest perfect square which is less or equal to
#its parameter (a positive integer). Implement this in the programming language of your choice.

#imports all libraries form the math module
from math import *

def rounder(num):                           #0(5)
    print(round(floor(sqrt(num)))**2)


rounder(int(input('Input a number:\n')))    #0(1)


#floor returns the largest number that is smaller or equal to the variable
#in this case its answer

#round does the rounding

#Total big0 = 0(6)
