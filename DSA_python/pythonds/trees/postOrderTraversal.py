def postOrderTraversal(root):
    if root is not None:
        postOrderTraversal(root.rightChild)
        postOrderTraversal(root.leftChild)
        print(root.key)
