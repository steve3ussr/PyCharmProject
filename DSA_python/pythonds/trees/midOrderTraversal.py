def midOrderTraversal(root):
    if root is not None:
        midOrderTraversal(root.leftChild)
        print(root.key)
        midOrderTraversal(root.rightChild)

