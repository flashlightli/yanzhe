#!/usr/bin/python
# -*- coding: utf-8 -*-
from SinaWeibo.SinaWeibo.weibo import Weibo
from SinaWeibo.SinaWeibo.get_joke import get_data, del_data
from time import strftime, localtime, time


if __name__ == '__main__':
    while True:
        hour = strftime('%H', localtime())
        if int(hour) >= 7 and int(hour) <= 23:
            wb = Weibo("17640215379", "lizhe184")
            data = get_data()
            if data.get('imgs'):
                wb.postImage(data.get('content'), "imgs/" + data.get('imgs'))
            else:
                wb.postMessage(message=data.get('content'))

            del_data(data.get('id'))
        time.sleep(3600)


    #wb.postMessage(message="0.2测试1:文本")
    # time.sleep(1)
    # wb.postImage("0.2测试2:一张图片","/Downloads/4.png")
    # time.sleep(1)
    #wb.postImage("0.2测试3:多张图片","../imgs/temp.jpg")
    # # 我的关注
    # pageNum = 1
    # followList, hasNext = wb.getFollowList(pageNum)
    # print(followList)
    # while hasNext == True:
    #     pageNum = pageNum + 1
    #     followList, hasNext = wb.getFollowList(pageNum)
    #     print(followList)
    #
    # # 我的粉丝
    # pageNum = 1
    # fansList , hasNext = wb.getFansList(pageNum)
    # print(fansList)
    # while hasNext == True:
    #     pageNum = pageNum + 1
    #     fansList, hasNext = wb.getFansList(pageNum)
    #     print(fansList)
    #
    # # 我的微博
    # blogList = wb.getMyBlogList(1)
    # for blog in blogList:
    #     print(blog)


