
from functools import reduce


my_list = [1, 2, 3]

your_list = [10, 20, 30]

their_list = [5, 4, 3]


def only_odd(item):
    return item % 2 != 0


print(list(filter(only_odd, my_list)))
print(my_list)

print(list(filter(lambda x: x % 2 == 0, my_list)))

print(list(zip(their_list, your_list)))  # [(1, 10), (2, 20), (3, 30)]


def accumulator(acc, item):
    print(acc, item)
    return acc + item


print(reduce(accumulator, my_list, 10))

print(reduce(lambda x, y: x+y, my_list, 10))


