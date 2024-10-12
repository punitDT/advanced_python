
for i in range(10):
    print(i)

for x in 'string':
    print(x)
print(x)
for x in [1, 2, 3, 4, 5]:
    print(x)

for x in {1, 2, 3, 4, 5, 5}:
    print(x)

for x in (1, 2, 3, 4, 5, 5):
    print(x)
print(x)


for i in (1,2,3,4,5):
    for j in ['a','b','c']:
        print(i,j)


# iterable list , dict, tuple, set, string can be iterate

user = {
    'name':'Golem',
    'age':5006,
    'can_swim': False
}

for key, value in user.items():
    print(key, value)

for i in user.keys():
    print(i)

for i in user.values():
    print(i)

for i in user:
    print(i) # prints keys
    print(user.get(i)) # print value
