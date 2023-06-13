class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head):
        # length=0      length=1
        if not head or not head.next:
            return head

        prev = ListNode(0, head)
        curr = head
        next = curr.next

        while curr:
            print(curr.val)
            curr.next = prev if curr != head else None
            prev = curr
            curr = next
            next = next.next if next else None

        return prev


if __name__ == '__main__':
    data = [1,2,3,4,5]
    _ = None
    for i in range(len(data)-1, -1, -1):
        _ = ListNode(data[i], _)
    head = _

    res = Solution().reverseList(head)
    _ = res
    while _:
        print(_.val)
        _ = _.next

