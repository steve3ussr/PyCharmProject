class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head):
        return self.v1(head)

    def v1(self, head):
        s = set()
        curr = head
        while curr and not curr in s:
            s.add(curr)
            curr = curr.next

        return curr

    def v2(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                idx_1 = head
                idx_2 = slow

                while idx_1 != idx_2:
                    idx_1 = idx_1.next
                    idx_2 = idx_2.next
                return idx_1

        return None