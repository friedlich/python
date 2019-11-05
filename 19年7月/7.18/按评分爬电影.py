import requests
from bs4 import BeautifulSoup
film_all = []
scores = dict()
for a in range(2):

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
    res=requests.get('https://movie.douban.com/top250?start='+str(25*a)+'&filter=',headers=headers)

    soup=BeautifulSoup(res.text,'html.parser')
    soup_0=soup.find('ol',class_='grid_view')
    lists=soup_0.find_all('li')
    for i in lists:
        num=i.find('em',class_='').text[:]
        url=i.find('a')['href']
        name=i.find('span',class_='title').text
        
        say=i.find('span',class_='inq')

        if say :
            say = say.text
        else:
            say = '无评论'
            
        star=i.find('span',class_='rating_num').text
        resa='序号'+num+'、'+name+'评分'+star+' 推荐语——'+say+url
        film_all.append(resa)
        
        scores[int(num)-1] = star
print(film_all)
        
order = sorted(scores.items(),key = lambda x:x[-1],reverse = True)
print(order)


for i in dict(order):
    print(i) # 默认应该是打印出键
    print(film_all[i])