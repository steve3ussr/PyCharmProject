# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        if not list1:  # list1 is empty
            return list2
        elif not list2:  # list2 is empty
            return list1
        else:
            pass

        head = ListNode(0)
        return_head = head

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                head.next = list1
                list1 = list1.next
                head = head.next
            else:
                head.next = list2
                list2 = list2.next
                head = head.next

        head.next = list1 if list2 is None else list2

        return return_head

