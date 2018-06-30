import time
from random import randint 

def generateArray(n=100):
    # randint can generate random number from [start, end]
    return [randint(0, 100) for x in range(n)]

def measureSort(func, arr, target):
    start = time.time()
    print("array is {}, target is {}, result is {}".format(arr, target, func(arr, target)))
    print('Execution time is {}s'.format(time.time()-start))
    # print(curArr)
    return