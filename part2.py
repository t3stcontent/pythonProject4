# Додайте нові функції до цього класу да реалізуйте для них команди в вічному циклі

class Cat:
    def __init__(self, name):
        self.name = name
        self.age = 0
        self.health = 9
        self.energy = 100
        self.happy = 70
        self.isAlive = True

    def info(self):
        print(f"Name = {self.name} Age = {self.age} Health =  {self.health} Energy = {self.energy} Happy = {self.happy}. ALive = {self.isAlive}")

    def checkAlive(self):
        if self.happy <= 0:
            self.isAlive = False
        elif self.energy <= 0:
            self.isAlive = False
        else:
            self.isAlive = True

    def sleep(self, hours):
        self.energy += hours * 10
        print(f"Zzz Zzz Zzzz. Repair energy = {hours * 10}")
        if self.energy > 100:
            diffrence = self.energy - 100
            self.energy = 100
            self.happy -= diffrence
        self.checkAlive()

    def play(self, hours):
        self.energy -= hours * 10
        self.happy += hours * 10
        print(f"Cat play hiihihh hahahaha meow mew meow")
        self.checkAlive()

cat1 = Cat("Tom")
print("Лaсково просимо в нашу гру")
while(cat1.isAlive):
    anw = input("Введіть команду ")
    if (anw.lower() == "play"):
        hours = int(input("Скільки годин кіт буде гратися? "))
        cat1.play(hours)
    elif(anw.lower() == "sleep"):
        hours = int(input("Скільки годин кіт буде спати? "))
        cat1.sleep(hours)

    cat1.info()

print("Вибач, але твій котик попав в котячий рай")