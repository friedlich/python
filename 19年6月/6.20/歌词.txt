import re,requests
for x in range(5):
    search_url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
    headers = {
        'origin': 'https://y.qq.com',
        'referer': 'https://y.qq.com/portal/search.html',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    params = {
        'ct': '24',
        'qqmusic_ver': '1298',
        'new_json': '1',
        'remoteplace': 'txt.yqq.song',
        't': '0',
        'aggr': '1',
        'cr': '1',
        'catZhida': '1',
        'lossless': '0',
        'flag_qc': '0',
        'p': str(x+1),
        'n': '10',
        'w': '周杰伦',
        'g_tk': '375486514',
        'loginUin': '0',
        'hostUin': '0',
        'format': 'json',
        'inCharset': 'utf8',
        'outCharset': 'utf-8',
        'notice': '0',
        'platform': 'yqq.json',
        'needNewCode': '0',
    }
    res_music = requests.get(search_url,headers=headers,params=params)
    json_music = res_music.json()
    list_music = json_music['data']['song']['list']
    for music in list_music:
        # 以name为键，查找歌曲名
        print('歌名：'+music['name'])
        # 查找专辑名
        play_name = music['album']['name']
        print('所属专辑：'+music['album']['name'])
        # 查找播放时长
        play_time = str(music['interval'])
        print('播放时长：'+str(music['interval'])+'秒')
        # 查找播放链接
        play_link = 'https://y.qq.com/n/yqq/song/'+music['mid']+'.html'
        print('播放链接：https://y.qq.com/n/yqq/song/'+music['mid']+'.html')
        #查找歌词
        print('歌词：')
        lyric_url = 'https://c.y.qq.com/lyric/fcgi-bin/fcg_query_lyric_yqq.fcg'
        headers = {
            'origin': 'https://y.qq.com',
            'referer': 'https://y.qq.com/n/yqq/song/'+music['mid']+'.html',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
        }
        params = {
        'nobase64': '1',
        'musicid': music['id'],
        '-': 'jsonp1',
        'g_tk': '375486514',
        'loginUin': '0',
        'hostUin': '0',
        'format': 'json',
        'inCharset': 'utf8',
        'outCharset': 'utf-8',
        'notice': '0',
        'platform': 'yqq.json',
        'needNewCode': '0'
        }
        res_lyric = requests.get(lyric_url,headers=headers,params=params)
        json_lyric = res_lyric.json()
        lyric = json_lyric['lyric']
        for i in lyric.split('&#10'):
            music_str = re.sub("[A-Za-z0-9\\!\\%\\[\\]\\,\\。\\&\\#\\;]", "", i)#用正则表达式去掉无用的符号字符
            if music_str.strip():#strip去掉空行
                print(music_str)
        print('------------------------')