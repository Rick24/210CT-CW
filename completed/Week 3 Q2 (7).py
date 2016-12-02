#Write a recursive function to check if a number n is prime

prime = int(input('Input a number:\n'))

def findingprime(prime, F = 3):
    if prime < 2:
        return False
    elif (prime == 3) or (prime == 2):
        return True
    elif (prime % 2) == 0:
        return False
    elif (prime % F) == 0:
        return False
    elif (F > (prime / 2)):
        return True
    else:
        return (findingprime(prime, F + 2))


print(findingprime(prime))
