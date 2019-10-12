import requests
import json


def GetIATA():
    city_name = input('Введите название города:')

    link = 'https://www.travelpayouts.com/widgets_suggest_params?q=Из%20' + city_name + '%20в%20Лондон'

    data = json.loads(requests.get(link).text)

    try:
        print(data['origin']['iata'])
    except (KeyError):
        print('Совпадений не найдено!')


if __name__ == '__main__':
    GetIATA()
