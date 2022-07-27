from .TreeNode import TreeNode


class BinarySearchTree(object):

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()  # 相当于iter(self.root)

    # *set* methods group:

    def put(self, key, value):
        if self.root:
            self._put(key, value, self.root)
        else:
            self.root = TreeNode(key, value)
        self.size += 1

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

    # *get* methods group:

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
        if currentRoot:
            print('trigger _get')  # I don't expect this seg to be triggered
        else:
            return None

        if key < currentRoot.key and currentRoot.hasLeftChild():
            return self._get(key, currentRoot.leftChild)

        elif key > currentRoot.key and currentRoot.hasRightChild():
            return self._get(key, currentRoot.rightChild)
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

    # *del* methods set:

    def delete(self, key):
        if nodeToRemove := self._get(key, self.root):
            if nodeToRemove == self.root and self.size == 1:
                self.root = None
            else:
                self.remove(nodeToRemove)
            self.size -= 1
        else:
            raise KeyError('Error, key not in tree')

    def __delitem__(self, key):
        self.delete(key)

    def remove(self, currentNode):
        if currentNode.childrenNums() == 0:  # 到这里说明一定是leaf
            if currentNode.parent.leftChild == currentNode:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None

        elif currentNode.childrenNums() == 1:
            currentNodeChild = currentNode.hasLeftChild() or currentNode.hasRightChild()
            if currentNode.parent:  # 不是根节点
                currentNodeChild.parent = currentNode.parent
                if currentNode == currentNode.parent.leftChild:
                    currentNode.parent.leftChild = currentNodeChild
                else:
                    currentNode.parent.rightChild = currentNodeChild
            else:  # 是根节点
                self.root = currentNodeChild

        else:
            succ = currentNode.findSuccessor()
            succ.spliceOut()  # succ extract
            currentNode.key = succ.key  # replace k-v, don't change children and parent
            currentNode.payload = succ.payload

    def __str__(self):
        alist = []

        def mid_trv(node):
            nonlocal alist
            if node is not None:
                mid_trv(node.leftChild)
                alist.append(node.key)
                mid_trv(node.rightChild)

        if self.root:
            mid_trv(self.root)
        else:
            pass

        return f'{alist}'


if __name__ == '__init__':
    a = TreeNode(1, 'a')
