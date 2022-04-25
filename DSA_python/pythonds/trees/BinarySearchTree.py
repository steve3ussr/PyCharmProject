from TreeNode import TreeNode


class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    # *set* methods sets:

    def put(self, key, value):
        if self.root:
            self._put(key, value, self.root)
        else:
            self.root = TreeNode(key, value)

    def _put(self, key, value, currentRoot):
        if key < currentRoot.key:
            if currentRoot.hasLeftChild():
                self._put(key, value, currentRoot.leftChild)
            else:
                currentRoot.leftChild = TreeNode(key, value, parent=currentRoot)
        elif key > currentRoot.key:
            if currentRoot.hasRightChild():
                self._put(key, value, currentRoot.rightChild)
            else:
                currentRoot.rightChild = TreeNode(key, value, parent=currentRoot)
        else:
            currentRoot.replaceNodeData(key, value, currentRoot.leftChild, currentRoot.leftChild)

    def __setitem__(self, k, v):
        self.put(k, v)

    # *get* methods sets:

    def get(self, k):
        if self.root:
            res = self._get(k, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self, key, currentRoot):
        """和书里的不一样，希望能运行 """
        if key < currentRoot.key:
            if currentRoot.hasLeftChild():
                self._get(key, currentRoot.leftChild)
            else:
                return None
        elif key > currentRoot.key:
            if currentRoot.hasRightChild():
                self._get(key, currentRoot.rightChild)
            else:
                return None
        elif key == currentRoot.key:
            return currentRoot
        else:
            return None

    def __getitem__(self, k):
        return self.get(k)

    def __contains__(self, k):
        if self._get(k, self.root):
            return True
        else:
            return False

    # *del* methods sets:

    def delete(self, key):
        if nodeToRemove := self._get(key, self.root):
            if nodeToRemove == self.root:
                self.root = None
            else:
                self.remove(nodeToRemove)
            self.size -= 1
        else:
            raise KeyError('Error, key not in tree')

    def __delitem__(self, key):
        self.delete(key)

    def remove(self, currentNode):
        if currentNode.childrenNums() == 0:
            pass
        elif currentNode.childrenNums() == 0:
            pass
        else:
            pass

