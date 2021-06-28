"""
The Elgamal is asymmetric key algorithm. It's security relies solely on the fact
that discrete logarithms are hard to compute.
It uses the group of units of ring Z_n.
"""
import random.random as rd
#Key Generation
def generate_key():