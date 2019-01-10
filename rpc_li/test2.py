# -*- coding: utf-8 -*-
#from test3 import Test
import math
import time
import datetime
from operator import itemgetter

from multiprocessing import Pool, Manager

from django.core.management.base import BaseCommand
from django.db.models import Q, Max
from django import db

def handle(kwargs):
    print(kwargs)


def handle2():
    queue = Manager().Queue(maxsize=4)
    queue.put(0)  # 触发程序开始

    per_num = 2
    all_record = [1, 2, 3, 4, 5, 6, 7, 8]
    count = 8
    cnt = int(math.ceil(count / per_num))

    pool = Pool(processes=4)
    arg_list = []
    for _ in range(cnt):
        arg_list.append({'qq': 1212, 'qqe': 13})
    pool.map(handle, arg_list)
    pool.close()
    pool.join()
    end_time = time.time()
    print("end at: ", end_time)
    print('total use {} s.'.format(end_time))
    print('Done!')


handle2()