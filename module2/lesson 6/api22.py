import requests
from bs4 import BeautifulSoup

user_currency = input('Введите первые буквы валюты, которая вас интересует: ').capitalize()
currency_date = input('Введите дату, на которую интересует курс валют в формате dd/mm/yyyy: ')

response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp', params={'date_req': currency_date})
soup = BeautifulSoup(response.content, features='xml')

currencies_list = soup.find_all('Valute')
for currency in currencies_list:
    currency_name = currency.Name.text
    currency_value = currency.Value.text
    currency_nominal = currency.Nominal.text

    if currency_name.startswith(user_currency):
        print(f'({currency_nominal} шт.) {currency_name} стоит(ят) {currency_value} руб.')
        