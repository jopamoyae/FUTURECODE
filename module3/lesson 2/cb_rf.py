import requests
from bs4 import BeautifulSoup

url = 'http://www.cbr.ru/scripts/XML_daily.asp'

response = requests.get(url)
soup = BeautifulSoup(response.content, features='xml')


def get_currency(currency_id):
    valute = soup.find("Valute", ID=currency_id)

    valute_value = valute.Value.text
    valute_name = valute.Name.text

    valute_info = {'name': valute_name, 'value': valute_value}

    return valute_info
    # return soup.find('Valute', ID='R01235').Value.text

