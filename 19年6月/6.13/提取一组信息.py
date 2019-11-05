import requests
# 引用requests库
from bs4 import BeautifulSoup
# 引用BeautifulSoup库

res_foods = requests.get('http://www.xiachufang.com/explore/')
# 获取数据
bs_foods = BeautifulSoup(res_foods.text,'html.parser')
# 解析数据
list_foods = bs_foods.find_all('div',class_='info pure-u')
# 查找最小父级标签

tag_a = list_foods[0].find('a') #因为这里的find方法默认的是找第一个标签，所以可以这么简化输入，事实上网页里有许多a标签
# 提取第0个父级标签中的<a>标签
print(tag_a.text[17:-13])
# 输出菜名，使用[17:-13]切掉了多余的信息
print('http://www.xiachufang.com'+tag_a['href'])
# 输出URL


# 自己做的，对比一下，有点繁琐
import requests
# 引用requests库
from bs4 import BeautifulSoup
# 引用BeautifulSoup库

res_foods = requests.get('http://www.xiachufang.com/explore/')
# 获取数据
bs_foods = BeautifulSoup(res_foods.text,'html.parser')
# 解析数据
list_foods = bs_foods.find_all('div',class_='info pure-u')
# 查找最小父级标签
list_food = list_foods[0]
food_name = list_food.find('a')
food_name = str.strip(food_name.text)
print(food_name)
food_URL = list_food.find('a')
print('链接为：'+'http://www.xiachufang.com'+food_URL['href'])
