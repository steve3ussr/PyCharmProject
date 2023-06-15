# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        head_fake = ListNode(0, head)
        lo, hi = head_fake, head_fake

        for _ in range(n):
            hi = hi.next

        while hi.next:
            hi = hi.next
            lo = lo.next

        lo.next = lo.next.next

        return head_fake.next
