class HashTable(object):
    def __init__(self):
        self.size = 11
        self.slot = [None] * self.size
        self.data = [None] * self.size

    @staticmethod
    def hash_func(key, a_int):
        return 1

    @staticmethod
    def rehash_func(key, a_int):
        return 2

    def put(self, k, v):
        hash_val = self.hash_func(k, len(self.slot))

        if self.slot[hash_val] is None:
            self.slot[hash_val] = k
            self.data[hash_val] = v
        elif self.slot[hash_val] == k:
            self.data[hash_val] = v
        else:
            flg = 1
            while flg:
                rehash_val = self.rehash_func(k, len(self.slot))
                if self.slot[rehash_val] is None:
                    flg = 0
                    self.slot[rehash_val] = k
                    self.data[rehash_val] = v
                elif self.slot[rehash_val] == k:
                    flg = 0
                    self.data[rehash_val] = v
                else:
                    pass

    def get(self, k): pass

    def del_map(self, k): pass

    def len(self): pass

    def __contains__(self, item):
        pass

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, k):
        pass




if __name__ == '__main__':
