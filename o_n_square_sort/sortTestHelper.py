import time
from random import randint 

def generateArray(n=100):
    # randint can generate random number from [start, end]
    return [randint(0, 100) for x in range(n)]

def measureSort(func, arr):
    start = time.time()
    # print(func(arr))
    func(arr)
    print('Execution time is {}s'.format(time.time()-start))
    return