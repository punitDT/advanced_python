# map


my_list = [1, 2, 3]


def multiply_by2(item):
    return item*2


def multiply_by21(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list


print(map(multiply_by2, my_list))

print(list(map(multiply_by2, my_list)))

print(list(map(lambda item: item*-1, my_list)))

print(multiply_by21(my_list))

print(my_list)
