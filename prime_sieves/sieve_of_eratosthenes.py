import time
import math

def eratosthenes_sieve(b):
    start_time = time.time()
    primes = [True,]*b

    for j in range(2, math.ceil(math.sqrt(b))):
        if primes[j]:
            for i in range(j*j, b, j):
                    primes[i] = False
    primes = [i for i in range(2, b) if primes[i]]
    return primes


print(eratosthenes_sieve(1000000000))
"""
if __name__ == '__main__':
    n = int(input('Enter the limit for primes: \n'))
    start = time.time()
    a = eratosthenes_sieve(n)
    count = 0
    for i in range(2, n):
        if a[i]:
            count += 1
            #print(i, end=' ')
            #if count % 10 == 0:
            #   print('\n')
    with open('eratosthenes_time.txt', 'a', encoding='utf-8') as comp:
        for i in range(2, n):
            if a[i]:
                count += 1
                if (i >= int(n/10)):
                    comp.write(f'{i}\t')            #To Write to file all primes
                    if count % 10 == 0:
                        comp.write('\n')
        comp.write(f'\nExecution time is {time.time()-start}.\nThe number of primes below {n} are {count}.')
        comp.write('\n********************\n')
        comp.write('\n')
        comp.close()
    print(f'\nExecution time is {time.time()-start}.\nThe number of primes below {n} are {count}.')
"""