# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nextLargerNodes(self, head) -> list[int]:

        st = []
        ans = []

        while head:
            while st and head.val > st[-1][-1]:
                ans[st.pop()[0]] = head.val

            st.append([len(ans), head.val])
            ans.append(0)
            head = head.next

            print(f"stack = {st}, ans = {ans}")

        print(ans)
        return ans


if __name__ == '__main__':
    lst = [2, 1, 5, 3, 2, 6]
    _ = None
    for i in range(len(lst) - 1, -1, -1):
        _ = ListNode(lst[i], _)

    res = Solution().nextLargerNodes(_)
    print(res)
