#-*- coding: utf-8 -*-

import argparse

def argParse():
    parser = argparse.ArgumentParser()
    parser.add_argument('method', type=str, required=True)
    parser.add_argument('request_url', type=str, required=True)
    args = parser.parse_args()

    return Parameters({
        'method': args.method.lower(),
        'url': args.request_url,
    })

class Parameters:
    def __init__(self, params):
        self.__params = params

    def method(self):
        return self.__params.get('method')

    def url(self):
        url = self.__params.get('url')
        if not url.startswith('http://') and not url.startswith('https://'):
            url = 'http://' + url
        return url

    def requestType(self):
        return 'normal'
