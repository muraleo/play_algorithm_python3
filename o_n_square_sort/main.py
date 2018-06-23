from onsquare_sort import *
from sortTestHelper import *

n = 100 # length of gererated array
arr = generateArray(n)

# copy generated array for different test
a1 = arr[:]

# test section
measureSort(selectionSort, a1)