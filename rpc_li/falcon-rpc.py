# -*- coding: utf-8 -*-
import falcon
import json
from urllib.parse import parse_qsl
from rpc_li.rpc_function import * 


def bind(*dargs):
    def wrapper(func):
        def __wraprs(*args, **kwargs):
            end_point = dargs
            func_map[end_point] = func
            return func
        return __wraprs
    return wrapper


# @bind('test/a')
def test_a(a=1):
    print('a==', a)
    return {'a': a}


# @bind('test/b')
def test_b(b=2):
    print('b==', b)
    return {'b': b}


func_map = {
    'test/a': test_a,
    'test/b': test_b,
}


class Resource(object):
    def on_get(self, req, resp):
        resp.body = '{"message":"Hello world!"}'
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        assert isinstance(req, falcon.Request)
        assert isinstance(resp, falcon.Response)

        params = {'a': 2}
        method = 'test/a'
        func = func_map.get(method)
        import ipdb
        ipdb.set_trace()
        resp.body = json.dumps(func(**params))
        resp.status = falcon.HTTP_200


class MiddlewareTest(object):
    def process_request(self, req, resp):
        pass

    def process_resource(self, req, resp, resource, params):
        print('=====222')

    def process_response(self, req, resp, resource, req_succeeded):
        print('======3333')


api = application = falcon.API(middleware=[MiddlewareTest()])

api.add_route('/test', Resource())