import requests

res_music = requests.get('https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=56283759775743983&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=10&w=%E5%91%A8%E6%9D%B0%E4%BC%A6&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0')

json_music = res_music.json()

list_music = json_music['data']['song']['list']
for music in list_music:
    print(music['name'])
    print('所属专辑：' + music['album']['name'])
    print('所属时长：' + str(music['interval']) + '秒')
    print('所属链接：' + 'https://y.qq.com/n/yqq/song/' + music['mid'] + '.html\n\n')

# 个人理解，这个找起来似乎要比之前复杂了，其实不然，这个Preview预览简直是神器，把json内部结构清晰地展现了出来，一环套
# 一环，一层套一套，内部很清晰，要找的东西很好找。这里想说一下字典和列表真得是基础加重重点，一般取值的话会用字典取，一
# 一对应，遍历的话多用列表，结构相似，适合重复，这些都是个很细节的东西。字典的遍历有很多套路。理解很重要，动手很重要，
# 重复很重要，环环相扣

# 歌曲名就在这里，它的键是name。理解这句话：这个XHR是一个字典，键data对应的值也是一个字典；在该字典里，键song对应的
# 值也是一个字典；在该字典里，键list对应的值是一个列表；在该列表里，一共有20个元素；每一个元素都是一个字典；在每个字
# 典里，键name的值，对应的是歌曲名。此刻的你有了一个大胆的想法：利用requests.get()访问这个链接，把这个字典下载到本
# 地。然后去一层一层地读取，拿到歌曲名。

