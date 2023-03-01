import os
from time import sleep

"""
Finding Prime Number from a given range of integers (0 - 1000000)
"""
def user_interface():
    user_input_1=input("Do you want to find a prime number or a range of prime numbers?\nPlease enter: Y for prime numbers || N for range of prime numbers: ")
    if user_input_1 in ["Y", "y", "yes"]:
        user_input_2=input("Enter Integer: ")
        handle_input(int(user_input_2))

    elif user_input_1 in ["N", "n", "no"]:
        user_input_2=input("Enter Initial Value: ")
        user_input_3=input("Enter Last Value: ")
        primes = find_primes(int(user_input_2), int(user_input_3))
        print(primes)
    else:
        print("Invalid input")
        sleep(1)
        os.system('clear')
        user_interface()


def is_prime(x):
    return len(get_factors(x, True)) == 0

def get_factors(x, stopOnFirst = False):
    #This function finds the factors of a given number
    factors = []
    for i in range(2, x):
        if x % i == 0:
            factors.append(i)
            if stopOnFirst:
                break
    return factors

def handle_input(n):
    #finds the factors of a number if it is not prime.
    if is_prime(n):
        print(f"{n} is a prime number.")
    else:
        factors = get_factors(n)
        print(f"{n} is not a prime number. Its factors are: {factors}")

# ex oflast
def find_primes(first, last):
    #function to finds all prime numbers in the given range and their factors
    primes = []
    for i in range(first, last):
        if is_prime(i):
            primes.append(i)
    return primes
    
user_interface()
# start