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
        paramDetails = self._extract(params)
        return requests.request(
                method,
                url,
                **paramDetails
                )

    def _extract(self, params):
        return {}

def buildRequest(reqType):
    if reqType == Request.REQUEST_NORMAL:
        return NormalRequest()
    else:
        raise NotImplementedError('Undefined request type')
