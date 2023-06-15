class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None

        cnt_a = cnt_b = 0
        curr_a = headA
        curr_b = headB

        while curr_a:
            cnt_a += 1
            curr_a = curr_a.next

        while curr_b:
            cnt_b += 1
            curr_b = curr_b.next

        curr_a = headA
        curr_b = headB
        if cnt_b < cnt_a:
            for _ in range(cnt_a - cnt_b):
                curr_a = curr_a.next
        else:
            for _ in range(cnt_b - cnt_a):
                curr_b = curr_b.next

        cnt = 0
        while curr_a != curr_b:
            cnt += 1
            curr_a = curr_a.next
            curr_b = curr_b.next

        return curr_a
