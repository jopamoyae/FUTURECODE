# Генераторы
import time

# my_list = [time.sleep(x) for x in range(1, 3)]
my_list = (time.sleep(x) for x in range(1, 3))
for sleep in my_list:
    print(sleep)


# def my_lazy_func():
#     for i in range(0, 10):
#         yield i
#
# # print(my_lazy_func())
#
# for i in my_lazy_func():
#     print(i)

# def my_lazy_func(items):
#     yield from items
#
#
# for item in my_lazy_func([1, 2, 3, 4, 5]):
#     print(item)