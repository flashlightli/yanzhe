from rpc_li.rpc_client import rpc_call


def call():
    rpc_call('api/rpc', a=2, b=3)


if __name__ == '__main__':
    call()
