class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head, val: int):
        head_fake = ListNode(0, head)
        last = head_fake

        while head:
            if head.val != val:
                last = head
            else:
                last.next = head.next
            head = head.next

        return head_fake.next


if __name__ == '__main__':
    data = [7,7,7,7]

    _ = None
    for i in range(len(data) - 1, -1, -1):
        _ = ListNode(data[i], _)
    head = _

    res = Solution().removeElements(head, 7)
    lst = []
    while res:
        lst.append(res.val)
        res = res.next
    print(lst)
