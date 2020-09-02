#REF: https://www.ams.org/journals/mcom/2004-73-246/S0025-5718-03-01501-1/S0025-5718-03-01501-1.pdf

import numpy as np
import time

def atkin_sieve(b):
    primes = [False,]*(b+1)
    #for i in np.arange(b+1):primes.append(False)

    for x in np.arange(1, b):
        for y in np.arange(1, b):
            if x**2 < b and y**2 < b:

                    n = 4*x**2 + y**2
                    if (n <= b) and (n % 12 == 1 or n % 12 == 5):       #Atkin_3.1
                        primes[n] = True

                    n = 3*x**2 + y**2
                    if ((n <= b) and (n % 12 == 7)):                    #Atkin_3.2
                        primes[n] = True
                
                    n = 3*x**2 - y**2
                    if (x > y and n <= b and n % 12 == 11):            #Atkin_3.3
                        primes[n] = True
    m = 5
    while(m*m < b):                                                    #Removing composites
        if primes[m]:
            for c in range(m*m, b,m):
                    primes[c] = False 
        m += 1
    return primes

if __name__ == '__main__':
    n = int(input('Enter the limit for primes: \n'))
    start = time.time()
    a =  atkin_sieve(n)
    if n == 1:
        print('No primes for the given value')
    if n == 2 or n > 2:
        print(2, end = ' ')
    if n == 3 or n > 3:
        print(3, end = ' ')
    count = 2
    for t in range(len(a)):
        if a[t]:
            count += 1
            print(t, end=' ')
            if count % 10 == 0:
                print('\n')
    
    print(f"\nExecution time = {time.time()-start}. \nThe total number of primes below {n} are {count}")