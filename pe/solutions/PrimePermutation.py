import primesum as ps
import numpy as np
from time import time
start_time = time()
a =  ps.eratosthenes_sieve(10000)
a = [a[i] for i in range(0, len(a)) if len(str(a[i]))>=4]

max_diff = max([np.abs(a[i]-a[j]) for i in range(0, len(a)) for j in range(0, len(a)) if i!=j])
min_diff = min([np.abs(a[i]-a[j]) for i in range(0, len(a)) for j in range(0, len(a)) if i!=j])

primes = list()
for d in range(min_diff, max_diff):
    for prime in a:
        if (prime + d in a) and (prime + 2*d) in a:
            if set(str(prime)) == set(str(prime+d)) == set(str(prime+2*d)):
                primes.append(prime)
                print(f"{prime}, {prime + d}, {prime + 2* d}")
print(time()-start_time)