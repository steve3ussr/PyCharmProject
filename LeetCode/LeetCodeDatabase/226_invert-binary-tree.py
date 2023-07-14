# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        lst = deque([root])

        while lst:
            for i in range(len(lst)):
                node = lst.popleft()


                node.left, node.right = node.right, node.left
                if node.left:
                    lst.append(node.left)
                if node.right:
                    lst.append(node.right)

        return root