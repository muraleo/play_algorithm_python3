import time
from random import randint 

def generateArray(n=100):
    # randint can generate random number from [start, end]
    return [randint(0, 1000000) for x in range(n)]

def measureSort(func, arr):
    start = time.time()
    # print(func(arr))
    curArr = func(arr)
    print('Execution time is {}s'.format(time.time()-start))
    # print(curArr)
    print(checkSorted(curArr))
    return

def checkSorted(arr):
    if not arr:
        return None
    if len(arr) == 1:
        return True

    for i in range(len(arr)-1):
        if arr[i+1]<arr[i]:
            print("ERROR: arr[{}] is {}, arr[{}] is {}.".format(i, arr[i], i+1, arr[i+1]))
            return False
    
    return True