#-*- coding: utf-8 -*-

import requests

class Request:
    REQUEST_NORMAL = 'normal'

    def execute(self, params):
        raise NotImplementedError("Implement execute method")

class NormalRequest(Request):
    def execute(self, params):
        method = params.method()
        url = params.url()
        param = self._extract(params)
        return requests.request(
                method,
                url,
                **param
                )

    def _extract(self, params):
        return {
                'headers': params.headers()
                }

def buildRequest(reqType):
    if reqType == Request.REQUEST_NORMAL:
        return NormalRequest()
    else:
        raise NotImplementedError('Undefined request type')
