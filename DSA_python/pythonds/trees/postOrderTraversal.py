def postOrderTraversal(root):
    if root is not None:
        postOrderTraversal(root.right)
        postOrderTraversal(root.left)
        print(root.key)
