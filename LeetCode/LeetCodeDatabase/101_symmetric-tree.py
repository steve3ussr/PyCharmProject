# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def isSymmetric(self, root) -> bool:
        lst = deque([root])
        level = deque()
        while lst:
            for i in range(len(lst)):
                node = lst.popleft()
                if node.left:
                    lst.append(node.left)
                    level.append(node.left.val)
                else:
                    level.append(None)
                if node.right:
                    lst.append(node.right)
                    level.append(node.right.val)
                else:
                    level.append(None)

            while level:
                if level.popleft() != level.pop():
                    return False
        return True