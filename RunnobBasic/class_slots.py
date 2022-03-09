class Human(object):
    __slots__ = ('name', 'age')
    a = 1


class Nigger(Human):
    __slots__ = 'jjlen'


class White(Human):
    pass


testA = Human()
try:
    testA.jjlen = 16
except AttributeError:
    pass

testB = Nigger()
testB.jjlen = 100
testB.name = 'Michael'
testB.age = "111"
testB.ana = 'fes'

testC = White()
testC.name = "Alice"
testC.fewfq = 'fdew'
