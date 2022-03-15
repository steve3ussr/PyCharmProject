# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        flag = 0
        while True:
            if l1.next is None and l2.next is None:
                return l3
            elif l1.next is None:
                l3.val = flag + l2.next
                if l3.val >= 10:
                    flag = 1
                    l3.val -= l3.val
            elif l2.next is None
                l3.val = flag + l1.next
                if l3.val >= 10:
                    flag = 1
                    l3.val -= l3.val
            else: