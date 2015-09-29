#from nose.tools import *
import ann.network as net
import ann.functions

def test_pass():
    pass

def test_perceptron_activate_with_heaviside_no_weights():
    """
    Generate tests of different Perceptron instances activating using the heaviside with no weights.
    
    Method:    
     - Initialise a list of perceptrons with a different number of inputs (one to four) and no weights.
     - Generate sets of inputs with which to activate the perceptrons.
     - Generate the expected results from activating the perceptrons with such inputs and no weights.
     - Yield the check function, the input vector and output vector, which gets automatically run by nosetests    
    """
    perceptrons = [net.Perceptron(i) for i in range(1,5)]
    in_vecs = {perceptrons[0]: [[-50.7], [-1], [0], [0.5], [1], [100]],
               perceptrons[1]: [[-37.5, -3], [-1, -1], [-5, 10], [-10, 5], [0, 0], [0, 1], [5, 5], [10.5, 1005]],
               perceptrons[2]: [[-37.5, -3, -5.7], [-1, -1, -1], [-5, 10, 0], [-1, -1, 2], [-10, 5, 7], [0, 0, 0], [0, 1, 3], [5, 5, 10], [10.5, 1005, 11]],
               perceptrons[3]: [[-37.5, -3, -5.7, -10], [-1, -1, -1, -1], [-5, 10, 0, 0], [-1, -1, 2, 1], [-10, 5, 7, 8.5], [0, 0, 0, 0], [0, 1, 3, 7.5], [5, 5, 10, 100], [10.5, 1005, 11, 13.5]]}
    
    out_vecs = {perceptrons[0]: [0]*len(in_vecs[perceptrons[0]]),
                perceptrons[1]: [0]*len(in_vecs[perceptrons[1]]),
                perceptrons[2]: [0]*len(in_vecs[perceptrons[2]]),
                perceptrons[3]: [0]*len(in_vecs[perceptrons[3]])}
    for p in perceptrons:
        for i, o in zip(in_vecs[p], out_vecs[p]):
            yield check_perceptron_activate_with_heaviside_no_weights, p, i, o
    
def check_perceptron_activate_with_heaviside_no_weights(perc, in_vecs, out):
    assert(perc.activate(in_vecs) == out)
    