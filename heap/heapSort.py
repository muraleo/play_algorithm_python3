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

def heapSort2(arr):
    if not arr:
        return None

    maxHeap = MaxHeap(arr)

    for i in range(len(arr)-1, -1, -1):
        arr[i] = maxHeap.extractMax()
    return arr

def __shiftDown(arr, n, i):
    while(2*i+1 < n):
        k = 2*i+1
        if k+1 < n and arr[k+1] > arr[k]:
            k += 1
        if arr[i] >= arr[k]:
            break
        arr[i], arr[k] = arr[k], arr[i]
        i = k

def heapSortInPlace(arr):
    if not arr:
        return None

    #heapify first
    for i in range((len(arr)-1)//2, -1, -1):
        __shiftDown(arr, len(arr), i)

    #extract max then move it to array's end
    for i in range(len(arr)-1, -1, -1):
        arr[i], arr[0] = arr[0], arr[i]
        __shiftDown(arr, i, 0)

    return arr