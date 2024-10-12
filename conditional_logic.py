
is_old = True
is_licensed = True

if is_old and is_licensed:
    print('can drive')

if is_old:
    print('older to drive')
elif is_licensed:
    print('can drive')
else:
    print('else block')

print('Outer if')


# Truthy and Falsy

# Truthy
print(bool('hello'))

# Falsy
print(bool(0))

username = 'test'
password = 'johnny'

if username and password:
    print(f'{username}:{password}')

# Ternary Operator
is_test = True
can_message = 'message allowed' if is_test else 'not allowed'

print(can_message)

test_ternary = 'a' if True else 'b'

# Short Circuiting
is_test = False
is_test_two = True

print(is_test and is_test_two)

if is_test or is_test_two:
    print('or operator')


# logical operators

print(4 == 5)
print('a' > 'A')
print(1 < 2 > 3 < 4)
print(1 != 2)

print(not (True))

is_magician = False
is_expert = True

# check if magician

if is_expert and is_magician:
    print('magician')
elif is_magician and not is_expert:
    print('not expert')
elif not is_magician:
    print('not magician')


print(10==10.0)

a = [1,2,3]
b = [1,2,3]

print(a is b)
print(b is b) # match references

