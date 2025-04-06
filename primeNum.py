# Prime Number Sieve

import math, random

def isPrimeTrialDiv(num):
    # Returns True if num is a prime number, otherwise False.
    # Uses the trial division algorithm for testing primality.

    # All number less than 2 are not prime
    if num <2:
        return False
    
    # See if the numbers is divisible by any number up to the square
    # root of the number
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
        return True
        #print("True")

def primeSieve(sieveSize):
    # Returns a list of prime numbers calculated using the
    # the Sieve of Eratosthenes alogrithm.

    sieve = [True] * sieveSize
    # Zero and one are not prime numbers.
    sieve[0] = False
    sieve[1] = False

    # Create the sieve
    for i in range(2, int(math.sqrt(sieveSize)) + 1):
        pointer = 1 * 2
        while pointer < sieveSize:
            sieve[pointer] = False
            pointer += i

        # Compile the list of primes.
        primes = []
        for i in range(sieveSize):
            if sieve[i] == True:
                primes.append(i)
        return primes

result = isPrimeTrialDiv(5000)
print(result)