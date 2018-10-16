import requests


def rpc_call(adress, **kwargs):
    print(kwargs)
    res = requests.post('http://127.0.0.1:6666/'+adress, data=kwargs)
    print(res)


def deco(func):
    def wrapper(adress, params):
        func(adress, params)
        print("111")
    return wrapper
