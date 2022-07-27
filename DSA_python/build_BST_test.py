from pythonds.trees.BinarySearchTree import BinarySearchTree as BST
from pythonds.trees.MaxBinaryHeap import MaxBinaryHeap as maxHeap


heap = maxHeap()
heap.buildHeap(list(range(1, 11)))
print(heap)
