from random import randint

def __partition3(arr, l, r):
    randIndex = randint(l, r)
    arr[randIndex], arr[l] = arr[l], arr[randIndex]

    v = arr[l]
    lt = l      #arr[l+1, lt] < v
    gt = r + 1  #arr[gt, r] > v
    i = l + 1   #arr[lt+1, i] == v
    while i < gt: #alert
        if arr[i] < v:
            arr[i], arr[lt+1] = arr[lt+1], arr[i]
            lt += 1
            i += 1 #alert
        elif arr[i] > v:
            arr[i], arr[gt-1] = arr[gt-1], arr[i]
            gt -= 1
        else:
            i += 1
        
    arr[l], arr[lt] = arr[lt], arr[l]
    return [lt, gt]

def __quickSort3(arr, l, r):
    if l < r:
        p = __partition3(arr, l, r)
        __quickSort3(arr, l, p[0]-1)
        __quickSort3(arr, p[1], r)

def quickSort3(arr):
    if not arr:
        return None
    
    __quickSort3(arr, 0, len(arr)-1)
    return arr