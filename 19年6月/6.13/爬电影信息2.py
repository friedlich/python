import requests
# 引用requests模块
from bs4 import BeautifulSoup
for x in range(10):
    url = 'https://movie.douban.com/top250?start=' + str(x*25) + '&filter='
    res = requests.get(url)
    bs = BeautifulSoup(res.text, 'html.parser')
    tag_num = bs.find_all('div', class_="item")
    # 查找包含序号，电影名，链接的<div>标签
    tag_comment = bs.find_all('div', class_='star')
    # 查找包含评分的<div>标签
    tag_word = bs.find_all('span', class_='inq')
    # 查找推荐语

    list_all = []
    for x in range(len(tag_num)):
        if tag_num[x].text[2:5] == '' or tag_num[x].text[2:5] =='':
        # 此处引号内，填写没有推荐语的电影序号
            list_movie = [tag_num[x].text[2:5], tag_num[x].find('img')['alt'], tag_comment[x].text[2:5], tag_num[x].find('a')['href'] ]
        else:
            list_movie = [tag_num[x].text[2:5], tag_num[x].find('img')['alt'], tag_comment[x].text[2:5], tag_word[x].text, tag_num[x].find('a')['href']]
        list_all.append(list_movie)
    print(list_all)
        
    


# import requests,random,bs4
# for i in range(10):
#     url = 'https://movie.douban.com/top250?start=' + str(i*25) + '&filter='
#     res = requests.get(url)
#     bs = bs4.BeautifulSoup(res.text,'html.parser')
#     num = bs.find_all(class_="pic")
#     print(type(num))
#     name = bs.find_all(class_="title")
#     reco = bs.find_all(class_="inq")
#     comment = bs.find_all(class_="rating_num")
#     url_movie = bs.find_all('a') 
#     print(range(len(num)))
#     for i in range(len(num)):
#         print(type(num[i]))
#         num_ = str.strip(num[i].text)
#         name_ = name[i].text
#         reco_ = reco[i].text
#         comment_ = comment[i].text
#         url_movie_ = url_movie[i]['href']
#         print(num_ + '.' + name_ + '——' + comment_ + '\n' + '推荐语：' + reco_ +'\n' + url_movie_)
        