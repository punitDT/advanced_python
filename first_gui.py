

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']


temp = []
for i in some_list:
    if (i in temp):
        print(i)
    temp.append(i)

for i in some_list:
    if some_list.count(i)>1:
        print(i, end=',')
