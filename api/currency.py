import configparser
import datetime
import requests
import time


def get_api_key():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['openweathermap']['api']


def get_domain():
    return 'https://api.openweathermap.org/'


def get_weather(loc):
    url = get_domain() + "data/2.5/weather?q={}&units=metric&appid={}".format(loc, get_api_key())
    r = requests.get(url)
    return r.json()


def compare_two_cities_temp():
    cities = ['Los Angeles', 'New York City']

    data = dict()

    for city in cities:
        timestamp = datetime.datetime.fromtimestamp(get_weather(city)['dt'])
        celsius = get_weather(city)['main']['temp']
        fahrenheit = (celsius * 9 / 5) + 32

        data[city] = int(fahrenheit)

        # print('Location: {}'.format(location))
        # print('Time: {}'.format(timestamp.strftime('%Y-%m-%d %H:%M:%S')))
        # print('Temperature:{}'.format(int(fahrenheit)))
        # print('========================================')

    if data[cities[0]] > data[cities[1]]:
        print('{} is hotter than {}'.format(cities[0], cities[1]))
    else:
        print('{} is hotter than {}'.format(cities[1], cities[0]))


def post_dummy_msg():
    time.sleep(3)
    return 'dummy message post'


def post_comments(api, message):
    if len(message) >= 0:
        res = post_dummy_msg()
    else:
        res = 'bad request'
    return res


if __name__ == '__main__':
    compare_two_cities_temp()
