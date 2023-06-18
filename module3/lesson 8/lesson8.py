import pprint

if __name__ == "__main__":
    goods = [
        {
            'name': 'Iphone 7',
            'brand': 'Apple',
            'price': 400
        },
        {
            'name': 'Ipad',
            'brand': 'Apple',
            'price': 500
        },
        {
            'name': 'Windows 7',
            'brand': 'Microsoft',
            'price': 200
        }
    ]

    # sorted, lambda
    def on_price(item):
        return item['price']


    print(sorted(goods, key=on_price))

    print(sorted(goods, key=lambda item: item['price']))

    # почти не используется память, т.к. итератор(filter)
    filtered_list = filter(lambda item: item['brand'] == 'Apple', goods)
    print(filtered_list)
    print(list(filtered_list))

    # map
    num_list = ['1', '2', '3', '4', '5']
    print(num_list)
    mapped_list = list(map(int, num_list))
    print(mapped_list)

    names_list = ['Данил', 'Эльвира', 'Данил']
    surnames_list = ['Федоров', 'Ибрагимова', 'Устюжин']
    person_list = list(map(lambda name, surname: f'{name} {surname}', names_list, surnames_list))
    print(person_list)

    # enumerate
    indexed_goods = []

    for index, item in enumerate(goods):
        indexed_goods.append({index: item})

    pprint.pprint(indexed_goods)

    # zip(итерирует два списка)
    names_list = ['Марсель', 'Максим', 'Алексей']
    surnames_list = ['Тарапатин', 'Словягин', 'Щербаков']

    for name, surname in zip(names_list, surnames_list):
        print(name, surname)

    #__name__
    print(__name__)
else:
    print('Another script.')