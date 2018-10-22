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
    content = tree.xpath('//*[@class="content"]/article')
    for item in content:
        time = item.xpath('header/p/time/text()')
        # if time.strip() != strftime('%Y-%m-%d', localtime()):
        #     exit('time pass')
        pic = item.xpath('div/section[@class="pic-content"]/a/img/@src')
        pic_content = item.xpath('div/section[@class="pic-content"]/a/img/@alt')
        text_content = item.xpath('div/section[@class="article-content"]/p//text()')
        data = {
            'type': 2,  #来福岛
            'content': pic_content if pic_content else text_content,
            'imgs': pic[0] if pic else '',
            'create_time': time[0].strip(),
        }
        table.insert(data)


for index in range(1, 7900):#2039
    url = 'http://www.laifudao.com/index_{page}.html'.format(page=index)
    slider(url=url)
    print(str(index) + ' is done')