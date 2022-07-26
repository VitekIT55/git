class Dessert:
    def __init__(self):
        self.name = None
        self.cl = None

#    @staticmethod
    def setnamecl(self, name, cl):
        self.name = name
        self.cl = cl

    def getname(self):
        return self.name

    def getcl(self):
        return self.cl

    def is_healthy(self):
        if self.cl < 200:
            return True
        return False

    def is_delicious(self):
        if self.cl >= 200:
            return True
        return False


ds = Dessert()
ds.setnamecl(input('Name = '), int(input('Calories = ')))
print(ds.getname(), 'is healthy:', ds.is_healthy())
print(ds.getname(), 'is delicious:', ds.is_delicious())
#if ds.is_healthy():
#    print(ds.getname(), 'is healthy')
#else:
#    print(ds.getname(), 'is delicious')