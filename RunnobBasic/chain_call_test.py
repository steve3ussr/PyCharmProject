class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


print(eval("Chain().status.user.timeline.list"))


class Student(object):
    def __init__(self):
        self._score = None
        self._age = None
        self._name = None

    def set_name(self, name=''):
        self._name = name
        return self

    def set_age(self, age=18):
        self._age = age
        return self

    def set_score(self, score=100):
        self._score = score
        return self


instA = Student().set_name("Colin").set_age(25).set_score(10000)
