# Sets
# unique values


my_set = {1, 2, 3, 4, 5, 5}

my_set.add(100)
my_set.add(2)

print(my_set)  # {1, 2, 3, 4, 5, 100}]

# print(my_set[0]) # dont work with indexes

print(1 in my_set)

my_list = [1, 2, 3, 4, 5, 5]

print(set(my_list))  # prints unique
print(list(set(my_list)))

new_set = my_set.copy()
# my_set.clear()
print(new_set)

set_one = {1, 2, 3, 4, 5, 7}
set_two = {4, 5, 6, 7, 8, 9, 10}

print(set_one.difference(set_two))

print(set_one.discard(5))
print(set_one)

print(set_one.intersection(set_two))

print(set_one & set_two)

set_one.difference_update(set_two)  # remove difference
print(set_one)


print(set_one.isdisjoint(set_two))  # TRUE for different set


print(set_one.issubset(set_two))
print(set_one.issuperset(set_two))

print(set_one.union(set_two))

print(set_one | set_two)
