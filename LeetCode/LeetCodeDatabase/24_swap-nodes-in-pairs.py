class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head):
        if not head or not head.next:
            return head

        head_fake = ListNode(0, head)
        prev = head_fake
        curr = head

        while curr and curr.next:
            prev.next, curr.next.next, curr.next = curr.next, curr, curr.next.next
            prev, curr = curr, curr.next

        return head_fake.next
