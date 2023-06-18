# def numbers(*args):
#     a = list(args)
#
#     c = [i for i in a if i % 2 != 0]
#
#     b = [i for i in a if i % 2 == 0]
#     return b, c
#
#
# print(numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


# def generator(*args):
#     return [list(filter(lambda x: x % 2 == i, args)) for i in range(2)]
#
# print(generator(1, 11, 23, 432, 5432, 6543, 213, 1234, 432, 9))
#

a = (5, 3, 2, 1, 4)
b = tuple(sorted(a))
print(b)