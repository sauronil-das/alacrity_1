import os
from time import sleep

"""
Finding Prime Number from a given range of integers (0 - 1000000)
"""
def user_interface():
    user_input_1=input("Do you want to find a prime number or a range of prime numbers?\nPlease enter: Y for prime numbers || N for range of prime numbers: ")
    if user_input_1 in ["Y", "y", "yes"]:
        user_input_2=input("Enter Integer: ")
        get_factors(int(user_input_2))
    elif user_input_1 in ["N", "n", "no"]:
        user_input_2=input("Enter Initial Value: ")
        user_input_3=input("Enter Last Value: ")
        find_primes(int(user_input_2), int(user_input_3))
    else:
        print("Invalid input")
        sleep(1)
        os.system('clear')
        user_interface()


def is_prime(x):
    # Check if given number is prime and return True if it is, False otherwise
    if x > 1:
    # Since prime starts after 1 (unit), 0 is compopsite
        for n in range(2, x):
            if (x%n) == 0:
                #checks if number is divisible
                return False
        return True
    else:
        return False

def set_factors(x):
    #This function finds the factors of a given number
    factors = []
    for i in range(1, x+1):
        if x % i == 0:
            factors.append(i)
    return factors
def get_factors(n):
    #finds the factors of a number if it is not prime.
    if is_prime(n):
        print(f"{n} is a prime number.")
    else:
        factors = factors(n)
        print(f"{n} is not a prime number. Its factors are: {factors}")

def find_primes(first, last):
    #function to finds all prime numbers in the given range and their factors
    primes = []
    for i in range(first, last+1):
        if is_prime(i):
            primes.append(i)
            factors = set_factors(i)
            print(f"{i} is a prime number. Its factors are: {factors}")
    return primes
    
user_interface()