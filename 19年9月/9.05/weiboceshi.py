import  requests

search_url = 'https://weibo.cn/search/mblog'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

data = {
    'mp': 100,
    'page': 2
}

keyword = '000001'
url = '{url}?keyword={keyword}'.format(url=search_url, keyword=keyword)

response = requests.post(url=url, headers=headers, data=data)
print(response.status_code)
print(response.text)