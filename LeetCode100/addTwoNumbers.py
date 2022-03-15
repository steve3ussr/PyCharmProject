# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        ans = head
        flag = 0
        status_end = 0

        def checkNone(inst1, inst2):
            if inst1.next is None and inst2.next is None:
                nonlocal status_end
                status_end = 1
            elif inst1.next is None:
                inst1.next = ListNode(0)
            elif inst2.next is None:
                inst2.next = ListNode(0)
            else:
                pass
            return inst1.val + inst2.val

        while True:
            temp_val = flag + checkNone(l1, l2)
            if temp_val >= 10:
                ans.val = temp_val - 10
                flag = 1
            else:
                ans.val = temp_val
                flag = 0
            # ans.next = ListNode(0)

            if status_end == 1:
                if flag is 1: ans.next = ListNode(1)
                else: ans.next = None
                break
            else:
                ans.next = ListNode(0)
                l1 = l1.next
                l2 = l2.next
                ans = ans.next

        return head
