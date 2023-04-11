# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nextLargerNodes(self, head) -> list[int]:
        res = []
        stack = []
        index = []
        cnt = 0

        while head:
            res.append(0)
            if len(stack) == 0:
                stack.append(head.val)
                index.append(cnt)
            elif stack[-1] >= head.val:
                stack.append(head.val)
                index.append(cnt)
            else:  # stack[-1] < head.val

                while stack and stack[-1] < head.val:
                    res[index[-1]] = head.val
                    stack.pop()
                    index.pop()

                stack.append(head.val)
                index.append(cnt)

            cnt += 1
            head = head.next

        return res


"""
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        res = []
        stack = []
        index = []
        cnt = 0
        while head:
            # pre
            res.append(0)

            # mid main
            if stack and stack[-1] >= head.val:
                stack.append(head.val)
                index.append(cnt)
            else:
                while stack and stack[-1] < head.val:
                    stack.pop()
                    res[index.pop()] = head.val

                stack.append(head.val)
                index.append(cnt)

            # post
            cnt += 1
            head = head.next

        return res
"""

if __name__ == '__main__':
    lst = [2, 1, 5, 3, 2, 6]
    _ = None
    for i in range(len(lst) - 1, -1, -1):
        _ = ListNode(lst[i], _)

    res = Solution().nextLargerNodes(_)
    print(res)
