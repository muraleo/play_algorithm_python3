from heap import *

def heapSort1(arr):
    if not arr:
        return None
    
    maxHeap = MaxHeap()
    for i in arr:
        maxHeap.insert(i)

    for i in range(len(arr)-1, -1, -1):
        arr[i] = maxHeap.extractMax()

    return arr