from mergeSort import *
from quickSort import *
from quickSortTwoWay import *
from quickSortThreeWay import *
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
measureSort(mergeSort, a1) 
measureSort(mergeSortBU, a2)
measureSort(quickSort, a3)
measureSort(quickSort2, a4)
measureSort(quickSort3, a5)