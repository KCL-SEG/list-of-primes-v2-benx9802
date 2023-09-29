"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""
import math

def primes(number_of_primes):
    try:
        if number_of_primes <= 0:
            raise ValueError
        list = []
        x = 2
        while len(list) < number_of_primes:
            if ifprime(x):
                list.append(x)
            x = x+1
        return list
    except ValueError:
        print(f'Cannot use {number_of_primes}, must use a positive integer!')
        raise


def ifprime(num):
    for i in range(2,num): # for all possible factors of i
        if num % i == 0: # if it is a factor
            return False
    return True