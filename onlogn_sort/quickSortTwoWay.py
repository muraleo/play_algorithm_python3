from random import randint

def __partition2(arr, l, r):
    randIndex = randint(l, r)
    arr[randIndex], arr[l] = arr[l], arr[randIndex]

    # arr[l+1, i) <= flag, arr(j,r] >= v
    flag, i, j = arr[l], l+1, r
    while True:
        while i <= r and arr[i] < flag:
            i += 1
        while j >= l+1 and arr[j] > flag:
            j -= 1
        if i > j:
            break
        else:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    arr[l], arr[j] = arr[j], arr[l]
    return j

def __quickSort2(arr, l, r):
    if l<r:
        p = __partition2(arr, l, r)
        __quickSort2(arr, l, p-1)
        __quickSort2(arr, p+1, r)

def quickSort2(arr):
    if not arr:
        return None

    __quickSort2(arr, 0, len(arr)-1)
    return arr