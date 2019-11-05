import requests
# 引用requests库
res_music = requests.get('https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=60997426243444153&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=20&w=%E5%91%A8%E6%9D%B0%E4%BC%A6&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0')
# 调用get方法，下载这个字典
json_music = res_music.json()
# 使用json()方法，将response对象，转为列表/字典
list_music = json_music['data']['song']['list']
# 一层一层地取字典，获取歌单列表
for music in list_music:
# list_music是一个列表，music是它里面的元素
    print(music['name'])
    # 以name为键，查找歌曲名
    print('所属专辑：'+music['album']['name'])
    # 查找专辑名
    print('播放时长：'+str(music['interval'])+'秒')
    # 查找播放时长
    print('播放链接：https://y.qq.com/n/yqq/song/'+music['mid']+'.html\n\n')
    # 查找播放链接