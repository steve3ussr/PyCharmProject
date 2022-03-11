class Auto(object):
    def __init__(self, var_name):
        self.name = var_name

    #def __str__(self):
        #return f"{self.name} is Auto"
    #__repr__ = __str__


sti = Auto('Subaru')
print(sti)
print(dir(sti))
print(sti.__repr__())
a = 1
print(dir(a))
