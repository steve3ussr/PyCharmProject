class Human(object):
    __slots__ = ('name', 'age')
    a = 1

class Nigger(Human):
    __slots__ = 'jjlen'

class White(Human):

    pass

testA = White()
testA.dd = 1 # 没有约束

testB = Nigger()
testB.jjlen = 100
testB.name = 'Michael'
testB.age = "111"
# testB.ana = 'fes'

testC = White()
testC.name = "Alice"
testC.fewfq = 'fdew'
# testB.dd = 1 # AttributeError
print(testB.__slots__)
testB.name = "aa" # No error

'''
1. 廖雪峰说的没错
2. __slot__的原理
3. __slots__的“继承”非同寻常
4. __slots__月缺点
'''

print(dir(Human))
print(dir(White))
print(dir(Nigger))
print(Human.__slots__)
print(White.__slots__)
print(Nigger.__slots__)

