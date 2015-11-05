from math import fsum

def heaviside(x):
    return 1 if fsum(x) > 0 else 0

