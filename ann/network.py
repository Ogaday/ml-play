class Perceptron:
    def __init__(self, ni, weights = None, func = heaviside):
        """
        Create a perceptron instance.
        """
        # Number of inputs
        self.ni = ni
        
        try:
            self.weights = list(weights)
            assert(len(self.weights)==ni+1)
        except TypeError:
            self.weights = [0]*(ni+1)
            
        self.func = func
            
    def activate(self, in_vec):
        in_vec = [1]+list(in_vec)
        assert(len(in_vec)==len(self.weights))
        return self.func(sum([v*w for v, w in zip(in_vec, self.weights)]))
    
    def train(self, Xtr, alpha = 0.1, iterations = 100, verbose = False):
        """
        Train the perceptron using the algorithm found on this page:
        https://en.wikipedia.org/wiki/Perceptron#Steps
        
        Xtr : numpy.array
          A two dimensional array.
        alpha : float
          The learning rate of the algorithm: how greedily the algorithm learns from the data.
        iterations : int
          Number of iterations of the algorithm.
        """
        # Assert size of Xtr is correct
        #if self.bias:
        #    assert(Xtr.shape[1] == len(self.weights))
        #else:
        #    assert(Xtr.shape[1] == len(self.weights))
            
        for i in range(iterations):
            j = i%Xtr.shape[0]
            
            # Get output
            in_vec = list(Xtr[j, :-1])
            if verbose:
                print("in_vec:", in_vec)
                print("weights:", self.weights)
            target = Xtr[j, -1]
            out = self.activate(in_vec)
            # Update weights:
            #for i, wi in enumerate(w):
            #    w[i] = wi + alpha*(row[-1]- out)*row[i]
            self.weights = [w + alpha * (target - out) * v for v, w in zip([1]+in_vec, self.weights)]
            
        # have a default alpha size
        # have a default number of iterations
        # perhaps have some arguments about other termination criteria.
    def accuracy(self, Xtr):
        results = [self.activate(row[:-1])==row[-1] for row in Xtr]
        return sum(results)/len(results)
    
class Network:
    def __init__(self, V, E, weights, func = None):
        """
        The conditions are:
         * No cycles.
         * Every vertex must be mapped to by at least one edge (ie. fully connected).
         * V must be orderable. min(V) will be set to the abstract source node from which inputs come and the
           max(V) will be set to the sink node which will collect the outputs. Therefore min(V) must not be the tail
           of any edge mapped tuple, and similarly max(V) must not be the head of any edge mapped tuple.
        """
        self.V = V
        self.E = E
        self.network = {e:0 for e in E}    # activated values on the edges. One approach for now.
        self.weights = weights
        if func:
            self.func = func
        else:
            self.func = lambda x: x
    
    def activate(self, in_vec):
        """
        Fire the neurons! With vector "in_vec", fire the neurons and return and "out_vec".
        """
        

    def fire(self, v, in_vec = None):
        """
        Maybe one day I'll make a vertex class that clear this up sometime. For now though, take a vertex, fire it
        based upon input and update the network property of Network.
        
        For the source and sink vertices, ie. the input and output vectors, edges are sorted by the rank of the
        connected vertices.
        
        RE: vertex class, can be subclassed for source and sink this fire method could be overwritten...
        """
        ins = {e for e in self.E if e[1] == v}
        outs = {e for e in self.E if e[0] == v}
        
        if ins == {}:
            # Then we are the source vertex
            sorted_outs = [(v, o) for o in [e[1] for e in outs].sort()]    # Important that we consider order here.
            if in_vec:
                for e, i in zip(sorted_outs, in_vec):
                    self.network[e] = i
            else:
                raise Exception("Input vector not defined.")
        elif outs == {}:
            # Then we are the sink vertex
            # Don't need to do anything?
            pass
        else:
            # The we are neither a source nor sink vertex and so we are a vertex in the neural network to be fired.
            val = self.func(sum([self.weights[e]*self.network[e] for e in ins]))
            for e in outs:
                self.network[e] = val