
def test(a):
    '''
    INFO: this function tests and prints
    '''
    print(a)


help(test)  # prints info
print(test.__doc__)
test('!!!!')


# clean code

def is_odd_or_even(num):
    if num % 2 == 0:
        return True
    elif num % 2 != 0:
        return False


print(is_odd_or_even(52))


def is_even(num):
    return num % 2 == 0


print(is_even(52))   
