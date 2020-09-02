import time

def eratosthenes_sieve(b):
    primes = [True,]*b

    for j in range(2, b):
        if primes[j]:
            for i in range(j*j, b, j):
                    primes[i] = False

    return primes

if __name__ == '__main__':
    n = int(input('Enter the limit for primes: \n'))
    start = time.time()
    a = eratosthenes_sieve(n)
    count = 0
    for i in range(2, n):
        if a[i]:
            count += 1
            print(i, end=' ')
            if count % 10 == 0:
                print('\n')

    print(f'\nExecution time is {time.time()-start}. \nThe number of primes below {n} are {count}.')
