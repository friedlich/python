import re,requests,openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = 'douban_movies'
sheet['A1'] = '序号'
sheet['B1'] = '电影名称'
sheet['C1'] = '上映时间'
sheet['D1'] = '上映地点'
sheet['E1'] = '电影分类'
sheet['F1'] = '电影评分'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}
movie_informations = []
for i in range(10):
    url = 'https://movie.douban.com/top250?start=' + str(i*25) + '&filter='
    # response = requests.get(url, headers=headers)
    # content = response.text.replace(' ', '').replace('\n', '')
    # all_tags = re.findall('.*grid_view.*?(<li>.*</li>)', content, flags=re.S)[0]
    # movie_tags = re.findall('<li>.*?</li>', all_tags)
    res = requests.get(url,headers=headers)
    content = res.text.replace('\n','').replace(' ','')
    grid = re.findall('.*?grid_view.*?(<li>.*</li>)',content)[0]
    movies = re.findall('(<li>.*?</li>)',grid) # 这里的/让我debug了半天
    # print(len(movies))
    for movie in movies:
        title = re.findall('.*?class="title">(.*?)<',movie)[0]
        other = re.findall('.*class="bd".*?<br>(.*?)<',movie)[0]
        year = int(re.findall('\d+',other)[0])
        country = re.findall('.*?/(.*?)/',other)[0].replace('&nbsp;','')
        type = re.findall('.*;(.*)',other)[0]
        rating = float(re.findall('.*?class="rating_num".*?>(.*?)<',movie)[0])
        movie_informations.append([title,year,country,type,rating])

for index,movie_information in enumerate(movie_informations):
    title,year,country,type,rating = movie_information
    sheet.append([index+1,title,year,country,type,rating])
wb.save(r'C:\Users\asus\Desktop\Python\风变Python爬虫精进\爬虫阶段练习\19年7月\7.06\douban_movies.xlsx') # 文件名取Top250.xlsx会报错




