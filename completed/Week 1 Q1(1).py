#Write a function that randomly shuffles an array of integers and explain the rationale
#behind its implementation.

#import random module
import random

initArray = [5,3,8,6,1,9,2,7]                       #0(1)
numList = [5,3,8,6,1,9,2,7]                         #0(1)
numOfSwaps = len(numList) * 5                       #0(1)
sizeOfList = len(numList)                           #0(1)

def swap(a, b):                                     #0(3)
    """a function which swaps values of 3 varibles between each other"""
    temp = numList[a]                               #0(1)
    numList[a] = numList[b]                         #0(1)
    numList[b] = temp                               #0(1)
        
for i in range(0, numOfSwaps):                      #0(n)         
    position1 = random.randrange(0, sizeOfList)     #0(1)
    position2 = random.randrange(0, sizeOfList)     #0(1)
    swap(position1, position2)

print("Initial array " + str(initArray))            #0(1)
print("Final array " + str(numList))                #0(1)

#randrange returns a randomly selected element
#range iterates over numbers 0 - numOfSwaps

#Total Big0 = 0(n)
