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
        if node.balanceFactor < 0:  # 右倾，需要左旋
            if node.rightChild.balanceFactor > 0:
                self.rotateRight(node.rightChild)
            else:
                pass
            self.rotateLeft(node)
        elif node.balanceFactor > 0:
            if node.leftChild.balanceFactor < 0:
                self.rotateLeft(node.leftChild)
            else:
                pass
            self.rotateRight(node)
        else:
            pass

    def rotateLeft(self, rotRoot: TreeNode):
        # 1. root.parent connection
        newRoot = rotRoot.rightChild
        newRoot.parent = rotRoot.parent
        if rotRoot.parent:
            if rotRoot.isLeftChild():
                rotRoot.parent.leftChild = newRoot
            else:
                rotRoot.parent.rightChild = newRoot
        else:
            self.root = newRoot
        # 2. rotRoot.rightChild rebuild
        rotRoot.rightChild = newRoot.leftChild
        if newRoot.leftChild:
            newRoot.leftChild.parent = rotRoot
        # 3. rotRoot.parent rebuild
        newRoot.leftChild = rotRoot
        rotRoot.parent = newRoot
        # 4. parent nodes balanceFactor recalculate
        rotRoot.balanceFactor += 1 - min(newRoot.balanceFactor, 0)
        newRoot.balanceFactor += 1 + max(rotRoot.balanceFactor, 0)

    def rotateRight(self, rotRoot: TreeNode):
        newRoot = rotRoot.leftChild
        newRoot.parent = rotRoot.parent
        if rotRoot.parent:
            if rotRoot.isLeftChild():
                newRoot.parent.leftChild = newRoot
            else:
                newRoot.parent.rightChild = newRoot
        else:
            self.root = newRoot

        rotRoot.leftChild = newRoot.rightChild
        if rotRoot.leftChild:
            rotRoot.leftChild.parent = rotRoot

        newRoot.rightChild = rotRoot
        rotRoot.parent = newRoot

        rotRoot.balanceFactor += -1 - max(0, newRoot.balanceFactor)
        newRoot.balanceFactor += -1 + min(0, rotRoot.balanceFactor)


