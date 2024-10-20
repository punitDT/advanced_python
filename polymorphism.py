

class User:
    def __init__(self, email):
        self.email = email

    def singIn(self):
        print('logged in!!!')

    def attack(self):
        print(f'do nothing!!!')


class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        User.attack(self)
        print(f'attacked with power of {self.power}')

    pass


class Archer(User):
    def __init__(self, name, num_arrows, email):
        super().__init__(email)
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacked with arrows left {self.num_arrows}')

    pass


wizard1 = Wizard('Merlin', 50, 'email')
archer1 = Archer('Robin', 500, 'email')

# introspection - ability to determine object type at run time
print(dir(wizard1))

print(wizard1.email)


for char in [wizard1, archer1]:
    char.attack()

