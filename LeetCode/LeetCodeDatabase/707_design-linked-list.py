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

    def __getitem__(self, i):
        return self.get[i]

    def __str__(self):
        res = []
        if self._len:
            curr = self.head
            while curr:
                res.append(curr.val)
        return str(res)

    __repr__ = __str__

    def _get_node(self, index: int) -> ListNode | None:
        if self._len == 0:
            return None

        if index >= self._len or index < 0:
            return None

        if index <= self._len // 2:
            cnt = 0
            curr = self.head
            while cnt < index:
                curr = curr.next
                cnt += 1
            return curr
        else:
            cnt = self._len - 1
            curr = self.tail
            while cnt > index:
                curr = curr.prev
                cnt -= 1
            return curr

    def get(self, index: int) -> int:
        if _ := self._get_node(index):
            return _.val
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        if not self._len:
            self.head = self.tail = ListNode(None, val, None)
        else:
            self.head.prev = ListNode(None, val, self.head)
            self.head = self.head.prev

        self._len += 1

    def addAtTail(self, val: int) -> None:
        if not self._len:
            self.head = self.tail = ListNode(None, val, None)
        else:
            self.tail.next = ListNode(self.tail, val, None)
            self.tail = self.tail.next

        self._len += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index == self._len:
            return self.addAtTail(val)

        if index == 0:
            return self.addAtHead(val)

        if target := self._get_node(index):
            target.prev.next = ListNode(target.prev, val, target)
            target.prev = target.prev.next
            self._len += 1

    def deleteAtIndex(self, index: int) -> None:
        if target := self._get_node(index):

            if index == 0:
                if self.head.next:
                    self.head = self.head.next
                    self.head.prev = None
                else:
                    self.head = self.tail = None
            elif index == self._len - 1:
                self.tail = self.tail.prev
                self.tail.next = None
            else:
                target.prev.next = target.next
                target.next.prev = target.prev

            self._len -= 1


if __name__ == '__main__':
    inst = MyLinkedList()
    inst.addAtIndex(2, 1); print(inst)
    inst.addAtIndex(3, 4);
    print(inst)
    inst.addAtTail(1); print(inst)


