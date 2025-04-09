# Prime Number Sieve

import math, random

class Style():
  RED = "\033[31m"
  GREEN = "\033[32m"
  BLUE = "\033[34m"
  YELLOW = "\033[33m"
  MAGENTA = "\033[35m"
  CYAN = "\033[36m"
  RESET = "\033[0m"

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
    
def rabinMiller(num):
    # Returns True id the number is a prime number.
    if num % 2 == 0 or num < 2:
        return False # Rabin-Miller does not work on even integers.
    if num == 3:
        return True
    s = num - 1
    t = 0
    while s % 2 == 0:
        # Keep halving s until it is odd 
        # and use t to count how many times we halve s)
        s = s // 2
        t += 1
    for trials in range(5):
    # Try to falsify numbers primality 5 times.
        a = random.randrange(2, num - 1)
        v = pow(a, s, num)
        if v != 1: # This test does not apply if v is 1.
            i = 0
            while v != (num - 1):
                return False
            else:
                i = i + 1
                v = (v ** 2) % num
    return True
    
LOW_PRIMES = primeSieve(100)

def isPrime(num):
    # Return True if number is a prime number. This function does a
    # quicker primality check before calling rabinMiller().
    if (num < 2):
        return False # 0 and 1, are negative numbers and not prime
    for prime in LOW_PRIMES:
        if (num % prime == 0):
            return False
        
        # If all else flase, call RabinMiller() to determine if the
        # number is prime.
        return rabinMiller(num)

def generateLargePrime(keysize=1024):
    # Return a random prime number that is keysize bits in size.
    while True:
        num = random.randrange(2**(keysize-1), 2**(keysize))
        if isPrime(num):
            return num
        
print("Which Prime Function would you like to run?")
print("===========================================")
print(f"{Style.RED}1 - Trial Division{Style.RESET}")
print(f"{Style.GREEN}2 - Eratosthenes Algorithm{Style.RESET}")
print(f"{Style.BLUE}3 - Rabin-Miller{Style.RESET}")
print(f"{Style.YELLOW}4 - Generate a large prime{Style.RESET}")
print(f"==========================================")

primeSelection = input(f"{Style.RED}Selection:{Style.RESET}")
if primeSelection == 1:
    numCheck = input(f"{Style.RED}Please enter a number to check:{Style.RESET}")
    result = isPrimeTrialDiv(int(numCheck))
    print("Prime Number Check: ", result)

elif primeSelection == 2:
    numCheck = input(f"{Style.RED}Please enter a number to check: {Style.RESET}")
    result = primeSieve(int(numCheck))
    print("Prime Number Check: ", result)

elif primeSelection == 3:
numCheck = input("Please enter a number to check: ")
result = isPrime(int(numCheck))
print("Prime Number Check: ", result)

print(f"{Style.RED}ONE{Style.RESET}")