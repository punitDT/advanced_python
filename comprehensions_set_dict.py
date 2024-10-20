

my_list1 = {char for char in 'hello'}
print(my_list1)

my_list2 = {num for num in range(0, 10)}

print(my_list2)

simple_dict = {
    'a': 1,
    'b': 2
}

my_dict = {key: value for key, value in simple_dict.items()}

print(my_dict)


my_dict2 = {key: value**2 for key, value in simple_dict.items() if value %
            2 == 0}

print(my_dict2)


my_dict3 = {num:num*2 for num in [1,2,3]}
print(my_dict3)


my_list = ['a','b','c','b','d','m','n','n']

my_duplicate_list = list(
    set([num for num in my_list if my_list.count(num) > 1]))

print(my_duplicate_list)
