def preOrderTraversal(root):
    if root is not None:
        print(root.key)
        preOrderTraversal(root.leftChild)
        preOrderTraversal(root.rightChild)
    else:  # 说明是个叶子节点的子节点
        pass
