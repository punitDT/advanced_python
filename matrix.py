# matrix
# n-dimensional list

matrix = [[1, 5, 3], [2, 4, 6], [7, 8, 9],]

print(matrix[0][1])  # 5

basket = [1, 2, 3, 4, 5]

print(len(basket))

# adding
new_list = basket.append(100)
print(new_list)  # None
print(basket)  # [1, 2, 3, 4, 5, 100] inplace
basket.insert(0, 200)
print(basket)
basket.extend([250, 400, 500])
print(basket)


# removing
basket.pop()  # remove last element
basket.pop(0)
basket.remove(4)
print(basket)

basket.clear()
print(basket)

basket = ['w', 'a', 'b', 'c', 'd', 'd', 'e']

print(basket.index('d', 0, len(basket)))

print('a' in basket)  # True
print('f' in basket)  # False

print(basket.count('d'))
print(sorted(basket))
# basket.sort()
print(basket)

new_basket = basket.copy()
new_basket.reverse()
print(new_basket)


print(new_basket[::-1])  # reverse

print(list(range(1, 100)))  # 0 to 99

data = ','.join(['hi','one','two'])
print(data)

# list unpacking
a,b,c, *other,d  = [1,2,3,4,5,6,7,8,9]
print(a,b,c,d)
print(other)

