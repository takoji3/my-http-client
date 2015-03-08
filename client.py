#-*- coding: utf-8 -*-

from parser import argParse
from request import buildRequest

def run():
    params = argParse()
    request = buildRequest(params.requestType())
    response = request.execute(params)
    print response.status_code
    print "\n".join(["{}: {}".format(k, v) for k, v in response.headers.items()])
    #print response.content

if __name__ == '__main__':
    run()