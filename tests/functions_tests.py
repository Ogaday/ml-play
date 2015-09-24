#from nose.tools import *
import ann.functions as fn

def test_heaviside():
    ins = [-100, -1, -0.5, False, 0, 0.5, 1, True, 100]
    outs = [0, 0, 0, 0, 0, 1, 1, 1, 1]
    for i, o in zip(ins, outs):
        yield check_heaviside, i, o

def check_heaviside(i, o):
    assert(fn.heaviside(i) == o)
