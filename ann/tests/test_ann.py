import unittest
from ann.ann import ANN
from ann.tests.test_graph import TestGraphBase

class TestANNBase(TestGraphBase):
    def setUp(self):
        self.G=ANN([[0]], sum)
        self.costs={(0,0):0}    # pair: cost dict.
        self.heads={0:()}
        self.tails={0:()}
        self.sources=(0,)
        self.sinks=(0,)
        self.order=1
        # Should I be returning tuples or lists?
        self.outputs={(0.1,):{0:0.1},(1,):{0:1},(5,):{0:5}}

    def testFeedforward0_1(self):
        self.assertEqual(self.G.feedforward((0.1,)), self.outputs[(0.1,)])

    def testFeedforward1(self):
        self.assertEqual(self.G.feedforward((1,)),self.outputs[(1,)])

    def testFeedforward5(self):
        self.assertEqual(self.G.feedforward((5,)),self.outputs[(5,)])

class TestNetSimple(TestANNBase):
    """
    --->
         1   3
         o----o
        / \  / \
     0 o   \/   o 5
        \  /\  /
         \/  \/
         o----o
         2    4
    """
    def setUp(self):
        self.G=ANN([[0,1,1,-1,-1,-1],
                    [-1,0,-1,1,1,-1],
                    [-1,-1,0,1,1,-1],
                    [-1,-1,-1,0,-1,1],
                    [-1,-1,-1,-1,0,1],
                    [-1,-1,-1,-1,-1,0]], sum)
        self.costs={(i,i):0 for i in range(6)}
        rest={(0,1):1,(0,2):1,(1,3):1,(1,4):1,(2,3):1,(2,4):1,(3,5):1,(4,5):1}
        self.costs.update(rest)
        self.heads={0:(), 1:(0,), 2:(0,), 3:(1,2), 4:(1,2), 5:(3,4)}
        self.tails={0:(1,2), 1:(3,4), 2:(3,4), 3:(5,), 4:(5,), 5:()}
        self.sources = (0,)
        self.sinks = (5,)
        self.order = 6
        self.outputs={(0.1,):{5:0.4},(1,):{5:4},(5,):{5:20}}
