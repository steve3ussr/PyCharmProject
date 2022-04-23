from pythonds.basic.BinaryTree import BinaryTree
r = BinaryTree('a')
print(r.getLeftBranch())
r.insertLeft('b')
print(r.getLeftBranch().getRootVal())
