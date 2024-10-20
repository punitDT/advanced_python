

def say_hello():
    print('hello!!!')
    for i, char in enumerate('hello'):
        print(i, char, end="")


say_hello  # not calling
print(say_hello)  # prints location

say_hello()  # calling
say_hello()

print('  ')

# parameters default


def test_function(name='default', emoji='default emoji'):
    print(name, emoji)
    pass


# parameters positional
test_function('test', 'two')
test_function('test2', 'two2')
test_function('test3', 'two3')

# keyword argument
test_function(emoji='emoji', name='test4')

# default parameter
test_function('fisttest')


def highest_even(li):
    evens = []
    for x in li:
        if (x % 2 == 0):
            evens.append(x)
    return max(evens)


print(highest_even([10, 2, 3, 4, 8, 7, 17, 18]))
