# :=

a = 'helloooo000000000000'

if ((n := len(a)) > 10):
    print(f'too long {len(a)} element')
    print(f'too long {n} element')


while ((n := len(a)) > 1):
    print(n)
    a = a[:-1]
