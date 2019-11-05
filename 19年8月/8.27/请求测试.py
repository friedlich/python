import requests
from urllib.parse import urlencode

headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                      + 'Chrome/74.0.3729.169 Safari/537.36'
    }

data = {
        'offset': 0,
        'format': 'json',
        'keyword': '街拍图集',
        'autoload': 'true',
        'count': 20,
        'en_qc': 1,
        'cur_tab': 1
    }
url = 'https://www.toutiao.com/api/search/content/?' + urlencode(data)
response = requests.get(url, headers=headers)
print(response.status_code)
print(response.text)