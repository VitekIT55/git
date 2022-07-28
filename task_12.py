class SetName:
    def __init__(self):
        self.name = None
        self.cl = None
        self.flavor = None

    def setname(self, name, cl, flavor):
        self.name = name
        self.cl = cl
        self.flavor = flavor


class JellyBean:
    def __init__(self):
        SetName.__init__(self)

    def getfl(self):
        return self.flavor


class Dessert(JellyBean, SetName):
    def __init__(self):
        SetName.__init__(self)

    def getname(self):
        return self.name

    def getcl(self):
        return self.cl

    def is_healthy(self):
        if self.cl < 200:
            return True
        return False

    def is_delicious(self):
        if self.flavor == 'black licorice':
            return False
        return True


#ds = Dessert()
#ds.setname(input('Name = '), int(input('Calories = ')), input('Flavor = '))
#print(ds.getname(), 'is healthy:', ds.is_healthy())
#print(ds.getname(), 'is delicious:', ds.is_delicious())
