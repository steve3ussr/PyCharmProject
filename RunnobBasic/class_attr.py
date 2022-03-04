class Human(object):
    def __init__(self):
        pass

    name = "Human_defaultName"


lyb = Human()
tny = Human()
lyb.name = "lybKing"
print(lyb.name)
print(tny.name)
del lyb.name
print(lyb.name)
