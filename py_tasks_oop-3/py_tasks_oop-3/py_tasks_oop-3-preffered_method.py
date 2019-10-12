import requests
import re


def GetIATA():
    city_name = input('Введите название города:')

    link = 'http://autocomplete.travelpayouts.com/places2?term=' + city_name + ''
    resp_text = requests.get(link).text

    iata = re.findall('"code": "([A-Z]{3})"', resp_text)
    if iata == []:
        print('Совпадений не найдено!')
    else:
        print(iata)


if __name__ == '__main__':
    GetIATA()
