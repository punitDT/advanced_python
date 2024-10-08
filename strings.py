
print(type('its string'))

username = 'username'
password = 'password'

logString = '''
WOW
0 0
---
'''

print(logString)


fullName = 'test' + ' ' + 'one'

print(fullName)

# string concat
print('string'+'concat')

# print('string'+5) # error

print(type(int(str(100))))

print('string'+str(5))

#Escape sequence
weather = "\tIt's \"kind of\" sunny \n good day!!!"
print(weather)

# formatted strings

name = 'Punit'
age = 55

print(f'hi {name}. you are {age} years old')
print('hi {}. you are {} years old'.format('punit', '55'))
print('hi {}. you are {} years old'.format(name, age))
