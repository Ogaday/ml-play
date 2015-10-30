import unittest
from ann.ann import ANN

class TestANNBase(unittest.TestCase):
    def setUp(self):
        self.net=ANN([[0]], sum)
        self.costs={(0,0):0}    # pair: cost dict.
        self.heads={0:()}
        self.tails={0:()}
        self.sources=(0,)
        self.sinks=(0,)

    def testCosts(self):
        # print(self.costs)
        for pair, c in self.costs.items():
            # print(pair, c)
            self.assertEqual(self.net.cost(pair[0], pair[1]), c)

    def testHeads(self):
        for V, heads in self.heads.items():
            self.assertEqual(tuple(self.net.heads(V)), heads)

    def testTails(self):
        for V, tails in self.tails.items():
            self.assertEqual(tuple(self.net.tails(V)), tails)

    def testSources(self):
        self.assertEqual(tuple(self.net.sources()), self.sources)

    def testSinks(self):
        self.assertEqual(tuple(self.net.sinks()), self.sinks)

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
        self.net=ANN([[0,1,1,-1,-1,-1],
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
