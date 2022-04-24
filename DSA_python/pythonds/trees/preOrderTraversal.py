def preOrderTraversal(root):
    if root is not None:
        print(root.key)
        preOrderTraversal(root.left)
        preOrderTraversal(root.right)
    else:  # 说明是个叶子节点的子节点
        pass
