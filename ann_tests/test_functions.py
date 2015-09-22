from ann.functions import *

def test_heaviside():
    ins = [-100, -0.5, False, 0, 0.5, True, 100]
    outs = [0, 0, 0, 0, 1, 1, 1]
    for i, o in zip(ins, outs):
        yield check_heaviside(i, o)

def check_heaviside(i, o):
    assert(heaviside(i) == o)
