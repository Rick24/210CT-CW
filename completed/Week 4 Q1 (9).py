#Adapt the binary search algorithm so that instead of outputting whether
#a specific value was found, it outputs whether a value within an interval
#(specified by you) was found.

list1 = [0, 1, 2, 8, 13, 17, 19, 32, 42]
lowitem = int(input('Input a lower bound value\n'))
highitem = int(input('Input a higher bound value\n'))

def binarySearch(list1, lowitem, highitem,):
    """an adapted binary search which will find values between a specified range"""
    lenght = len(list1)                     #lenght = 9
    midpoint = round(lenght / 2)            #midpoint = 13
    if lenght == 0:
        return False
    #if size of the list is 1 and not in the list return false
    if lenght == 1 and list1[midpoint] != (lowitem or highitem):
        return False
    #if the item is in the middle of the list return true
    if list1[midpoint] >= lowitem and list1[midpoint] <= highitem:
        return True
    #if midpoint is larger than highitem recall function with everything
    #before midpoint in the list
    elif list1[midpoint] > highitem:
        return binarySearch(list1[:midpoint], lowitem, highitem)
    #if midpoint is smaller than lowitem recall function with everything
    #after the midpoint
    elif list1[midpoint] < lowitem:
        return binarySearch(list1[midpoint:], lowitem, highitem)
    else:
        return False

    
print(list1)
print(binarySearch(list1, lowitem, highitem,))
