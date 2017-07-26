# Exercise 3.9: Implement the sum function


def sum(values_list):
    r = type(values_list[0])()
    for value in values_list:
        r += value
    return r

print(sum([2,2,2]))
print(sum(["Hi", ":)"]))
print(sum([[2,1,2,5], [6,2,1], [8,8,8]]))