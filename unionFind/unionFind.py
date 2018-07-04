class UnionFind(object):
    # private
    def __init__(self, n):
        self.__id = [x for x in range(n)] # at first, every id is different, every value belongs to their own group
        self.__count = n
    
    #public
    def find(self, p):
        if p >= 0 and p < self.__count:
            return self.__id[p]
            
    def isConnected(self, p, q):
        return self.find(p) == self.find(q)

    def unionElements(self, p, q):
        if self.__id[p] != self.__id[q]:
            pID = self.__id[p]
            qID = self.__id[q]
            for i in range(len(self.__id)):
                if self.__id[i] == pID:
                    self.__id[i] == qID
