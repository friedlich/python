from urllib.parse import urlencode
import requests

headers = {
    'Cookie': 'CXID=99EC883C10E56ACCD9C51E0501F2572B; SUID=421DCF8C4D238B0A5D2338DC000E3439; IPLOC=CN3100; SUV=004574F9B4A0D2065D34F2E2EC1C1816; ABTEST=0|1567213379|v1; weixinIndexVisited=1; sct=4; JSESSIONID=aaaTOsab0kNkW8D87P6Yw; ppinf=5|1567214067|1568423667|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZTo1OkdhdmlufGNydDoxMDoxNTY3MjE0MDY3fHJlZm5pY2s6NTpHYXZpbnx1c2VyaWQ6NDQ6bzl0Mmx1T05XY3pnekl0THB4WjBGcmp1ZmxWWUB3ZWl4aW4uc29odS5jb218; pprdig=Zg2fm4B5rhf1tLzXFzymVIYOpuQHkoC3cyazrrRQAh5FrJBMarC0XdJrE5qF0aoSwp7dveEdz_NvU5wrc_rThDVm6QOBdvalGSKL3vPhTF-saxl7WOPmXaDhW3QKxSggfWd9Feor0peRqnP1bDUgC2kXvY4EUaMllJRWv2U2wk8; sgid=25-30830015-AV1pyfPib3c1Sng3HH1kEXL0; ppmdig=156721406700000009eb7dbffa0675d018161e8cd139e0a7; PHPSESSID=vnh2p6jm5pnff54634nc5tviv0; SNUID=BAE43774F8FD69A787537952F9E440D8',
    'Host': 'weixin.sogou.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}

base_url = 'https://weixin.sogou.com/weixin?'

data = {
        'query': '风景',
        'type': 2,
        'page': 2
    }
queries = urlencode(data)
url = base_url + queries

proxies = {
                'http': '27.13.24.19:8998'  # 其实这一切都是假的，根本就没有用到代理啊，这可是无效的代理
            }
response = requests.get(url, allow_redirects=False, headers=headers, proxies=proxies)
print(response.status_code)