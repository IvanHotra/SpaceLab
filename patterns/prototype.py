import copy

class Prototype:
    def __init__(self,name):
        self.list = []
        self.list.append(name)
    def clone(self,*args):
        obj = copy.deepcopy(self.list[0])
        return obj

class Copy:pass

prototype = Prototype(Copy)
copy = prototype.clone('wwe')
print(type(copy))