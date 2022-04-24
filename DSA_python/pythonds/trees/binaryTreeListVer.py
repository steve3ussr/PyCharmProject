def BinaryTree(val):
    return [val, [], []]


def insertLeft(root, val):
    temp = root.pop(1)
    if not temp:
        root.insert(1, BinaryTree(val))
    else:
        root.insert(1, [val, temp, []])


def insertRight(root, val):
    temp = root.pop(2)
    if not temp:
        root.insert(2, BinaryTree(val))
    else:
        root.insert(2, [val, [], temp])


def getRootVal(root):
    return root[0]


def setRootVal(root, val):
    root[0] = val


def getLeftChild(root):
    return root[1]


def getRightChild(root):
    return root[2]


if __name__ == '__main__':
    r = BinaryTree(3)
    insertLeft(r, 4)
    insertLeft(r, 5)
    insertRight(r, 6)
    insertRight(r, 7)
    print(r)
    print(l := getLeftChild(r))
    setRootVal(l, 9)

    insertLeft(l, 11)
    print(r)
    print(getRightChild(getRightChild(r)))
