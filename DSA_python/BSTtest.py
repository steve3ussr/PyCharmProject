from pythonds.trees.BinarySearchTree import BinarySearchTree
from pythonds.trees.TreeNode import TreeNode


BST = BinarySearchTree()
BST.put(1, 'a')
BST.put(0, 'a')
BST.put(2, 'a')
for i in BST:
    print(i)

