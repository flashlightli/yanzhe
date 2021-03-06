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
proxies = {
  'http': 'http://221.195.74.74:80',
}


def slider(url):
    res = requests.get(url, headers=headers, proxies=proxies)
    res.encoding = 'UTF-8'
    tree = html.fromstring(res.text)
    content = tree.xpath('//*[@class="xhlist"]')
    for item in content:
        text = item.xpath('dd/text()')
        pic = item.xpath('dd/img/@src')
        _ = ''
        for i in text:
            _ += str(i).replace('\r\n', '')
        data = {
            'type': 4,  # 别逗了
            'content': _,
            'imgs': pic[0] if pic else '',
            'create_time': strftime('%Y-%m-%d', localtime()),
        }
        table.insert(data)


for index in range(2, 26649):#21300
    url = 'https://www.pengfu.com/index_{page}.html'.format(page=index)
    slider(url=url)
    print(str(index) + ' is done')