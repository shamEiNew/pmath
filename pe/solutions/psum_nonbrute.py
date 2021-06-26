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

def sumofprimes(p, n):
    largest_prime = 2
    chain_length = 1
    largest_index = max([i for i in range(2, len(p)) if sum(p[:i]) < n])
    
    for i in range(0, largest_index):
        for j in range(0, largest_index):
            temp = sum(p[i:j+2])
            if temp in p:
                if (temp > largest_prime and j-i+2 >= chain_length) :
                    largest_prime = temp
                    chain_length = j-i+2
                    #print(chain_length, largest_prime)
                        
    return chain_length, largest_prime

if __name__ == '__main__':
    
    n = 100
    while n <= 1000000:
        start_time = time.time()
        primes = eratosthenes_sieve(n)
        prime = sumofprimes(primes, n)
        print(prime)
        print(time.time()-start_time)
        n*=10
    
