
li = [1, 2, 3, 4, 5]
li2 = ['a', 'b', 'c', 'd']
li3 = [1, 2, 'a', 'b', True]

# data structure = organize information

amazon_crt = ['notebooks', 'sunglasses', 'toys', 'grapes']

# list are mutable strings are immutable
amazon_crt[0] = 'laptop'
print(amazon_crt[0:])
new_cart = amazon_crt  # same values than assign address of amazon_crt
# new_cart = amazon_crt[0:2] different value assign values
new_cart[0] = 'gum'
print(new_cart)
# change value in memory reference (when values are same assigned address not value)
print(amazon_crt)
