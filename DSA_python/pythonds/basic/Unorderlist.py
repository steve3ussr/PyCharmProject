class Node(object):
    def __init__(self):
        self._data = None
        self._next = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, new_data):
        self._data = new_data

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, new_next):
        self._next = new_next


class Unorderlist(object):
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def add(self, new_data):
        temp_node = Node()
        temp_node.data = new_data
        temp_node.next = self.head
        self.head = temp_node

    def length(self):
        cnt = 0
        temp = self.head
        while temp is not None:
            cnt += 1
            temp = temp.next
        return cnt

    def search(self, i):
        temp = self.head

        while temp is not None:
            if i == temp.data:
                return True
            temp = temp.next
        return False

    def remove(self, i):
        current = self.head
        last = None

        while current is not None:

            # 只要找到一样的就可以break
            if i == current.data:
                if last is None:
                    self.head = current.next
                else:
                    last.next = current.next
                break

            else:
                last = current
                current = current.next

    def append(self, new_data):
        current = self.head
        while current.next is not None:
            print(current.data)
            current = current.next
        temp_node = Node()
        temp_node.data = new_data
        current.next = temp_node

    def insert(self, new_data, i): pass

    def index(self, a_data): pass

    def pop(self): pass

    def __str__(self):
        temp = self.head
        data_list = []
        while temp is not None:
            data_list.append(temp.data)
            temp = temp.next
        return f"{data_list}"

    def __repr__(self):
        print(self.__str__())
