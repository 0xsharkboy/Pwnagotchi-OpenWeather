import logging
import requests

import pwnagotchi.plugins as plugins

class OpenWeather(plugins.Plugin):
    __author__ = '0xsharkboy'
    __version__ = '1.0.0'
    __license__ = 'GPL3'
    __description__ = ''

    def __init__(self):
        self.options = dict()
        self.api_key = None
        self.city = None
        self.unit = None
        self.coordinates = None

    def _check_options(self):
        if 'api_key' not in self.options:
            self.options["api_key"] = ""
        if 'city' not in self.options:
            self.options["city"] = ""
        if 'unit' not in self.options:
            self.options["unit"] = "metric"
        if self.options["unit"] is not ('metric' or 'imperial' or 'standard'):
            self.options["unit"] = "metric"

    def _get_weather(self):
        if self.coordinates:
            latitude = self.coordinates["Latitude"]
            longitude = self.coordinates["Longitude"]
            url = f'http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={self.api_key}&units={self.unit}'
        else:
            url = f'http://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={self.api_key}&units={self.unit}'

        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data['main']['temp']
        else:
            return None

    def on_loaded(self):
        self._check_options()
        self.api_key = self.options["api_key"]
        self.city = self.options["city"]
        self.unit = self.options["unit"]

        if self.api_key:
            logging.info('[openweather] plugin loaded.')
        else:
            logging.warning('[openweather] plugin loaded but no api key specified! Plugin will not work')