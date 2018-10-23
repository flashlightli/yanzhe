from lxml import html
from time import strftime, localtime
import requests
res = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<div id="a"><a><p class="22">aaa</p></a>
<span></span></div>
<div><p>qqq</p></div>
</body>
</html>
"""
tree = html.fromstring(res)
content = tree.xpath('//*[@id="a"]')
print(content)
a = content[0].xpath('a/p[@class="22"]/text()')
print(a)
b = content[0].xpath('//p/text()')
print(b)


# def a():
#     for index in range(1,21):
#         if index == 3:
#             break
#         print("1")
#
#
# for i in range(1, 20):
#     for index in range(1, 21):
#         if index == 3:
#             exit('2333')
#         print(i, '===', index)

print(strftime('%Y-%m-%d', localtime()))

res = requests.get('http://image6.pengfu.com/origin/181019/5bc970324a7a4.gif')
img = res.content
with open('./slide', "wb") as f:  # 开始写文件，wb代表写二进制文件
    f.write(img)
