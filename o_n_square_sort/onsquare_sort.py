def selectionSort(arr):
    if not arr:
        return []

    #from [0, len(a))
    for i in range(len(arr)):
        minIndex = i
        # find the minimal index from [i, len(arr))
        for j in range(i, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr

def insertionSort(arr):
    if not arr:
        return []

    # from [1, len(arr))
    for i in range(1, len(arr)):
        # find the postion arr[j] should be inserted from [i, 0)
        for j in range(i,0, -1):
            if arr[j]<arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                # can stop this loop early
                break
    return arr

# very efficient when the array is nearly ordered
# best time complexity is O(n)
def insertionSortOptime(arr):
    if not arr:
        return []

    # loop through the whole array from [1, len(arr))
    for i in range(1, len(arr)):

        cur, j = arr[i], i
        # find the proper position in arr[1, i]
        for j in range(i, 0, -1):
            if arr[j-1] > cur:
                arr[j] = arr[j-1]
            else:
                arr[j] = cur
                break
    return arr

def bubbleSort(arr):
    if not arr:
        return []
    
    # from [len(arr)-1, 1]
    for i in range(len(arr)-1, 0, -1):
        # from [0, i-1] because arr[j+1] must exist
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# The reason why this bubble sort has better performance 
# is that when swapCheck is False after a inner loop,
# it means this array is already sorted, so we can avoid
# extra loop
def bubbleSortOptime(arr):
    if not arr:
        return[]

    # inner loop range from [len(arr)-1, 1]
    for i in range(len(arr)-1, 0, -1):
        swapCheck = False

        # loop from [0, i-1] to garantee that arr[j+1] exist
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapCheck = True
        if swapCheck == False:
            break
    return arr