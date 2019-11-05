from urllib.parse import urlencode
import pymongo
import requests
from lxml.etree import XMLSyntaxError
from requests.exceptions import ConnectionError
from pyquery import PyQuery as pq
from liyang.WeixinArticles.config import *

client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]

base_url = 'https://weixin.sogou.com/weixin?'

headers = {
    'Cookie': 'CXID=99EC883C10E56ACCD9C51E0501F2572B; SUID=421DCF8C4D238B0A5D2338DC000E3439; IPLOC=CN3100; SUV=004574F9B4A0D2065D34F2E2EC1C1816; ABTEST=0|1567213379|v1; weixinIndexVisited=1; sct=4; JSESSIONID=aaaTOsab0kNkW8D87P6Yw; ppinf=5|1567214067|1568423667|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZTo1OkdhdmlufGNydDoxMDoxNTY3MjE0MDY3fHJlZm5pY2s6NTpHYXZpbnx1c2VyaWQ6NDQ6bzl0Mmx1T05XY3pnekl0THB4WjBGcmp1ZmxWWUB3ZWl4aW4uc29odS5jb218; pprdig=Zg2fm4B5rhf1tLzXFzymVIYOpuQHkoC3cyazrrRQAh5FrJBMarC0XdJrE5qF0aoSwp7dveEdz_NvU5wrc_rThDVm6QOBdvalGSKL3vPhTF-saxl7WOPmXaDhW3QKxSggfWd9Feor0peRqnP1bDUgC2kXvY4EUaMllJRWv2U2wk8; sgid=25-30830015-AV1pyfPib3c1Sng3HH1kEXL0; ppmdig=156721406700000009eb7dbffa0675d018161e8cd139e0a7; PHPSESSID=vnh2p6jm5pnff54634nc5tviv0; SNUID=BAE43774F8FD69A787537952F9E440D8',
    'Host': 'weixin.sogou.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}

# proxy = '200.137.138.2:80'
proxy = '187.243.253.182:33796'
max_count = 5


def get_proxy():
    try:
        response = requests.get(PROXY_POOL_URL)
        if response.status_code == 200:
            return response.text
        return None
    except ConnectionError:
        return None


def get_html(url, count=1):
    print('Crawling', url)
    print('Trying Count', count)
    global proxy
    if count >= max_count:
        print('Tried Too Many Counts')
        return None
    try:
        if proxy:
            print('用了代理', proxy)
            proxies = {
                'http': 'http://' + proxy
            }
            response = requests.get(url, allow_redirects=False, headers=headers, proxies=proxies)
        else:
            print('没用代理')
            response = requests.get(url, allow_redirects=False, headers=headers)
        if response.status_code == 200:
            return response.text
        if response.status_code == 302:
            # Need Proxy
            print('302')
            proxy = get_proxy()
            if proxy:
                print('Using Proxy', proxy)
                # count += 1
                # return get_html(url, count) # 因为要多次更换代理尝试获得能用的，所以不要去加以更换限制
                return get_html(url)
            else:
                print('Get Proxy Failed')
                return None
    except ConnectionError as e:
        print('Error Occurred', e.args)
        proxy = get_proxy()
        count += 1
        return get_html(url, count)


def get_index(keyword, page):
    data = {
        'query': keyword,
        'type': 2,
        'page': page
    }
    queries = urlencode(data)
    url = base_url + queries
    html = get_html(url)
    return html


def parse_index(html):
    doc = pq(html)
    items = doc('.news-box .news-list li .txt-box h3 a').items()  # 为了得到链接的生成器
    for item in items:
        yield item.attr('data-share')


def get_detail(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except ConnectionError:
        return None


def parse_detail(html):
    try:
        doc = pq(html)
        title = doc('.rich_media_title').text()
        content = doc('.rich_media_content ').text()
        date = doc('#publish_time').text()
        nickname = doc('#js_profile_qrcode > div > strong').text()
        wechat = doc('#js_profile_qrcode > div > p:nth-child(3) > span').text()
        return {
            'title': title,
            'content': content,
            'date': date,
            'nickname': nickname,
            'wechat': wechat
        }
    except XMLSyntaxError:
        return None


def save_to_mongo(data):
    if db['articles'].update({'title': data['title']}, {'$set': data}, True):
        print('Saved to Mongo', data['title'])
    else:
        print('Saved to Mongo Failed', data['title'])


def main():
    for page in range(70, 72):
        html = get_index(KEYWORD, page)
        # print(html)
        if html:
            article_urls = parse_index(html)
            for article_url in article_urls:
                article_html = get_detail(article_url)
                if article_html:
                    article_data = parse_detail(article_html)
                    print(article_data)
                    if article_data:
                        save_to_mongo(article_data)


if __name__ == '__main__':
    main()


# Using Proxy 200.137.138.2:80

# 我的 IP：140.207.29.66
# 访问时间：2019.08.31 11:07:41
