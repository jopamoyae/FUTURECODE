# class Item:
#     def __init__(self, price, brand):
#         self.price = price
#         self.brand = brand
#
#     def __repr__(self):
#         return self.brand
#
#
# items_list = [
#     Item(1000, "Apple"),
#     Item(1200, "Apple"),
#     Item(900, "Samsung"),
#     Item(700, "Samsung"),
#     Item(660, "Xiaomi")
# ]
#
# result = list(filter(lambda i: i.brand == 'Apple', items_list))
# print(result)

# result2 = [x for x in items_list if x.brand == 'Samsung']
# print(result2)

names_list = ['данил', 'артём', 'никита', 'влад']

result = [i.capitalize() for i in names_list]
print(result)