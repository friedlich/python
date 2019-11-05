import requests

url = 'https://c.y.qq.com/lyric/fcgi-bin/fcg_query_lyric_yqq.fcg'
headers = {    
    'Referer': 'https://y.qq.com/n/yqq/song/004Z8Ihr0JIu5s.html',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    }
params = {
    'nobase64': '1',
    'musicid': '102065756',
    '-': 'jsonp1',
    'g_tk': '5381',
    'loginUin': '0',
    'hostUin': '0',
    'format': 'json',
    'inCharset': 'utf8',
    'outCharset': 'utf-8',
    'notice': '0',
    'platform': 'yqq.json',
    'needNewCode': '0'
    }
res_lyric = requests.get(url,params=params)
json_lyric = res_lyric.json()
print(json_lyric)
# list_lyric = json_lyric["lyric"]
# print(list_lyric.text)
