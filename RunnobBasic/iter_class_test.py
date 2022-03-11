class IterMain(object):

    def __iter__(self):
        print('return an iterator')
        # global instA
        return K


class Iterator(object):
    def __init__(self, i):
        self.num = i

    def __next__(self):
        self.num = self.num + 1
        if self.num <= 10:
            return self.num
        else:
            raise StopIteration()


K = Iterator(0)
for instB in IterMain():
    print(instB)
