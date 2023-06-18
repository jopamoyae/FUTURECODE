import contextlib

# file = open('test.txt', 'w', encoding='utf-8')
# file.write('Вебинарчик)')
# file.close()

# with open('test.txt', 'w', encoding='utf-8') as file:
#     file.write('Вебинарчик)')


# @contextlib.contextmanager
# def reverse_str(string):
#     yield string[::-1]
#
#
# with reverse_str('hello') as reversed_string:
#     print(reversed_string)


@contextlib.contextmanager
def exc_handler(*args):
    try:
        yield
    except args:
        print('Mistake, but..')

my_list = [1, 2]
my_dict = {1: 1}

with exc_handler(IndexError, ValueError, KeyError):
    my_list[4]
    print(my_list.asd)
    my_dict[2]