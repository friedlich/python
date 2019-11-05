import requests
import json

singer = input('你最喜欢的歌手是谁呀：')
for i in range(3):
    url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
    params = {
        'ct': '24',
        'qqmusic_ver': '1298',
        'new_json': '1',
        'remoteplace': 'txt.yqq.song',
        'searchid': '65952186418122277',
        't': '0',
        'aggr': '1',
        'cr': '1',
        'catZhida': '1',
        'lossless': '0',
        'flag_qc':' 0',
        'p': str(i+1),
        'n': '10',
        'w': singer,
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
    res_infor = requests.get(url,params=params)
    json_infor = json.loads(res_infor.text)
    list_infor = json_infor['data']['song']['list']
    for infor in list_infor:
        print(infor['name'])
        print('专辑：'+infor['album']['name'])
        print('时长：'+str(infor['interval'])+'秒')
        print('链接：'+ res_infor.url + infor['mid'] + 'html\n\n')


    