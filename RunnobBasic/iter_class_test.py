class Fib(object):
    def __init__(self):
        self.cnt1 = 0
        self.cnt2 = 1

    def __iter__(self):
        return self

    def __next__(self):
        (self.cnt1, self.cnt2) = (self.cnt2, self.cnt1 + self.cnt2)
        if self.cnt1 > 10000:
            raise StopIteration()
        return self.cnt1


for i in Fib():
    print(i)
    