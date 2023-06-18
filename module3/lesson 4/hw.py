import contextlib
import requests
from bs4 import BeautifulSoup
from datetime import datetime
# # 1 способ(генераторное выражение)
# squares = (n ** 2 for n in range(1_000_001))
# for square in squares:
#     print(square)
#
# # 2 способ(списковое включение)
# squares2 = [n ** 2 for n in range(1_000_001)]
# for square in squares2:
#     print(square)
#
# # 3 способ(генераторная функция)
# def squares(length):
#     for n in range(length):
#         yield n ** 2
#
# for square in squares(1_000_001):
#     print(square)

@contextlib.contextmanager
def get_currency(currency_id):
    today = datetime.today().strftime('%d.%m.%Y')
    response = requests.get("http://www.cbr.ru/scripts/XML_daily.asp", params={'date_req': today})

    soup = BeautifulSoup(response.content, features='xml')
    valute = soup.find("Valute", ID=currency_id)

    valute_value = valute.Value.text
    valute_name = valute.Name.text

    valute_info = {'name': valute_name, 'value': valute_value}

    return valute_info


currency_id = input("Введите айди валюты: ")
print(get_currency(currency_id)['name'], get_currency(currency_id)['value'])
