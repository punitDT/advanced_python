
i = 0

while i < 10:
    print(i)
    i += 1
else:
    print(f'loop done {i}')


for i in [1, 2, 3]:
    print(i)

for i in [1, 2, 3]:
    pass  # handle indentation


while 0 == 1:
    result = input('say something!!')
    if (result == 'bye'):
        break

while 0 == 1:
    result = input('say something!!')
    if (result != 'bye'):
        continue
    break
