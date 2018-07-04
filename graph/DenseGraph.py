# adjacency matrix
class DenseGraph(object):
    # n: number of points
    # directed: this graph is directed or not
    def __init__(self, n, directed):
        self.__n = n
        self.__m = 0
        self.__directed = directed
        self.__g = [[0 for x in range(n)] for y in range(n)] # initialize a two dimensional array


    # return how many vector does this graph has
    def v(self):
        return self.__n

    # return how many edges does this graph has
    def e(self):
        return self.__m

    # add new edge between vector v and vector w
    def addEdge(self, v, w):
        if v >= 0 and v < self.__n and w >=0 and w < self.__n:
            if self.__directed is False:
                self.__g[v][w] = 1
                if not self.hasEdge(v, w):
                    self.__m += 1
        else:
            raise Exception("Vector not in the graph!")

    # check if there is an edge between v and w
    def hasEdge(self, v, w):
        if v >= 0 and v < self.__n and w >=0 and w < self.__n:
            return self.__g[v][w]
        else:
            raise Exception("Vector not in the graph!")

    def show(self):
        for i in self.__g:
            print(i)
