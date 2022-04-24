def midOrderTraversal(root):
    if root is not None:
        midOrderTraversal(root.left)
        print(root.key)
        midOrderTraversal(root.right)

