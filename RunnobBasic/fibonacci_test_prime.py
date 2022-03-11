class Fib(object):
    def __init__(self, j):
        """j is the limit of iterations"""
        self.a = 0
        self.b = 1
        self.limit = j
        self.cnt = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        self.cnt += 1
        if self.cnt <= self.limit:
            return self.a
        else:
            raise StopIteration()


for instA in Fib(10):
    print(instA)
