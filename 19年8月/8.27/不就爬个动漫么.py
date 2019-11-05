import requests
from urllib.parse import urlencode

headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    }
data = {
    'offset': 0,
    'format': 'json',
    'keyword': '动漫图集',
    'autoload': 'true',
    'count': 20,
    'en_qc': 1,
    'cur_tab': 1
    }
url = 'https://www.toutiao.com/api/search/content/?aid=24&app_name=web_search&offset=0&format=json&keyword=%E5%8A%A8%E6%BC%AB%E5%9B%BE%E9%9B%86&autoload=true&count=20&en_qc=1&cur_tab=1&from=search_tab&pd=synthesis&timestamp=1566909169922'
response = requests.get(url, headers=headers)
print(response.status_code)
result = response.json()
print(result)