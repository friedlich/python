import requests
from bs4 import BeautifulSoup

list_all = []

def recipe():
    url = 'http://www.xiachufang.com/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
    res = requests.get(url,headers=headers)
    bsdata = BeautifulSoup(res.text,'html.parser')
    bs_foods = bsdata.find(class_="pop-recipes block")('li')
    # print(bs_foods)
    for i in bs_foods:
        name = i.find(class_="recipe")['title']
        half = i.find(class_="cover")['href']
        href = 'http://www.xiachufang.com/'+half
        list_all.append([name,href])
        
recipe()        
print(list_all)