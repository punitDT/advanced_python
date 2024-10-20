

class User:
    def singIn(self):
        print('logged in!!!')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacked with power of {self.power}')

    pass


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacked with arrows left {self.num_arrows}')

    def run(self):
        print('ran really fast')

    pass


class MybridBorg(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Wizard.__init__(self, name, power)
        Archer.__init__(self, name, arrows)
    pass


wizard1 = Wizard('Merlin', 50)
archer1 = Wizard('Robin', 500)

hb1= MybridBorg('borgie', 50, 100)

print(hb1.singIn())
