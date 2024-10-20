
# for i in range(5):
#     for j in range(5):
#         print(f'{i}{j} ', end='')
#     print()

n = 7

print(int(n/2))
x = int(n/2)

for i in range(n):
    for j in range(n):
        if (j == i + x or j == x-i):
            print('$', end='')
        elif (j == i-x or j == (n - 1 - i) + x):
            print('$', end='')
        else:
            print(' ', end='')
    print()

# for i in range(5):
#     for j in range(5):
#         if (i == 0 and j == 2):
#             print('*', end='')
#         if (i == 1 and j == 1):
#             print('*', end='')
#         if (i == 1 and j == 3):
#             print('*', end='')
#         if (i == 2 and j == 0):
#             print('*', end='')
#         if (i == 2 and j == 4):
#             print('*', end='')
#         if (i == 3 and j == 1):
#             print('*', end='')
#         if (i == 3 and j == 3):
#             print('*', end='')
#         if (i == 4 and j == 2):
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()

  #
 ###
#####
 ###
  #
