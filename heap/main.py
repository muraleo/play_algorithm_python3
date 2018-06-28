from heap import MaxHeap
from sortTestHelper import *
from heapSort import *

a = generateArray(1000)
a1 = a[:]
a2 = a[:]
measureSort(heapSort1, a1)
measureSort(heapSort2, a2)
