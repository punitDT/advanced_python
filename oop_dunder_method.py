
class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age

    def __str__(self):  # modify dander method
        return f'{self.color}'

    def __len__(self):
        return 5

    def __del__(self):
        print('deleted')

action_figure = Toy('red', 0)

print(action_figure.__str__())
print(action_figure.__len__())
print(action_figure.__del__())
print(str(action_figure))
