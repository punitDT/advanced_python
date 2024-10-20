
# object
# methods to perform actions

# class
class BigObject:
    pass


# instance
obj1 = BigObject()
obj2 = BigObject()
obj3 = BigObject()

print(type(BigObject))
print(type(obj1))


class PlayerCharacter:

    membership = True

    # calls every time instantiate
    def __init__(self, name='anonymous', age=0):
        if (self.membership):  # or PlayerCharacter.membership
            self.name = name
            self.age = age

    def shout(self, hello):
        print(f'my name is {self.name}')
        return 'done'

    @classmethod
    def addingThings(cls, num1, num2):
        # init constrictor using cls
        return cls('Teddy', num1+num2)

    @staticmethod
    def addingThings2(num1, num2):
        # can not init constrictor using cls
        return num1+num2

    def speak(self): #encapsulation
        print(f'my name is {self.name}, and age is {self.age}')

    def test(self):
        print(f'my name is {self.name}, and age is {self.age}')


player1 = PlayerCharacter(name='Cindy', age=21)
player2 = PlayerCharacter(name='Tom', age=21.5)

player2.attack = 20

print(player1)
print(player1.addingThings(2, 3).age)

print(player1.speak())

player1.test =  'test string' # this is bad reassing value function to string

print(player1.test)

# print(player2.shout())
# print(player2.attack)
