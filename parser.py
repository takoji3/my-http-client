#-*- coding: utf-8 -*-

import argparse
from request import REQUEST_PLAIN,REQUEST_OAUTH

def arg_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('method', type=str)
    parser.add_argument('url', type=str)
    parser.add_argument('--type', type=str, choices=[REQUEST_PLAIN, REQUEST_OAUTH], default='plain', required=False)
    parser.add_argument('--headers', nargs='*', type=str, default={})
    parser.add_argument('--data', nargs='*', type=str)
    parser.add_argument('--consumer_key', type=str, required=False)
    parser.add_argument('--consumer_secret', type=str, required=False)
    parser.add_argument('--access_token', type=str, required=False)
    parser.add_argument('--access_token_secret', type=str, required=False)
    parser.add_argument('-d', nargs='?', const=True, default=False, type=bool, required=False)
    args = parser.parse_args()

    return Parameters(args)

class Parameters:
    def __init__(self, params):
        self._params = params

    def method(self):
        return self._params.method.lower()

    def url(self):
        url = self._params.url
        if not url.startswith('http://') and not url.startswith('https://'):
            url = 'http://' + url
        return url

    def headers(self):
        return { k:v for k, v in [s.split(':') for s in self._params.headers] }

    def data(self):
        return { k:v for k, v in [s.split(':') for s in self._params.data] }

    def request_type(self):
        return self._params.type.lower()

    def oauth_parameters(self):
        oauth_params = [self._params.consumer_key, self._params.consumer_secret]
        try:
            tokens = [self._params.access_token, self._params.access_token_secret]
            oauth_params.extend(tokens)
        finally:
            return oauth_params

    def debug(self):
        return self._params.d
