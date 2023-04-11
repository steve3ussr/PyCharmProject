class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        ans = head
        flag = 0

        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            sum_ = flag + x + y
            ans.next = ListNode(sum_ % 10)
            flag = sum_ // 10
            ans = ans.next

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        if flag > 0:
            ans.next = ListNode(1)
        return head.next
