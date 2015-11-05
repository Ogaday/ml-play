import unittest
from ann.ann import ANN
from ann.tests.test_graph import TestGraphBase
from ann.functions import heaviside

class TestANNBase(TestGraphBase):
    def setUp(self):
        self.G=ANN([[None]], sum)
        self.costs={(0,0):None}    # pair: cost dict.
        self.heads={0:()}
        self.tails={0:()}
        self.sources=(0,)
        self.sinks=(0,)
        self.order=1
        # Should I be returning tuples or lists?
        self.outputs={(0.1,):{0:0.1},(1,):{0:1},(5,):{0:5}}

    def testFeedforward(self):
        for inputs, output in self.outputs.items():
            self.assertEqual({i:round(o, 6) for i, o in
                              self.G.feedforward(inputs).items()},output)

#    def testFeedforward0_1(self):
#        self.assertEqual(self.G.feedforward((0.1,)), self.outputs[(0.1,)])
#
#    def testFeedforward1(self):
#        self.assertEqual(self.G.feedforward((1,)),self.outputs[(1,)])
#
#    def testFeedforward5(self):
#        self.assertEqual(self.G.feedforward((5,)),self.outputs[(5,)])

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
        self.G=ANN([[None,1,1,None,None,None],
                    [None,None,None,1,1,None],
                    [None,None,None,1,1,None],
                    [None,None,None,None,None,1],
                    [None,None,None,None,None,1],
                    [None,None,None,None,None,None]], sum)
        self.costs={(i,i):None for i in range(6)}
        rest={(0,1):1,(0,2):1,(1,3):1,(1,4):1,(2,3):1,(2,4):1,(3,5):1,(4,5):1}
        self.costs.update(rest)
        self.heads={0:(), 1:(0,), 2:(0,), 3:(1,2), 4:(1,2), 5:(3,4)}
        self.tails={0:(1,2), 1:(3,4), 2:(3,4), 3:(5,), 4:(5,), 5:()}
        self.sources = (0,)
        self.sinks = (5,)
        self.order = 6
        self.outputs={(0.1,):{5:0.4},(1,):{5:4},(5,):{5:20}}

class TestPerceptron(TestANNBase):
    """
    --->
    2
    o
     \
    3 \0  1
    o--o--o
      /
    4/
    o

    """
    def setUp(self):
        self.G=ANN([[None,   1,None,None,None],
                    [None,None,None,None,None],
                    [ 0.3,None,None,None,None],
                    [ 0.5,None,None,None,None],
                    [   1,None,None,None,None]], sum)
        self.costs={(2,0):0.3, (3,0):0.5, (4,0):1, (0,1):1}
        self.heads={2:(), 3:(), 4:(), 0:(2,3,4), 1:(0,)}
        self.tails={2:(0,), 3:(0,), 4:(0,), 0:(1,), 1:()}
        self.sources=(2,3,4)
        self.sinks=(1,)
        self.order=5
        self.outputs={(0,0,0):{1:0}, (1,1,1):{1:1.8}, (-1,1,1):{1:1.2},
                      (0.5,0.3,1):{1:1.3}, (1,1,-1):{1:-0.2}}

class TestPerceptronHeaviside(TestANNBase):
    """
    --->
    2
    o
     \
    4 \0  1
    o--o--o
      /
    3/
    o

    """
    def setUp(self):
        self.G=ANN([[None,   1,None,None,None],
                    [None,None,None,None,None],
                    [ 0.3,None,None,None,None],
                    [ 0.5,None,None,None,None],
                    [   1,None,None,None,None]], heaviside)
        self.costs={(2,0):0.3, (3,0):0.5, (4,0):1, (0,1):1}
        self.heads={2:(), 3:(), 4:(), 0:(2,3,4), 1:(0,)}
        self.tails={2:(0,), 3:(0,), 4:(0,), 0:(1,), 1:()}
        self.sources=(2,3,4)
        self.sinks=(1,)
        self.order=5
        self.outputs={(0,0,0):{1:0}, (1,1,1):{1:1}, (-1,1,1):{1:1},
                      (0.5,0.3,1):{1:1}, (1, 1, -1):{1:0}}

class TestGershenson1(TestANNBase):
    """
    --->
    0  2     4  6
    o--o-----o--o
        \   /
         \ /
          x
         / \
        /   \
    o--o-----o--o
    1  3     5  7
    """
    def setUp(self):
        self.G=ANN([[None,None,   1,None,None,None,None,None],
                    [None,None,None,   1,None,None,None,None],
                    [None,None,None,None,   1,   1,None,None],
                    [None,None,None,None,   1,   1,None,None],
                    [None,None,None,None,None,None,   1,None],
                    [None,None,None,None,None,None,None,   1],
                    [None,None,None,None,None,None,None,None],
                    [None,None,None,None,None,None,None,None]], sum)
        self.costs={(0,2):1, (1,3):1, (2,4):1, (3,5):1, (4,6):1, (5,7):1}
        self.heads={0:(), 1:(), 2:(0,), 3:(1,), 4:(2,3), 5:(2,3), 6:(4,), 7:(5,)}
        self.tails={0:(2,), 1:(3,), 2:(4,5), 3:(4,5), 4:(6,), 5:(7,), 6:(), 7:()}
        self.sources=(0,1)
        self.sinks=(6,7)
        self.order=8
        self.outputs={(1,1):{6:2, 7:2}}



# def testHeaviside(ins, weights, outs):
#        print(heaviside([i*w for i, w in zip(ins,weights)]), outs)
