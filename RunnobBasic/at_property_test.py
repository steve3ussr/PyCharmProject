class Student(object):

    def __init__(self, k):
        self._value = k

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, i):
        # check value
        if not isinstance(i, int):
            raise ValueError('int only, you fool')
        elif 0 <= i <= 100:
            pass
        else:
            raise ValueError('[0, 100] only, you fool')
        # set value
        self._value = i

    @property
    def inv_value(self):
        return 100 - self._value


instA = Student(45)
print(instA.inv_value)
instA.value = 1
print(instA.inv_value)
print(dir(instA))
