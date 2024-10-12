# Tuple immutable list
my_tuple = (1,2,3,4,5,5)

# my_tuple[1] = 'x' #unmodifiable

dictionary = {
    (1,2): [1, 2, 3], # tuple is valid key
    'b': 'test',
    'c': False
}

print(dictionary.items())

new_tuple = my_tuple[1:2]

print(new_tuple)

x,y,z, *other = (1, 2, 3, 4, 5)

print(len(my_tuple))
print(my_tuple.count(5))
print(my_tuple.index(4))
