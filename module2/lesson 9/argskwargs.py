# def func(a, b, *args, **kwargs):
#     print(a, b)
#     print(args)
#     print(kwargs.get('name'))
#
#
# func(10, 20, 30, 40, 50, 60, 70, name='Эльвира')


# def func(a, b="Apple"):
#     print(a, b)
#
#
# # func(10, "Samsung")
# func(10)
# сначала все позиционные параметры, а только птом именнованные


# тернарный условный оператор

# age = 18

# if age >= 18:
#     is_allow = 'Можно'
# else:
#     is_allow = 'Нельзя'
#
# print(is_allow)

# citizenship = 'РФ'
# is_allow = 'Можно' if age >= 18 and citizenship == 'РФ' else 'Нельзя'
# print(is_allow)


# возвращает только правду
# a = True
# b = False
#
# c = a or b
#
# print(c)


# my_list = [i if i % 3 == 0 else i ** 2 for i in range(1000) if i % 5 == 0]
#
# print(my_list)


# my_dict = {i: len(i) for i in {'orange', 'green', 'blue'} if len(i) != 5}
# print(my_dict)


# my_list_1 = [1, 2]
# my_list_2 = [1, 2]
#
# a = 20
# b = 20

# print(my_list_1 == my_list_2)
# print(my_list_1 is my_list_2)
# print(a is b)
# print(id(a), id(b))
# print(id(my_list_1), id(my_list_2))


# my_tuple = (1, 2, 3, 4, 5)
# print(type(my_tuple))
# print(my_tuple.count(4))
# print(my_tuple[4])
# print(my_tuple[2:4])


# my_list = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
# my_set = set(my_list)
# print(my_set)

# пересечение множеств и объединение
# my_set = {1, 2, 3, 4, 5}
# my_set_2 = {4, 5, 6, 7, 8}
# print(my_set.intersection(my_set_2))
# print(my_set.union(my_set_2))