from graph import Graph

class ANN(Graph):
    def __init__(self, matrix, func):
        """
        Initialise an ANN object. Default behaviour is initialise an empty
        Graph.

        Arguments
        ---------
        matrix : list
          2d matrix formed by nested lists.
        directed : bool
          Boolean to change enforce symmetry of edge matrix for undirected
          graphs.
        """
        self.matrix = matrix
        self.func = func
        # Check matrix is square
        # assert(isinstance(self.matrix, list))
        # for row in self.matrix:
        #     assert(len(row) == self.order)
            # assert(isinstance(row, list))
        #    self.inputs={s:0 for s in self.sources()}

    def activate(self, V):
        """
        Activate a vertex with index V by recursively calling activate on
        vertices preceding V.

        Arguments
        ---------
        V : int
          Index of vertex.

        Returns
        -------
        output : float
        """
        # Base case
        if V in self.sources():    # in self.inputs
            return self.inputs[V]
        # Recursion case
        elif V in self.sinks():
            heads=self.heads(V)
            assert(len(heads)==1)
            v=heads[0]
            return self.cost(v,V)*self.activate(v)
        else:
            inputs = []
            for v in self.heads(V):
                inputs.append(self.cost(v,V)*self.activate(v))
            return self.func(inputs)

    def feedforward(self, vals):
        self.inputs={V:val for V, val in zip(self.sources(), vals)}
        outputs={}    # make decision regarding returning dictionaries vs list,
                      # refrring via indexes or vertices, etc.
        for V in self.sinks():
            outputs[V]=self.activate(V)
        return outputs

# Concerns: What should I be returning? Be aware of ordering - I am referring
# to vertices by indexes, but also by labels. Is that a problem?
