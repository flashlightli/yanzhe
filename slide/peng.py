import requests
from lxml import html
from time import strftime, localtime
from slide.util import gm_decode_html
import pymongo
client = pymongo.MongoClient(host='mongodb://123.206.31.62', port=27017)
db = client.weibo
table = db['joke']

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}


def slide(url):
    res = requests.get(url, headers=headers)
    res.encoding = 'UTF-8'
    tree = html.fromstring(res.text)
    content = tree.xpath('//*[@class="list-item bg1 b1 boxshadow"]')#/dl/dd/h1/a/text()
    img = tree.xpath('//*[@class="content-img clearfix pt10 relative"]/img/@src')
    text = tree.xpath('//*[@class="content-img clearfix pt10 relative"]/text()')
    print(content)
    for item in content:
        pic = item.xpath('dl/dd/*[@class="content-img clearfix pt10 relative"]/img/@src')
        pic_content = item.xpath('dl/dd/h1/a/text()')
        text_content = item.xpath('dl/dd/*[@class="content-img clearfix pt10 relative"]/text()')
        _ = ''
        for i in text_content:
            _ += str(i).replace('\n\t\t\t\t\t\t\t\t\t\t', '').replace('\r\n', '').replace('\t\t\t\t\t\t\t\t\t', '')

        data = {
            'type': 3,  #捧腹网
            'content': pic_content if pic_content else text_content,
            'imgs': pic[0] if pic else '',
            'create_time': strftime('%Y-%m-%d', localtime()),
        }
        table.insert(data)


for index in range(1, 50):
    url = 'https://www.pengfu.com/index_{page}.html'.format(page=index)
    slide(url=url)
    print(str(index) + ' is done')