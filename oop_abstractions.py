# hiding info and giving necessary access
# abstract how its implemented
# public and private access
# prevent modification from user


print((1,2,3,2,1).count(2))


class PlayerCharacter:

    # calls every time instantiate
    # __ means dunder method built in method
    def __init__(self, name='anonymous', age=0):
            self._name = name  # private variable
            self._age = age

    def run(self):
        print(f'my name is {self._name}, and age is {self._age}')

    def speak(self):  # encapsulation
        print(f'my name is {self._name}, and age is {self._age}')

    def __abstractTest(self):  # encapsulation
        print(f'my name is {self._name}, and age is {self._age}')


player1 = PlayerCharacter(name='Tom', age=10)
player1.speak = 'change'
player1._name = 'name changes'

print(player1._name)

player1.__abstractTest = 'cant change'

print(player1.speak)

print(player1._abstractTest)
