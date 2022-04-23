"""
ver: nodes and references
"""


class BinaryTree(object):
    def __init__(self, val):
        self.key = val
        self.left = None
        self.right = None

    def insertLeft(self, val):
        if self.left is None:
            self.left = BinaryTree(val)
        else:
            temp_node = BinaryTree(val)
            temp_node.left = self.left
            self.left = temp_node

    def insertRight(self, val):
        if self.right is None:
            self.right = BinaryTree(val)
        else:
            temp_node = BinaryTree(val)
            temp_node.right = self.right
            self.right = temp_node

    def getLeftBranch(self):
        return self.left

    def getRightBranch(self):
        return self.right

    def setRootVal(self, new_val):
        self.key = new_val

    def getRootVal(self):
        return self.key

    


if __name__ == '__main__':
    r = BinaryTree(5)
