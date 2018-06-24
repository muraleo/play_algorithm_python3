def __partition(arr, l, r):
    v,i = arr[l],l
    # arr[l+1,i-1] < v, arr[i, j-1] > v
    for j in range(l+1, r+1):
        if arr[j] <= v:
            arr[i+1], arr[j] = arr[j], arr[i+1]
            i += 1
    arr[l], arr[i] = arr[i], arr[l]
    return i


# quick sort arr from [l, r]
def __quickSort(arr, l, r):
    if l < r:
        # return index p so that arr[0:p-1] < arr[p] and arr[p+1:] > arr[p]
        p = __partition(arr, l, r)
        __quickSort(arr, l, p-1)
        __quickSort(arr, p+1, r)
    else:
        return None

def quickSort(arr):
    if not arr:
        return None

    __quickSort(arr, 0, len(arr)-1)
    return arr