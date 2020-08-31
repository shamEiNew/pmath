#Error in endpoints at 5, 7, 11 needs to be rectified.

#REF: https://www.ams.org/journals/mcom/2004-73-246/S0025-5718-03-01501-1/S0025-5718-03-01501-1.pdf

import numpy as np
import math as mt

def atkin_sieve(b):
    a = []
    for i in np.arange(b):a.append(False)

    for x in np.arange(1, b):
        for y in np.arange(1, b):
            if x**2 < b and y**2 < b:

                    n = 4*x**2 + y**2
                    if (n <= b) and ((n % 12 == 1) or (n % 12 == 5)):  #Atkin 3.1
                        a[n] = True

                    n = 3*x**2 + y**2
                    if ((n <= b) and (n % 12 == 7)):                   #Atkin 3.2
                        a[n] = True
                
                    n = 3*x**2 - y**2
                    if (x > y and n <= b and n % 12 == 11):            #Atkin 3.3
                        a[n] = True
    r  = 5
    while(r * r < b):
        if (a[r]):
            for i in range(r * r, b, r * r): a[i] = False 
        r += 1
    return a

if __name__ == '__main__':
    n = int(input('Enter the limit for primes: \n'))
    a =  atkin_sieve(n)
    if n == 1:
        print('No primes for the given value')
    if n == 2 or n > 2:
        print(2, end = ' ')
    if n == 3 or n > 3:
        print(3, end = ' ')
    for t in range(len(a)):
        if a[t]:
            print(t, end=' ')