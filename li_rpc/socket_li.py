# -*- coding: utf-8 -*-
import socket
import json
import time
import socketserver
from http_server.url import *


class RpcServer(socketserver.BaseRequestHandler):

    def handle(self):
        print('thread----')
        str_content = bytes.decode(self.request.recv(1024))
        dic_success = json.loads(str_content)
        key = dic_success.get('mark')
        func_args = dic_success.get('data')
        func = UrlRemote.url_dic.get(key)
        result = func(**func_args)

        self.request.sendall(bytes(json.dumps(result), encoding="utf-8"))
        print("from conn:", self.request)


s1 = socketserver.ThreadingTCPServer(("127.0.0.1", 8080), RpcServer)
s1.serve_forever()