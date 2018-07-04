class UnionFind5(object):
    # private
    def __init__(self, n):
        self.__parent = [x for x in range(n)] # at first, every id is different, every value belongs to their own group
        self.__rank = [ 1 for x in range(n)] # this rank is used to record the height of each group
        self.__count = n

    # find the root of p
    def find(self, p):
        if p>=0 and p<self.__count:
            while(p != self.__parent[p]):
                p = self.__parent[self.__parent[p]] # path compression
            return p

            # Final optimization
            # if p != self.__parent[p]:
            #     self.__parent[p] = self.find(self.__parent[p])
            #     return self.__parent[p]

    def isConnected(self, p, q):
        return self.find(p) == self.find(q)

    def unionElements(self, p, q):
        pRoot = self.find(p)
        qRoot = self.find(q)
        if pRoot != qRoot:
            if self.__rank[pRoot] < self.__rank[qRoot]:
                self.__parent[pRoot] = qRoot
            elif self.__rank[pRoot] > self.__rank[qRoot]:
                self.__parent[qRoot] = pRoot
            else:
                self.__parent[pRoot] = qRoot
                rank[qRoot] += 1