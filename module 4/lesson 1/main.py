# def strcount(s): #сложность О(N*M)
#     for sym in set(s):
#         counter = 0
#         for sub_sym in s:
#             if sym == sub_sym:
#                 counter += 1
#         print(sym, counter)


def strcount(s): #сложность О(2 + N)
    mydict = {}
    for sym in s:
        mydict[sym] = mydict.get(sym, 0) + 1

    for key in mydict:
        print(key, mydict.get(key))

strcount('aabcde')


# l = [1, 1, 2]
# print(set(l))