import requests,bs4,json,openpyxl,re,sys
wb = openpyxl.Workbook()
#创建工作薄
sheet = wb.active
#获取工作薄的活动表
sheet.title = '许嵩'
#工作表重命名

sheet['A1'] = '歌曲名'
sheet['B1'] = '所属专辑'
sheet['C1'] = '播放时长'
sheet['D1'] = '播放链接'
sheet['E1'] = '歌词'

for i in range(3):
    url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
    params = {'ct': '24', 'qqmusic_ver': '1298', 'new_json': '1', 'remoteplace': 'txt.yqq.song', 'searchid': '60614869207311875', 't': '0', 'aggr': '1', 'cr': '1', 'catZhida': '1', 'lossless': '0', 'flag_qc': '0', 'p': str(i+1), 'n': '10', 'w': '许嵩', 'g_tk': '5381', 'loginUin': '0', 'hostUin': '0',
'format': 'json', 'inCharset': 'utf8', 'outCharset': 'utf-8', 'notice': '0', 'platform': 'yqq.json', 'needNewCode': '0'}
    res = requests.get(url,params=params,headers=headers) #TypeError: request() got an unexpected keyword argument 'header',原来是眼镜瞎了
    print(res.status_code)
    json_music = json.loads(res.text)
    json_list = json_music['data']['song']['list']
    for list in json_list:
        name = list['name']
        album = list['album']['name']
        interval = list['interval']
        href = 'https://y.qq.com/n/yqq/song/' + list['mid'] + '.html'
        music_id = list['id']

        url = 'https://c.y.qq.com/lyric/fcgi-bin/fcg_query_lyric_yqq.fcg'
        headers = {
                'Origin': 'https://y.qq.com',
                'Referer': 'https://y.qq.com/n/yqq/song/'+list['mid']+'.html', # 难以想象，这里面一定是要带这个referer的，不然报错
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
            }
        params = {'nobase64': '1', 'musicid': str(music_id), '-': 'jsonp1', 'g_tk': '5381', 'loginUin': '0', 'hostUin': '0', 'format': 'json', 'inCharset': 'utf8', 'outCharset': 'utf-8', 'notice': '0', 'platform': 'yqq.json', 'needNewCode': '0'}
        res = requests.get(url, headers=headers,params=params)
        json_lyric = json.loads(res.text)
        # print(json_lyric)
        # try:
        #     content = json_lyric['lyric']  # content = json_lyric['lyric']   KeyError: 'lyric'
        #     lyric = re.sub('&#10;','\n',content)
        #     lyric1 = re.sub('[a-z J]','',lyric) 
        #     lyric2 = re.sub('[\[\]\d\&\#\;]','',lyric1)
        #     lyric3 = re.sub('[\n]{2,}','\n',lyric2)
        #     sheet.append([name,album,interval,href,lyric3])
        # except KeyError:
        #     content = ''
        #     sheet.append([name,album,interval,href,content]) 
        if json_lyric['lyric']: # 原来如此，竟发现if也是有try的效果的呀。其实就是先尝试是否为真的效果，为真就可以继续，否则else
            content = json_lyric['lyric']
            lyric = re.sub('&#10;','\n',content)
            lyric1 = re.sub('[a-z J]','',lyric) 
            lyric2 = re.sub('[\[\]\d\&\#\;]','',lyric1)
            lyric3 = re.sub('[\n]{2,}','\n',lyric2)
            sheet.append([name,album,interval,href,lyric3])
        else:
            content = ''
            sheet.append([name,album,interval,href,content]) 
wb.save(sys.path[0]+'\\许嵩.xlsx')