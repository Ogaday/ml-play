class Graph:
    """
    Matrix representation of an edge weighted(, directed) graph.
    """

    def __init__(self, matrix=[[]], directed=True):
        """
        Initialise a Graph object. Default behaviour is initialise an empty
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
        self.directed = directed
        self.order = len(matrix)
        # Check matrix is square
        # assert(isinstance(self.matrix, list))
        for row in self.matrix:
            assert(len(row) == self.order)
            # assert(isinstance(row, list))

    def cost(self, V1, V2):
        """
        For two vertex indices, V1 and V2, return the cost of the edge from V1
        to V2.

        Arguments
        ---------
        V1 : int
          Vertex index for a vertex belonging to the Graph object.
        V2 : int
          Vertex index for a vertex belonging to the Graph object.

        Returns
        -------
        cost : float
          Weight on the edge between vertices indicated by V1 and V2.
        """
        return self.matrix[V1][V2]

    def heads(self, V):
        """
        For a vertex index V, return the vertex indices for vertices which are
        at the heads of edges connected to the vertex indicated by V.

        Arguments
        ---------
        V : int
          Vertex index for a vertex belonging to the Graph object.

        Returns
        -------
        Vertices : list
          list of vertex indices of the vertices at the heads of the edges
          connected to the vertex indicated by V.
        """
        return [i for i in range(self.order) if self.matrix[i][V] > 0]
    #replace [ ] with ( ) to create a generator: better practice, right?

    def tails(self, V):
        """
        For a vertex index V, return the vertex indices for vertices which are
        at the heads of edges connected to the vertex indicated by V.

        Arguments
        ---------
        V : int
          Vertex index for a vertex belonging to the Graph object.

        Returns
        -------
        vertices : list
          list of vertex indices of the vertices at the heads of the edges
          connected to the vertex indicated by V.
        """
        return [i for i in range(self.order) if self.matrix[V][i] > 0]
    #replace [ ] with ( ) to create a generator: better practice, right?

class UndirectedUnweightedCompleteGraph(Graph):
    def __init__(self, k):
        self.matrix=[[1 if i!=j else 0 for j in range(n)] for i in range(n)]
        self.directed=False
        self.order=k
