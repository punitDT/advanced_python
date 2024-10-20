

class User:
    def singIn(self):
        print('logged in!!!')


class Wizard(User):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacked with power of {self.power}')

    pass


class Archer(User):
    def __init__(self, name, num_arrows):
        super().__init__()
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacked with arrows left {self.num_arrows}')

    pass


wizard1 = Wizard('Merlin', 50)
archer1 = Wizard('Robin', 500)


wizard1.attack

print(wizard1.singIn())

print(wizard1.attack())


print(isinstance(wizard1, User))
