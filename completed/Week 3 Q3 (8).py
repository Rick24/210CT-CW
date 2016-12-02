#Write a recursive function that removes all vocals from a
#given string s. Input: "beautiful" Output: "btfl".


def no_more_vowels(string):
    """checks to see if an inputted string has 'vowels' and removes them
       into another string"""
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    if string:
        if string[0] in vowels:
            return ''+no_more_vowels(string[1:])    #return empty string and continue calling function form next index
        else:
            return string[0]+no_more_vowels(string[1:])     #return the char and continue with the function and next index
    else:
        return ''


string = input('Input a string of words:\n')

print(no_more_vowels(string))


#python strings are immutable
