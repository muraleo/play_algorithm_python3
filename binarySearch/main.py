from binarySearch import *
from sortTestHelper import *
from random import randint
from bst import *

a = sorted(generateArray(100))
a1 = a[:] # copy array a
a2 = a[:]

target = randint(0, 100)
testbst = BST()
testbst.insert(2, 3)


measureSort(binarySearchIter, a1, target)
measureSort(binarySearchRec, a2, target)