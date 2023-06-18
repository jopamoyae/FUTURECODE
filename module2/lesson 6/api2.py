import requests
from bs4 import BeautifulSoup

response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
soup = BeautifulSoup(response.content, features='xml')



# def get_course(currency_id):
#     australian_dollar = soup.find('Valute', ID=currency_id)
#
#     currency_value = australian_dollar.Value.text
#     currency_nominal = australian_dollar.Nominal.text
#     currency_name = australian_dollar.Name.text
#
#     print(f'({currency_nominal} шт.) {currency_name} стоит(ят) {currency_value} руб.')


belorus_ruble = soup.find('Valute', ID="R01090B")

currency_value2 = belorus_ruble.Value.text
currency_nominal2 = belorus_ruble.Nominal.text
currency_name2 = belorus_ruble.Name.text

print(f'({currency_nominal2} шт.) {currency_name2} стоит(ят) {currency_value2} руб.')

dollar_usa = soup.find('Valute', ID="R01235")

currency_value3 = dollar_usa.Value.text
currency_nominal3 = dollar_usa.Nominal.text
currency_name3 = dollar_usa.Name.text

print(f'({currency_nominal3} шт.) {currency_name3} стоит(ят) {currency_value3} руб.')




# currencies_list = soup.find_all('Valute')
# for currency in currencies_list:
#     get_course(currency['ID'])
