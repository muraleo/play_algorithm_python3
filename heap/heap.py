class MaxHeap(object):
    # private
    def __shiftUp(self, n):
        while n > 0 and self.__heap[n] > self.__heap[(n+1)//2-1]:
            self.__heap[n], self.__heap[(n+1)//2-1] = self.__heap[(n+1)//2-1], self.__heap[n]
            n = (n+1)//2-1

    # public
    def __init__(self, max=1000):
        self.__heap = [] # heap list start from 0
        self.__capacity = max
        self.__count = 0

    def size(self):
        return self.__count

    def isEmpty(self):
        return self.__count == 0

    def insert(self, e):
        if self.__count+1 < max:
            self.__heap.append(e)
            self.__count += 1
            self.__shiftUp(self.__count-1)

    def printHeap(self):
        print(self.__heap)