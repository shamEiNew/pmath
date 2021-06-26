import time
import math

def eratosthenes_sieve(limit):
    preprimes = [True,]*limit

    for j in range(2, math.ceil(math.sqrt(limit))):
        if preprimes[j]:
            for i in range(j*j, limit, j):
                    preprimes[i] = False

    list_of_primes = []
    for i in range(2, len(preprimes)):
        if preprimes[i]:
            list_of_primes.append(i)

    return list_of_primes

def sumofprimes(p):
    largest_prime = 2
    chain_length = 1

    """😂 computation goes 10^12 i guess 🤡💅   """
    for prime in p:
        for i in range(0, len(p)):
            for j in range(0, len(p)):
                if prime == sum(p[i:j+2]):
                    if (prime > largest_prime and j-i+2 >= chain_length) :
                        largest_prime = prime
                        chain_length = j-i+2
                        #print(chain_length, largest_prime)
                        
    return chain_length, largest_prime

if __name__ == '__main__':
    start_time = time.time()
    n = int(input('Enter the limit for primes: \n'))
    primes = eratosthenes_sieve(n)
    prime = sumofprimes(primes)
    print(prime)
    print(time.time()-start_time)
    
