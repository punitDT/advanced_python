
# pure  function
# produce same output
# no side effect
# not interact with out of scope


def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item+2)
    return new_list

print(multiply_by2([1, 2, 3]))
