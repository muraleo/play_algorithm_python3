class UnionFind(object):
    # private
    def __init__(self, n):
        self.__id = [x for x in range(n)] # at first, every id is different, every value belongs to their own group
        self.__count = n
    
    #public
    def find(self, p):
        if p >= 0 and p < self.__count:
            return self.__id[p]
            
    def isConnected(p, q):
        return self.find(p) == self.find(q)