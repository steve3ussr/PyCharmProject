class ListNode:
    def __init__(self, prev, val, next):
        self.prev = prev
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.head = ListNode(None, 0, None)
        self.tail = ListNode(None, 0, None)
        self.len = 0
        self.head.next = self.tail
        self.tail.prev = self.head

    def _get_node(self, index:int) -> ListNode|None:
        if not self.len or 0 > index or index >= self.len:
            return None

        if index <= self.len//2:
            cnt = 0
            curr = self.head.next
            while cnt != index:
                curr = curr.next
                cnt += 1
        else:
            cnt = self.len-1
            curr = self.tail.prev
            while cnt != index:
                curr = curr.prev
                cnt -= 1
        return curr

    def get(self, index: int) -> int:
        res = self._get_node(index)
        return res.val if res else -1


    def addAtHead(self, val: int) -> None:
        _ = ListNode(self.head, val, self.head.next)
        _.prev.next = _
        _.next.prev = _
        self.len += 1


    def addAtTail(self, val: int) -> None:
        _ = ListNode(self.tail.prev, val, self.tail)
        _.prev.next = _
        _.next.prev = _
        self.len += 1


    def addAtIndex(self, index: int, val: int) -> None:
        if index == self.len:
            return self.addAtTail(val)

        target = self._get_node(index)
        print(target.val if target else 'None')
        if not target:
            return

        _ = ListNode(target.prev, val, target)
        _.prev.next = _
        _.next.prev = _
        self.len += 1


    def deleteAtIndex(self, index: int) -> None:
        target = self._get_node(index)
        if not target:
            return

        target.prev.next = target.next
        target.next.prev = target.prev
        self.len -= 1

    def __str__(self):
        res = []
        if not self.len:
            return res
        curr = self.head.next
        while curr:
            res.append(curr.val)
            curr = curr.next
        res.pop()
        return f"{self.len}, {res}"

    __repr__ = __str__

    def __len__(self):
        return self.len

    def __getitem__(self, i):
        return self.get(i)

    def __delitem__(self, key):
        return self.deleteAtIndex(key)

    def __setitem__(self, key, val):
        target = self._get_node(key)
        if target:
            target.val = val


if __name__ == '__main__':
    inst = MyLinkedList()
    inst.addAtHead(1); print(inst)
    inst.addAtTail(3);
    print(inst)
    inst.addAtIndex(1, 2);
    print(inst)
    # inst.addAtTail(1); print(inst)


