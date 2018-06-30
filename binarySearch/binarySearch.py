def binarySearchIter(arr, target):
    if not arr:
        return None
    # search in [l,r]
    l, r = 0, len(arr)-1
    while(l <= r):
        mid = l + (r-l)//2
        if(arr[mid] < target):
            l = mid + 1
        elif(arr[mid] > target):
            r = mid - 1
        else:
            return mid
    return None

def  __binarySearchRec(arr, l, r, target):
    if not arr:
        return None
    mid = l + (r - l)//2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return __binarySearchRec(arr, mid+1, r, target)
    else:
        return __binarySearchRec(arr, l, mid-1, target)

def binarySearchRec(arr, target):
    if not arr:
        return None
    return __binarySearchRec(arr, 0, len(arr)-1, target)