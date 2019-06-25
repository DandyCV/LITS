import requests
import json
import argparse


def weather(city, language):

    params = {
        'APPID': 'b64a35cdd04a1caa08cf1d64cc08e0b1',        #персональний ключ для доступу до API
        'lang': language,
        'q': city
}
    r = requests.get('https://api.openweathermap.org/data/2.5/weather?', params=params)
    data = json.loads(r.text)

    if data['cod'] == '404':
        print('Місто не знаедене. Можливо Ви ввели неправильно назву!')
    else:
        wind_d = round(data['wind']['deg']/45)              #визначаємо напрямок вітру
        wind = {
            0: "Північний",
            1: "Північно-східний",
            2: "Східний",
            3: "Південно-східний",
            4: "Південний",
            5: "Південно-західний",
            6: "Західний",
            7: "Північно-західний",
            8: "Північний"
}
        wind_deg = wind[wind_d]
        data['wind']['deg'] = wind_deg

        press = round(data['main']['pressure']*0.750062)    #переводимо тиск в мм.рт.ст та округлюємо до цілих
        data['main']['pressure'] = press

        temp = round(data['main']['temp']-273.15)           #переводимо температуру в °C та округлюємодо цілих
        data['main']['temp'] = temp

        print('Пгода у місті ' + city + ''':
Стан неба - {weather[0][description]}
Температура повітря - {main[temp]}°C
Атмосферний тиск - {main[pressure]} мм.рт.ст
Вологість повітря - {main[humidity]}%
Швидкіть вітру - {wind[speed]} м/с
Напрямок вітру - {wind[deg]}'''.format(**data))


def weather_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-name', '--city_name', dest='city_name', type=str)
    parser.add_argument('-lang', '--language', dest='language', default='ua', type=str)
    args = parser.parse_args()

    weather(args.city_name, args.language)


weather_parser()