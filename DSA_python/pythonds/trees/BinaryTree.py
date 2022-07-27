"""
ver: nodes and references
"""


class BinaryTree(object):
    def __init__(self, val=None):
        self.key = val
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, val=None):
        if self.leftChild is None:
            self.leftChild = BinaryTree(val)
        else:
            temp_node = BinaryTree(val)
            temp_node.leftChild = self.leftChild
            self.leftChild = temp_node

    def insertRight(self, val=None):
        if self.rightChild is None:
            self.rightChild = BinaryTree(val)
        else:
            temp_node = BinaryTree(val)
            temp_node.rightChild = self.rightChild
            self.rightChild = temp_node

    def getLeftBranch(self):
        return self.leftChild

    def getRightBranch(self):
        return self.rightChild

    def setRootVal(self, new_val):
        self.key = new_val

    def getRootVal(self):
        return self.key


if __name__ == '__main__':
    r = BinaryTree(5)
