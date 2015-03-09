#-*- coding: utf-8 -*-

import argparse

def argParse():
    parser = argparse.ArgumentParser()
    parser.add_argument('method', type=str)
    parser.add_argument('url', type=str)
    parser.add_argument('--headers', nargs='*', type=str)
    args = parser.parse_args()

    return Parameters(args)

class Parameters:
    def __init__(self, params):
        self.__params = params

    def method(self):
        return self.__params.method

    def url(self):
        url = self.__params.url
        if not url.startswith('http://') and not url.startswith('https://'):
            url = 'http://' + url
        return url

    def headers(self):
        return { k:v for k, v in [s.split(':') for s in self.__params.headers] }

    def requestType(self):
        return 'normal'
