from .BinarySearchTree import BinarySearchTree
from .TreeNode import TreeNode


class AVL_BST(BinarySearchTree):
    def _put(self, key, value, currentRoot):
        if key < currentRoot.key:
            if currentRoot.hasLeftChild():
                self._put(key, value, currentRoot.leftChild)
            else:
                currentRoot.leftChild = TreeNode(key, value, parent=currentRoot)
                self.updateBalance(currentRoot.leftChild)

        elif key > currentRoot.key:
            if currentRoot.hasRightChild():
                self._put(key, value, currentRoot.rightChild)
            else:
                currentRoot.rightChild = TreeNode(key, value, parent=currentRoot)
                self.updateBalance(currentRoot.rightChild)
        else:
            currentRoot.replaceNodeData(key, value, currentRoot.leftChild, currentRoot.leftChild)

    def updateBalance(self, node):
        # node here is the new node just inserted
        if node.balanceFactor > 1 or node.balanceFactor < -1:
            self.rebalance(node)
            return

        if node.parent:
            if node.isLeftChild():
                node.parent.balanceFactor += 1
            elif node.isRightChild():
                node.parent.balanceFactor -= 1
            else:  # root node
                pass

        if node.parent.balanceFactor != 0:
            self.updateBalance(node.parent)

    def rebalance(self, node):
        # TODO: unkonwn
        pass

    def rotateLeft(self, node):
        pass

    def rotateRight(self, node):
        pass



