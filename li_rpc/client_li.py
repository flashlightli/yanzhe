# -*- coding: utf-8 -*-
import socket
import json

demo_dic = {"mark": "mark1", "data": {"a": 1, "b": 2}}
for i in range(100):
    obj = socket.socket()
    obj.connect(("127.0.0.1", 8080))
    obj.send(json.dumps(demo_dic).encode('utf-8'))
    ret = str(obj.recv(1024), encoding="utf-8")
    temp = json.loads(ret)
    print('返回内容', temp)