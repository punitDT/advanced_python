
total = 100  # global var

print(total)


def some_func():
    total = 50
    return total


def some_func2():
    global total
    total += 1
    return total


def some_func3(total):
    total += 1
    return total


print(some_func3(some_func3(some_func3(total))))

print(some_func2())
print(some_func2())
print(some_func2())

print(some_func())
print(total)

# nonlocal

def outer():
    x = 'local'
    def inner():
        nonlocal x
        x = 'nonlocal'  # refers to outer variable
        print('inner', x)

    inner()
    print('outer', x)

outer()
