# merge arr[l,m] and arr[m+1, r]
def __merge(arr, l, mid, r):
    # auxiliary array to store arr[l, mid]
    auxl = arr[l:mid+1]
    # auxiliary array to store arr[mid+1, r]
    auxr = arr[mid+1:r+1]

    i, j = 0, 0
    for k in range(l, r+1):
        if i >= len(auxl):
            arr[k] = auxr[j]
            j += 1
        elif j >= len(auxr):
            arr[k] = auxl[i]
            i += 1
        elif auxl[i] < auxr[j]:
            arr[k] = auxl[i]
            i+=1
        else:
            arr[k] = auxr[j]
            j+=1

def __mergeSort(arr, l, r):
    if l < r:
        # 2nd optimization when array is short, insertion sort is faster
        if r - l <= 15:
            insertionSortM(arr, l, r)
        else:
            mid = (l+r)//2
            __mergeSort(arr, l, mid)
            __mergeSort(arr, mid+1, r)

            # 1st optimization when array is nearly ordered
            if arr[mid] > arr[mid+1]:
                __merge(arr, l, mid, r)

# insertion sort arr[l:r+1]
def insertionSortM(arr, l, r):
    if not arr:
        return None
    # loop arr from [l+1, r]
    for i in range(l+1, r+1):
        cur = arr[i]
        # loop arr from [i, 1] to make sure arr[j-1] is legal
        for j in range(i,l,-1):
            if arr[j-1] > cur:
                arr[j] = arr[j-1]
            else:
                arr[j] = cur
                break

def mergeSort(arr):
    if not arr:
        return None
    
    #from [0, len(arr)-1]
    __mergeSort(arr, 0, len(arr)-1)
    return arr

def mergeSortBU(arr):
    if not arr:
        return None

    # block size increase from 1 to len(arr)
    sz = 1
    while sz <= len(arr):
        i = 0
        while i + sz < len(arr):
            # if arr[i+sz] < arr[i+sz-1]:
            #     if sz < 15:
            #         insertionSortM(arr, i, i+sz+sz-1)
            #     else:
             __merge(arr, i, i+sz-1, min(i+sz+sz-1, len(arr)-1))
             i = i + sz + sz
        sz += sz
    return arr