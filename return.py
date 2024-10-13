
def sum(num1, num2):
    return num1+num2


total = sum(10, 5)
print(sum(2, total))


def sum2(num1, num2):
    def another_fun(n1, n2):
        return n1+n2
    return another_fun(num1, num2)


print(sum2(2, 3))
