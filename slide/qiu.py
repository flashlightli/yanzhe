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


def slider(url):
    res = requests.get(url, headers=headers)
    tree = html.fromstring(res.text)
    content = tree.xpath('//*[@id="content-left"]/div')

    for item in content:
        result = item.xpath('*[@class="contentHerf"]//span/text()')  #需要获取的数据
        imgs = item.xpath('*[@class="thumb"]//img/@src')
        _ = ''
        for words in result:
            if words == '查看全文':
                _ = ''
            elif '\n\n\n' in words:
                _ = '' + str(words).replace('\n\n\n', '').replace('\n\n', '').replace('\n', '')
            else:
                _ += str(words).replace('\n\n', '').replace('\n', '')
        imgs = ['http:' + img for img in imgs]
        data = {
            'type': 1,  #糗事百科
            'content': _,
            'imgs': imgs[0] if imgs else '',
            'create_time': strftime('%Y-%m-%d', localtime()),
        }
        table.insert(data)


for index in range(1, 14):
    url = 'https://www.qiushibaike.com/hot/page/{page}/'.format(page=index)
    try:
        slider(url)
        print(str(index) + ' is done')
    except:
        pass