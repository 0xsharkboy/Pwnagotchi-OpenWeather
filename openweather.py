import logging

import pwnagotchi.plugins as plugins

class OpenWeather(plugins.Plugin):
    __author__ = '0xsharkboy'
    __version__ = '1.0.0'
    __license__ = 'GPL3'
    __description__ = ''

    def __init__(self):
        self.options = dict()
        self.api_key = None

    def _check_options(self):
        if 'api_key' not in self.options:
            self.options["api_key"] = ""

    def on_loaded(self):
        self._check_options()
        self.api_key = self.options["api_key"]

        if self.api_key:
            logging.info('[openweather] plugin loaded.')
        else:
            logging.warning('[openweather] plugin loaded but no api key specified! Plugin will not work')