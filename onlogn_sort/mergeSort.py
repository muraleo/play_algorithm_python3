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
        mid = (l+r)//2
        __mergeSort(arr, l, mid)
        __mergeSort(arr, mid+1, r)
        __merge(arr, l, mid, r)


def mergeSort(arr):
    if not arr:
        return None
    
    #from [0, len(arr)-1]
    __mergeSort(arr, 0, len(arr)-1)
    return arr