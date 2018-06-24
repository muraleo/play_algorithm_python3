from onsquare_sort import *
from sortTestHelper import *

n = 1000 # length of gererated array
arr = generateArray(n)

# copy generated array for different test
a1 = arr[:]
a2 = arr[:]
a3 = arr[:]
a4 = arr[:]
a5 = arr[:]

# test section
measureSort(selectionSort, a1)
measureSort(insertionSort, a2)
measureSort(insertionSortOptime, a3)
measureSort(bubbleSort, a4)
measureSort(bubbleSortOptime, a5)