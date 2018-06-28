class MaxHeap(object):
    # private
    def __shiftUp(self, n):
        # This heap index start from 0
        while n > 0 and self.__heap[n] > self.__heap[(n+1)//2-1]:
            self.__heap[n], self.__heap[(n+1)//2-1] = self.__heap[(n+1)//2-1], self.__heap[n]
            n = (n+1)//2-1

    def __shiftDown(self, i=0):
        while 2*i+1 < self.__count:
            j = 2 * i +1
            if j+1 < self.__count and self.__heap[j+1] > self.__heap[j] :
                j = j+1
            if self.__heap[i] > self.__heap[j]:
                break
            
            self.__heap[i], self.__heap[j] = self.__heap[j], self.__heap[i]
            i = j

    def __heapify(self):
        for i in range(self.__count//2+1, -1, -1):
            self.__shiftDown(i)

    # public
    # def __init__(self, max=1000):
    #     self.__heap = [] # heap list start from 0
    #     self.__capacity = max
    #     self.__count = 0

    def __init__(self, arr=[], max=1000):
        self.__heap = arr
        self.__capacity = max
        self.__count = len(arr)
        self.__heapify()

    def size(self):
        return self.__count

    def isEmpty(self):
        return self.__count == 0

    def insert(self, e):
        if self.__count+1 < max:
            self.__heap.append(e)
            self.__count += 1
            self.__shiftUp(self.__count-1)

    def extractMax(self):
        if self.__count == 1:
            result = self.__heap[0]
            self.__count -= 1
            self.__heap = []
            return result
        elif self.__count > 1:
            result = self.__heap[0]
            self.__heap[0] = self.__heap[self.__count-1]
            self.__count -= 1
            self.__heap = self.__heap[:-1]
            self.__shiftDown()
            return result
        return None

    def printHeap(self):
        print(self.__heap)