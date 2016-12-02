#Given a sequence of n integer numbers, extract the sub-sequence of maximum
#length which is in ascending order. 210CT Coursework 2016/2017 3 of 7 11


list1 = [1, 2, 3, 4, 1, 5, 1, 6, 7]

def sublist(list1):
    """extracts all sub-strings of the list in ascending order"""
    results = []
    currentlist = []
    #if there is no list return nothing (base case)
    if(len(list1) == 0):
        return list[0]
    for i in range(len(list1)):
        #if the list is 
        if(len(currentlist) > 1):
            #when the next item is smaller that previous it moves list into
            #results and clears the currentlist varibale to be used again
            if(list1[i] < tail(currentlist)):
                results.append(currentlist)
                currentlist = []
        currentlist.append(list1[i])
    results.append(currentlist)
    return results

def tail(list):
    """takes the end of the list"""
    return list[len(list) - 1]

results = sublist(list1)
#key is the lenght of each array and reverse puts the largest at the front
#and smallest at the back
results.sort(key = len, reverse = True)
print('Input: ' + str(list1))
print('Output: ' + str(results))
print('largest list: ' + str(results[0]))
