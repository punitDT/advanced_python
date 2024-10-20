# list, set, dictionary

my_list = []

for char in 'hello':
    my_list.append(char)


print(my_list)


my_list1 = [char for char in 'hello']
print(my_list1)


my_list2 = [num for num in range(0, 10)]

print(my_list2)

my_list3 = [num*2 for num in range(0, 10)]

print(my_list3)

my_list4 = [num for num in range(0, 10) if num % 2 == 0]

print(my_list4)
