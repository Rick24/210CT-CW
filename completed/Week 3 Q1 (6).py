#Write the pseudocode and code for a function that reverses the words in a sentence.
#Input: "This is awesome" Output: "awesome is This". Give the Big O notation

def string_reverse(string):                             #0(n + 2)
    """a function which splits a given string and creates a new one with the input
       elements reversed"""
    words = string.split()                              #0(1)
    reverse_string = " ".join(reversed(words))          #0(n)
    print(reverse_string)                               #0(1)

string = input('type a string:\n')                      #0(1)
string_reverse(string)                                  #0(1)


#Total big0 = 0(n)
#python strings are immutable
#.split separates the inputted string into its individual elements.
#.join reassembles the elements into a new string
