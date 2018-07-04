class UnionFind2(object):
    # private
    def __init__(self, n):
        self.__parent = [x for x in range(n)] # at first, every id is different, every value belongs to their own group
        self.__count = n

    # find the root of p
    def find(self, p):
        if p>=0 and p<self.__count:
            while(p != self.__parent[p]):
                p = self.__parent[p]
            return p

    def isConnected(self, p, q):
        return self.find(p) == self.find(q)

    def unionElements(self, p, q):
        pRoot = self.find(p)
        qRoot = self.find(q)
        if pRoot != qRoot:
            self.__parent[pRoot] = qRoot
