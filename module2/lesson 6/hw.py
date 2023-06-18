valute_from = "EUR"
valute_to = "USD"
amount = int(input('Введите сумму для конвертации: '))


def course(valute_from, valute_to, amount):
    courses = {
        "EUR": 75.4,
        "USD": 69.3,
        "RUR": 1.0
    }
    if valute_from == "RUR":
        return amount/courses[valute_to]
    else:
        return amount/courses[valute_from]*courses[valute_to]

print('Сконвертировано: ', round(course(valute_from, valute_to, amount),2))





