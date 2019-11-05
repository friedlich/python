import requests, random, bs4

list_movies = []

for x in range(10):
    url = 'https://movie.douban.com/top250?start=' + str(x*25) + '&filter='
    headers = {
    'referer':'https://y.qq.com/portal/search.html',
    # 请求来源
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    # 标记了请求从什么设备，什么浏览器上发出
    }
    # 加表头是相当重要的，小心被和谐，被认出来是爬虫，然后就要被限制。虽然现在也有反爬虫，不过这么点小事应该不会大动干戈。
    res = requests.get(url)
    bs = bs4.BeautifulSoup(res.text, 'html.parser')
    bs = bs.find('ol', class_="grid_view")
    for titles in bs.find_all('li'):
        num = titles.find('em',class_="").text
        title = titles.find('span', class_="title").text
        comment = titles.find('span',class_="rating_num").text
        url_movie = titles.find('a')['href']

        if titles.find('span',class_="inq") != None:
            tes = titles.find('span',class_="inq").text
            # print(num + '.' + title + '——' + comment + '\n' + '推荐语：' + tes +'\n' + url_movie)
            list_movies.append(num + '.' + title + '——' + comment + '\n' + '推荐语：' + tes +'\n' + url_movie + '\n')
        else:
            # print(num + '.' + title + '——' + comment + '\n' +'\n' + url_movie)
            list_movies.append(num + '.' + title + '——' + comment + '\n' +'\n' + url_movie + '\n')

with open(r'c:/Users/asus/Desktop/Python/风变Python爬虫精进/爬虫阶段练习/6.13/movies_new2.txt','w',encoding='utf-8') as f:
    for i in list_movies:
        f.writelines(i)
        # writelines() 方法用于向文件中写入一序列的字符串。这一序列字符串可以是由迭代对象产生的，如一个字符串列表。
        # 换行需要制定换行符 \n。  fileObject.writelines( [ str ])



# import requests,random,bs4

# list_movies = []

# for i in range(10):
#     url = 'https://movie.douban.com/top250?start=' + str(i*25) + '&filter='
#     res = requests.get(url)
#     res.encoding = 'utf-8'
#     bs = bs4.BeautifulSoup(res.text,'html.parser')
#     bs = bs.find(class_="grid_view")
#     for movie in bs.find_all('li'):
#         num = str.strip(movie.find(class_="pic").text)
#         name = movie.find(class_="title").text
#         reco = movie.find(class_="inq").text
#         comment = movie.find(class_="rating_num").text
#         url_movie = movie.find('a')['href']       
#         idea = num + '.' + name + '——' + comment + '\n' + '推荐语：' + reco +'\n' + url_movie
#         list_movies.append(idea)
# print(list_movies)

# with open('movies_new.txt','w',encoding='utf-8') as f:
#     for i in list_movies:
#         f.write(i)