import requests

for i in range(5):
    url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
    headers = {
        'Origin': 'https://y.qq.com',
        'Referer': 'https://y.qq.com/portal/search.html',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
        }
    params = {
        'ct': '24',
        'qqmusic_ver': '1298',
        'remoteplace': 'txt.yqq.lyric',
        'searchid': '103398584634794647',
        'aggr':'0',
        'catZhida': '1',
        'lossless': '0',
        'sem': '1',
        't': '7',
        'p': str(i+1),
        'n': '5',
        'w': '周杰伦',
        'g_tk': '5381',
        'loginUin': '0',
        'hostUin': '0',
        'format': 'json',
        'inCharset': 'utf8',
        'outCharset': 'utf-8',
        'notice': '0',
        'platform': 'yqq.json',
        'needNewCode': '0',
        }

    res_lyric = requests.get(url,params=params)
    print(res_lyric.url)
    json_lyric = res_lyric.json()
    list_lyric = json_lyric['data']['lyric']['list']
    # for lyric in list_lyric:
    #     print(lyric['content'])

