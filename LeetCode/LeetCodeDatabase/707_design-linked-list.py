class ListNode:
    def __init__(self, prev, val, next):
        self.prev = prev
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self._len = 0

    def __len__(self):
        return self._len

    def __str__(self):
        if self._len == 0:
            return f"{self._len}, {[]}"

        curr = self.head
        res = []
        while curr:
            res.append(curr.val)
            curr = curr.next
        return f"{self._len}, {res}"

    __repr__ = __str__

    def __getitem__(self, index):
        if not self._len:  # empty
            return None
        elif self._len == 1:
            return self.head

        if index <= self._len // 2:
            curr = self.head
            cnt = 0
            while cnt < index:
                curr = curr.next
                cnt += 1
            return curr
        else:
            cnt = self._len-1
            curr = self.tail

            while cnt > index:
                curr = curr.prev
                cnt -= 1
            return curr

    def get(self, index: int) -> int:
        return self[index].val if 0<=index<self._len else -1

    def addAtHead(self, val: int) -> None:
        if self.head is None:
            self.head = self.tail = ListNode(None, val, None)
        else:
            self.head.prev = ListNode(None, val, self.head)
            self.head = self.head.prev

        self._len += 1

    def addAtTail(self, val: int) -> None:
        if self.head is None:
            self.head = self.tail = ListNode(None, val, None)
        else:
            self.tail.next = ListNode(self.tail, val, None)
            self.tail = self.tail.next
        self._len += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if self._len == 0:
            if index == 0:
                self.addAtHead(val)
            return

        if index < 0 or index > self._len:
            return

        if index == self._len:
            self.addAtTail(val)
            return

        if index == 0:
            self.addAtHead(val)
            return

        target = self[index]
        target.prev.next = ListNode(target.prev, val, target)
        target.prev = target.prev.next
        self._len += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self._len:
            return
        elif index < 0:
            return
        elif self._len == 0:
            return

        if index == 0:
            if self._len == 1:
                self.tail = self.head = None
            else:
                self.head = self.head.next
                self.head.prev = None
            self._len -= 1
            return

        if index == self._len-1:
            self.tail = self.tail.prev
            self.tail.next = None
            self._len -= 1
            return

        target = self[index]
        target.prev.next = target.next
        target.next.prev = target.prev
        self._len -= 1

    def extend(self, seq):
        if len(seq) < 1:
            return

        for _ in seq:
            self.addAtTail(_)


if __name__ == '__main__':
    inst = MyLinkedList()
    inst.addAtHead(7); print(inst)
    inst.addAtTail(7); print(inst)
    inst.addAtHead(9); print(inst)
    inst.addAtTail(8); print(inst)
    inst.addAtHead(6); print(inst)
    inst.addAtHead(0); print(inst)

    print(inst[5].val)
    inst.addAtHead(0); print(inst)
    print(inst[2].val)
    print(inst[5].val)
