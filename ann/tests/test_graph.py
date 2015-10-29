import unittest
from ann.graph import Graph

print(__name__)
class TestClass(unittest.TestCase):
    def test(self):
        pass

class TestGraphBase(unittest.TestCase):
    def setUp(self):
        self.arg=5
        self.out=5

    def testExpectedOutputs(self):
        "This test should pass"
        self.assertEqual(self.arg, self.out)

class TestGraphSimple(TestGraphBase):
    """
      o----o
     / \  / \
    o   \/   o
     \  /\  /
      \/  \/
       o---o
    """
    def setUp(self):
        self.arg=6
        self.out=6
