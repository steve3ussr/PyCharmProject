class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        result = ListNode(0)
        r = result
        carry = 0
        while (l1 or l2):
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            local_sum = x + y + carry
            carry = local_sum // 10
            r.next = ListNode(local_sum % 10)
            r = r.next
            if l1 != None:
                l1 = l1.next

            if l2 != None:
                l2 = l2.next

        if carry > 0:
            r.next = ListNode(1)
        return result.next