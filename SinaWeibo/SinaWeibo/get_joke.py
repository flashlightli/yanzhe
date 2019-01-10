# -*- coding: utf-8 -*-
import pymongo
import random
import requests
from time import strftime, localtime

client = pymongo.MongoClient(host='mongodb://123.206.31.62', port=27017)
db = client.weibo
table = db['joke']


def get_data():
    number = random.randint(0, 9)
    query = {'type': 1}
    if number < 2:
        query = {'type': 1}
    if number < 4:
        query = {'type': 2}
    if number < 8:
        query = {'type': 3}
    joke = table.find_one(query)
    path = ''
    if joke.get('imgs'):
        res = requests.get(joke.get('imgs'))
        img = res.content
        _list = joke.get('imgs').split('.')
        _ = 'temp.' + _list[-1]
        path = _
        with open('imgs/' + _, "wb") as f:  # 开始写文件，wb代表写二进制文件
            f.write(img)
    # print(joke.get('_id'))
    # qq = table.delete_one({'_id': joke.get('_id')})
    # print(qq)
    return {
        'id': joke.get('_id'),
        'content': joke.get('content'),
        'imgs': path,
    }


def del_data(id):
    del_data = table.delete_one({'_id': id})
    return del_data

a = strftime('%H', localtime())
print(int(a)>10)