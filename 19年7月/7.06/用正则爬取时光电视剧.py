import re,requests,csv

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

url_list = []
url_1 = 'http://www.mtime.com/top/tv/top100/'
url_list.append(url_1)
url_2 = 'http://www.mtime.com/top/tv/top100/index-{page}.html'
for i in range(2,11):
    real_url = url_2.format(page=i)
    url_list.append(real_url)
for i in url_list:
    url = 'http://www.mtime.com/top/tv/top100/index-' + str(i) + '.html'
    # print(url)
    res = requests.get(url,headers=headers)
    content = res.text.replace('\n','').replace(' ','')
    id = re.findall('.*?"asyncRatingRegion".*?(<li>.*</li>)',content)[0]
    plays = re.findall('<li>.*?</li>',id)
    for play in plays:
        TV_title = re.findall('.*?"_blank">(.*?)<',play)[0]  #别花里花俏的，直接一步到位多好
        # TV_title = re.findall('.*?class="px14 pb6".*?"_blank">(.*?)<',play)[0] #这里的空格之前删除了，所以一定会报错
        # TV_title = re.findall('.*?class="px14.*?"_blank">(.*?)<',play)[0]
        # 东京爱情故事&nbsp;TokyoLoveStory(1991)
        print(TV_title)
        chinese_name = re.findall('(.*?)&nbsp',TV_title)[0]
        print(chinese_name)
        english_name = re.findall('\w+',TV_title)[2] #['东京爱情故事', 'nbsp', 'TokyoLoveStory', '1991']
        print(english_name)
        year = re.findall('\d+',TV_title)[0]
        print(year)       
