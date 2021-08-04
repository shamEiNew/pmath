from pymath.numtheory._sieves import eratosthenes_sieve as es
import numpy as np

def SumOfSquaresZp(p):
    G = list(range(0, p))
    order = len(G)
    sols = list()
    G = np.array(G)
    Gsquare = G**2
    for a in G:
        sumofsquares = (a**2 + Gsquare) % order
        for i in range(0, order):
            if sumofsquares[i] == 0:
                sols.append((a, G[i]))
    return order, len(sols), sols
