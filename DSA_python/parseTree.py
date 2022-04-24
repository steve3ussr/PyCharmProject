from pythonds.trees.BinaryTree import BinaryTree
from pythonds.basic.Stack import Stack
import operator
from pythonds.trees.preOrderTraversal import preOrderTraversal as preOrder
from pythonds.trees.postOrderTraversal import postOrderTraversal as postOrder
from pythonds.trees.midOrderTraversal import midOrderTraversal as midOrder


def buildParseTree(a_str):
    a_str = a_str.replace(' ', '')
    print(a_str)
    head = BinaryTree()
    current = head
    parentNodeStack = Stack()
    parentNodeStack.push(head)
    for i in a_str:
        if i == '(':
            current.insertLeft()
            parentNodeStack.push(current)
            current = current.getLeftBranch()
        elif i == ')':
            current = parentNodeStack.pop()
        elif i in '+-*/':
            current.setRootVal(i)
            current.insertRight()
            parentNodeStack.push(current)
            current = current.getRightBranch()
        else:  # nums
            current.setRootVal(eval(i))
            current = parentNodeStack.pop()
    if parentNodeStack.size() == 0:
        print('Stack is CLEAR')
    return head


def calculate(root):
    operator_dict = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }
    leftBranch = root.getLeftBranch()
    rightBranch = root.getRightBranch()

    if leftBranch is None and rightBranch is None:
        return root.getRootVal()
    elif leftBranch is None and rightBranch is not None:
        return calculate(rightBranch)
    elif rightBranch is None and leftBranch is not None:
        return calculate(leftBranch)
    else:
        return operator_dict[root.getRootVal()](calculate(leftBranch), calculate(rightBranch))


# (((2 + 5) + 3) * ((7 + 3) * (2 + (1 + 1))))
resTree = buildParseTree('((7+3)*(5-2))')
resAns = calculate(resTree)
print(resAns)
print('--------pre: ')
preOrder(resTree)
print('--------post: ')
postOrder(resTree)
print('--------mid: ')
midOrder(resTree)


