# coding=utf-8
import sys


def main(args):
    host = '127.0.0.1'
    port = 9000
    service_name = 'winners'

    try:
        service_name = args[0]
        second_arg = args[1]
    except IndexError:
        pass
    else:
        if ':' in second_arg:
            host, port = second_arg.split(':')
            port = int(port)
        else:
            port = int(second_arg)
    print('Server {} running on {}:{}'.format(service_name, host, port))
    to_run(host=host, port=port)


def running():
    sys.exit(main(sys.argv[1:]))


if __name__ == '__main__':
    running()