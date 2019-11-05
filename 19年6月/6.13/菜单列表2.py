import requests
# 引用requests库
from bs4 import BeautifulSoup
# 引用BeautifulSoup库

res_foods = requests.get('http://www.xiachufang.com/explore/')
# 获取数据
bs_foods = BeautifulSoup(res_foods.text,'html.parser')
# 解析数据

tag_name = bs_foods.find_all('p',class_='name')
# 查找包含菜名和URL的<p>标签
tag_ingredients = bs_foods.find_all('p',class_='ing ellipsis')
# 查找包含食材的<p>标签
list_all = []
# 创建一个空列表，用于存储信息
for x in range(len(tag_name)):
# 启动一个循环，次数等于菜名的数量
    list_food = [tag_name[x].text[18:-14],tag_name[x].find('a')['href'],tag_ingredients[x].text[1:-1]]
    # 提取信息，封装为列表。注意此处[18:-14]切片和之前不同，是因为此处使用的是<p>标签，而之前是<a>
    list_all.append(list_food)
    # 将信息添加进list_all
print(list_all)
# 打印


import requests
# 引用requests库
from bs4 import BeautifulSoup
# 引用BeautifulSoup库

res_foods = requests.get('http://www.xiachufang.com/explore/')
# 获取数据
bs_foods = BeautifulSoup(res_foods.text,'html.parser')
# 解析数据
list_all = []
# 创建一个空列表，用于存储信息
list_1 = bs_foods.find_all(class_="name")
long = range(len(list_1))
print(long)
list_2 = bs_foods.find_all(class_="ing ellipsis")

for i in range(26):
    name = str.strip(list_1[i].text)
    tag = list_1[i].find('a')
    URL = 'http://www.xiachufang.com'+tag['href']
    ingredients = str.strip(list_2[i].text)
    list_all.append([name,URL,ingredients])
print(list_all)
    