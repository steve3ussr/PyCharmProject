class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        pretend = head
        last = None
        temp_head = head
        cnt = 1
        while cnt != n:
            cnt += 1
            temp_head = temp_head.next

        if temp_head.next is None:
            return head.next
        else:
            while temp_head.next is not None:
                last = pretend
                pretend = pretend.next
                temp_head = temp_head.next
            last.next = pretend.next

        return head
