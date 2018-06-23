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