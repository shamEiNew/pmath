import typing
import functools
import numpy as np
from decimal import Decimal
from fractions import Fraction as fracs
from sympy import *



def trackcalls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.has_been_called = True
        return func(*args, **kwargs)
    wrapper.has_been_called = False
    return wrapper

def using_floor(alpha, k=15):
    quotients = list()

    

    i=0

    while i<k:
        quotients.append(np.floor(alpha))
        alpha = 1/(alpha-np.floor(quotients[i]))
        i+=1
    return list(map(int, quotients))

def euclid_method(a: int, b: int):
    quotients = []
    gcd_val = 1

    if b >= a:
        quotients.append(0)
        temp = a
        a=b
        b=temp

    while b != 0:
        q = a//b
        quotients.append(q)
        r = a%b
        if r == 0:gcd_val = b
        a = b
        b = r
    return quotients

@trackcalls
def GCD(a:int,b:int)-> int:
    if (a%b == 0) and (a > b):
        return b
    return euclid_method(a, b)

def convergents(cf: list,k=None):
    p = [cf[0], cf[1]*cf[0]+1]
    q = [1, cf[1]]

    #Calculate p_k and q_k
    for i in range(2, len(cf)):
        p.append(cf[i]*p[i-1]+p[i-2])
        q.append(cf[i]*q[i-1]+q[i-2])

    #Writing all convergents
    convergent  = [fracs(p[i],q[i]) for i in range(0, len(cf))]

    if k is not None:
        return convergent[k]
    return convergent


def continued_fraction(x, _rational=True, k=15)-> list[int]:

    def infinite_continued_fraction(k):
        return using_floor(float(sympify(x)), k)

    def finite_continued_fraction():
        return euclid_method(fracs(x).numerator, fracs(x).denominator)

    
    if _rational:
        return finite_continued_fraction()
    else:
        return infinite_continued_fraction(k)
    
    