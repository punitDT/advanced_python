
print(range(10))

for _ in range(0,10, 2):
    print(_)

for _ in range(10, 0, -2):
    print(_)

for i in 'hello':
    print(i)

# enumerate providing index and value

for i,char in enumerate('hello'):
    print(i, char, end="")
