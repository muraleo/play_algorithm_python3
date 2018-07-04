from DenseGraph import *
from SparseGraph import *
from readGraph import *

g1 = DenseGraph(13, False)
ReadGraph(g1, '/Users/wildog/Documents/workspace/algorithm_python/graph/g1.txt')
g1.show()

g2 = SparseGraph(13, False)
ReadGraph(g2, '/Users/wildog/Documents/workspace/algorithm_python/graph/g1.txt')
g2.show()