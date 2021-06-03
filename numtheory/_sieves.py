import math
from typing import List

def eratosthenes_sieve(b: int) -> List[int]:

    """This sieve takes an argument a positive integer 
    returns all primes less then b.

    Returns a list of primes.

    ------
    Example:

     In [1]:eratosthenes_sieve(20)
     Out[2]:[2, 3, 5, 7, 11, 13, 17, 19]
    """
    try:
        primes = [True,]*b
    except TypeError:
        raise TypeError("Expected an integer value, float given")

    for j in range(2, math.ceil(math.sqrt(b))):
        if primes[j]:
            for i in range(j*j, b, j):
                    primes[i] = False
    
    prime = list()
    for i in range(2, len(primes)):
        if primes[i]:
            prime.append(i)
    return prime

