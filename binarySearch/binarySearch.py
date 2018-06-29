def binarySearchIter(arr, target):
    if not arr:
        return None
    # search in [l,r]
    l = 0, r = len(arr)-1
    while(l <= r):
        int mid = l + (r-l)//2
        if(arr[mid] < target):
            l = mid + 1
        elif(arr[mid] > target):
            r = mid - 1
        else:
            return mid
    return None