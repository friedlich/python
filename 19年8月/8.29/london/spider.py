import json
import sys
from hashlib import md5
import pymongo
import requests
from urllib.parse import urlencode
from json.decoder import JSONDecodeError
from requests import RequestException
from config import *

client = pymongo.MongoClient(MONGO_URL, connect=False)
db = client[MONGO_DB]

def get_page_index(pn):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    }
    # data = {
    #     'tn': 'resultjson_com',
    #     'ipn': 'rj',
    #     'ct': 201326592,
    #     'fp': 'result',
    #     'queryWord': '柏林',
    #     'cl': 2,
    #     'lm': -1,
    #     'latest': 1,
    #     'word': '柏林',
    #     'pn': pn,
    #     'rn': 30,
    # }

    url = 'http://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E7%BA%BD%E7%BA%A6&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=0&ic=0&hd=0&latest=0&copyright=0&word=%E7%BA%BD%E7%BA%A6&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&pn=30&rn=30&gsm=&1567060161371='
    try:
        response = requests.get(url, headers=headers)
        print(response.status_code)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求详情页出错')
        return None

def parse_page_index(html):
    try:
        data = json.loads(html)
        # print(data)
        if data and 'data' in data.keys():
            for item in data.get('data'):
                yield item.get('thumbURL')
    except JSONDecodeError:
        pass

def save_to_mongo(result):
    if db[MONGO_TABLE].insert(result):
        print('存储到MondoDB成功', result)
        return True
    return False

def download_image(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    }
    print('正在下载', url)
    try:
        response = requests.get(url, headers=headers)
        print(response.status_code)
        if response.status_code == 200:
            save_image(response.content)
        print('请求未成功')
        return None
    except RequestException:
        print('请求图片出错', url)
        return None

def save_image(content):
    print('开始保存')
    with open(sys.path[0] + '\\' + 'image', 'wb') as f:
        f.write(content)

def main():
    pn = 30
    html = get_page_index(pn)
    # print(html)
    parse_page_index(html)
    print(parse_page_index(html))
    for url in parse_page_index(html):
        # print(url)
        download_image(url)
        result = {
            'title': '纽约',
            'image': url
        }
        if result: save_to_mongo(result)

if __name__ == '__main__':
    main()


