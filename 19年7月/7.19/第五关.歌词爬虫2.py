import requests,bs4,csv,sys,json,re
headers = {'Referer': 'https://y.qq.com/portal/search.html',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
for i in range(1):
    url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
    params = {'ct': '24', 'qqmusic_ver': '1298', 'remoteplace': 'txt.yqq.lyric', 'searchid': '105183628855408710', 'aggr': '0', 'catZhida': '1', 'lossless': '0', 'sem': '1', 't': '7', 'p': str(i+1), 'n': '5', 'w': '周杰伦', 'g_tk': '5381', 'loginUin': '0', 'hostUin': '0', 'format': 'json', 'inCharset':
'utf8', 'outCharset': 'utf-8', 'notice': '0', 'platform': 'yqq.json', 'needNewCode': '0'}
    res = requests.get(url,headers=headers,params=params)
    print(res.status_code)
    res.encoding = 'utf-8'
    # json_music = res.json()
    # print(res.text)
    json_music = json.loads(res.text)
    lyric_list = json_music['data']['lyric']['list']
    for i in lyric_list:
        title = i['songname']
        print(title)
        lyric = i['content'].replace(' ','').replace('\\n','\n').split('\n')
        print(lyric)
        for i in lyric:
            if '<em>' or '</em>' in i:
                i = re.findall('<em>?(.*?)</em>',i)
        
        print(lyric)