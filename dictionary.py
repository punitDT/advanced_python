# dictionary un ordered key value pair
# data type and data structure


dictionary = {
    'a': [1, 2, 3],
    'b': 'test',
    'c': False
}

print(dictionary['b'])
print(dictionary['a'][1])

my_list = [{
    'a': [1, 2, 3],
    'b': 'test',
    'c': False
}, {
    123: [4, 5, 6],
    True: 'test',
    # [100]: False # key has to be immutable
    '[100]': False
}
]

print(my_list[0]['a'][2])
print(my_list[1]['[100]'])

dict_one = {
    '123': [1, 2, 3],
    '123': 'hello'  # key has to be unique otherwise overrided
}

print(dict_one['123'])

user = {
    'basket': [1, 2, 3],
    '123': 'hello'
}

# print(user['age']) throws error
print(user.get('age'))  # returns None
print(user.get('age', 55))  # default value
print(user.get('basket'))


user2 = dict(name='test', sub='eng')  # wrong dict('name'='test')
print(user2)

print('basket' in user)
print('basket' in user.keys())
print('basket' in user.values())
print('basket' in user.items())

print(user.items())

user3 = user2.copy()

user2.clear()
print(user2)
print(user3)
print(user3.pop('name'))
print(user3.popitem()) # randomly pop
print(user3)

print(user3.update({'age':65}))
print(user3.update({'ages': 65}))

print(user3)
