class Person:
    moods = ("Happy", "Tired", "Lazy")

    def __init__(self, name, money, mood, healthRate):
        self.name = name
        self.money = money
        self.mood = mood
        self.__healthRate = healthRate

    def sleep(self, hours):
        if hours == 7:
            self.mood = Person.moods[0]
        elif hours > 7:
            self.mood = Person.moods[2]
        else:
            self.mood = Person.moods[1]

    def eat(self, meals):
        if meals == 1:
            self.__healthRate = 50
        elif meals == 2:
            self.__healthRate = 75
        elif meals > 2:
            self.__healthRate = 100

    def buy(self, items):
        self.money -= (items * 10)

    @property
    def healthRate(self):
        return self.__healthRate

    @healthRate.setter
    def healthRate(self, newHealthRate):
        if newHealthRate in range(0, 100):
            self.__healthRate = newHealthRate
