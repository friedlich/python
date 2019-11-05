import requests,bs4,json
while True:
    singer = input('请输入歌手名字：')
    for i in range(2):
        url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
        params = {'ct': '24', 'qqmusic_ver': '1298', 'new_json': '1', 'remoteplace': 'txt.yqq.song', 'searchid': '60614869207311875', 't': '0', 'aggr': '1', 'cr': '1', 'catZhida': '1', 'lossless': '0', 'flag_qc': '0', 'p': str(i+1), 'n': '10', 'w': singer, 'g_tk': '5381', 'loginUin': '0', 'hostUin': '0',
    'format': 'json', 'inCharset': 'utf8', 'outCharset': 'utf-8', 'notice': '0', 'platform': 'yqq.json', 'needNewCode': '0'}
        res = requests.get(url,params=params,headers=headers)
        json_music = json.loads(res.text)
        json_list = json_music['data']['song']['list']
        for list in json_list:
            name = list['name']
            album = list['album']['name']
            interval = list['interval']
            href = 'https://y.qq.com/n/yqq/song/' + list['mid'] + '.html'
            print('歌曲名:',name,   '所属专辑：',album,   '歌曲时长:',interval)
            print('播放链接:',href)
    a = input('输入0退出，输入其他继续查询：')
    if a == '0':
        break
    else:
        continue