import requests,json,re,csv,sys

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
with open(sys.path[0] + '\\陈雪凝歌单.csv','w',newline='',encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        # writer.writerow(['歌曲名','专辑','时长','播放链接','歌词'])   
        writer.writerow(['歌曲名','专辑','时长','播放链接']) 
        for i in range(3):
            url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
            params = {'ct': '24', 'qqmusic_ver': '1298', 'new_json': '1', 'remoteplace': 'txt.yqq.song', 'searchid': '66890336131401644', 't': '0', 'aggr': '1', 'cr': '1', 'catZhida': '1', 'lossless': '0', 'flag_qc': '0', 'p': str(i+1), 'n': '10', 'w': '陈雪凝', 'g_tk': '5381', 'loginUin': '0', 'hostUin': '0',
        'format': 'json', 'inCharset': 'utf8', 'outCharset': 'utf-8', 'notice': '0', 'platform': 'yqq.json', 'needNewCode': '0'}
            res = requests.get(url,params=params,headers=headers)
            jsres = json.loads(res.text)
            jsdata = jsres['data']['song']['list']       
            for data in jsdata: # 昨天把for循环放在最前面总是出错的原因是'w'模式把之前写的全部擦除了，就是说昨天那样写就是打开了很多次文件
                title = data['title']
                print(title)
                album = data['album']['name']
                print(album)
                interval = str(data['interval'])
                print(interval)
                href = 'https://y.qq.com/n/yqq/song/' + data['mid'] + '.html'
                music_id = data['id']
                print(music_id)
                # writer.writerow([title,album,interval,href])
            

                # url1 = 'https://c.y.qq.com/lyric/fcgi-bin/fcg_query_lyric_yqq.fcg'
                lyric_url = 'https://c.y.qq.com/lyric/fcgi-bin/fcg_query_lyric_yqq.fcg'
                # params = {'nobase64': '1', 'musicid': str(music_id), '-': 'jsonp1', 'g_tk': '5381', 'loginUin': '0', 'hostUin': '0', 'format': 'json', 'inCharset': 'utf8', 'outCharset': 'utf-8', 'notice': '0', 'platform': 'yqq.json', 'needNewCode': '0'}
                # res_lyric = requests.get(url1,params=params,headers=headers)
                headers = {
                    'Origin': 'https://y.qq.com',
                    'Referer': 'https://y.qq.com/n/yqq/song/'+data['mid']+'.html', # 难以想象，这里面一定是要带这个referer的，不然报错
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
                }
                res_lyric = requests.get(lyric_url,headers=headers,params='nobase64=1&musicid='+str(music_id)+'&-=jsonp1&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0')
                # json_lyric = res_lyric.json()
                # content = json_lyric['lyric']
                json_lyric = res_lyric.json()
                # print(json_lyric)
                content = json_lyric['lyric']
                lyric = re.sub('&#10;','\n',content)
                lyric1 = re.sub('[a-z J]','',lyric)
                lyric2 = re.sub('[\[\]\d\&\#\;]','',lyric1)
                lyric3 = re.sub('[\n]{2,}','\n',lyric2)
                # lyric = json_lyric['lyric']
                # lyric = lyric.replace(' ','').replace('&#10;','\n')
                # lyric = re.sub('[A-Za-z\d\#\&\;]','',lyric)
                # lyric = re.findall('.*?](.*)',lyric)
                # lyric = [i for i in lyric if i !='']
                # for i in lyric1:
                #     print(i)
                # # with open(sys.path[0] + '\\歌曲信息.csv','w',newline='',encoding='utf-8-sig') as f:
                # #     writer = csv.writer(f)
                # #     writer.writerow(['歌曲名','专辑','时长','播放链接','歌词'])
                writer.writerow([title,album,interval,href,lyric3])
                



