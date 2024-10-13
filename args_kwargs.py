# *args **kwargs

def super_func(name, *args, i='hi', **kwargs):
    print(i)
    print(name)
    print(args)  # tuple of arguments (1, 2, 3, 4, 5)
    print(kwargs)  # dict of arguments {'num1': 4, 'num2': 3}
    return sum(args) + sum(kwargs.values())


print(super_func('punit', 1, 2, 3, 4, 5, num1=4, num2=3))

# Rule: params, *args, default parameters, **kwargs
