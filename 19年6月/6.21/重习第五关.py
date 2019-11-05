import re,requests
for i in range(3):
    search_url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
    headers = {
        'Origin': 'https://y.qq.com',
        'Referer': 'https://y.qq.com/portal/search.html',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    }
    res_music = requests.get(search_url,headers=headers,params='ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=62724806234357446&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p='+str(i+1)+'&n=10&w=%E5%91%A8%E6%9D%B0%E4%BC%A6&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0')
    json_music = res_music.json()
    list_music = json_music['data']['song']['list']
    for music in list_music:
        print('歌名：'+music['name'])
        play_name = music['album']['name']
        print('所属专辑：'+music['album']['name'])
        play_time = str(music['interval'])
        print('播放时长：'+str(music['interval'])+'秒')
        play_link = 'https://y.qq.com/n/yqq/song/'+music['mid']+'.html'
        print('播放链接：https://y.qq.com/n/yqq/song/'+music['mid']+'.html')
        print('歌词：')
        lyric_url = 'https://c.y.qq.com/lyric/fcgi-bin/fcg_query_lyric_yqq.fcg'
        headers = {
            'Origin': 'https://y.qq.com',
            'Referer': 'https://y.qq.com/n/yqq/song/'+music['mid']+'.html',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
        }
        res_lyric = requests.get(lyric_url,headers=headers,params='nobase64=1&musicid='+str(music['id'])+'&-=jsonp1&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0')
        json_lyric = res_lyric.json()
        lyric = json_lyric['lyric']
        for i in lyric.split('&#10'):
            music_str = re.sub("[A-Za-z0-9\\!\\%\\[\\]\\,\\。\\&\\#\\;]", "", i)#用正则表达式去掉无用的符号字符
            if music_str.strip():#strip去掉空行
                print(music_str)
        # s = re.sub('&#10;','\n',lyric)
        # t = re.sub('\\[.*?\\]','',s)
        # print(t)
        # for i in lyric:
        #     music_str = i.split()
        #     print(music_str)
        print('------------------------')


