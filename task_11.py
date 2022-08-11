class Dessert:
    def __init__(self):
        self.name = None
        self.calories = None

#    @staticmethod
    def setnamecl(self, name, calories):
        self.name = name
        self.calories = calories

    def getname(self):
        return self.name

    def getcalories(self):
        return self.calories

    def is_healthy(self):
        if (type(self.calories) == int or type(self.calories) == float) and self.calories < 200:
            return True
        return False

    def is_delicious(self):
        return True