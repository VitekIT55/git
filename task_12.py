class SetName:
    def __init__(self):
        self.name = None
        self.calories = None
        self.flavor = None

    def setname(self, name, calories, flavor):
        self.name = name
        self.calories = calories
        self.flavor = flavor


class Dessert:
    def __init__(self):
        SetName.__init__(self)

    def getname(self):
        return self.name

    def getcalories(self):
        return self.calories

    def is_healthy(self):
        if type(self.calories) == int and self.calories < 200:
            return True
        return False


class JellyBean(Dessert, SetName):
    def __init__(self):
        SetName.__init__(self)

    def getflavor(self):
        return self.flavor

    def is_delicious(self):
        if self.flavor == 'black licorice':
            return False
        return True

