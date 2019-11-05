import requests
from bs4 import BeautifulSoup

url_destnation = 'https://spidermen.cn/'
res_destnation = requests.get (url_destnation)
print(res_destnation.status_code) # 打印响应码

bs_articles = BeautifulSoup(res_destnation.text,'html.parser')
list_articles = bs_articles.find_all('header', class_ = "entry-header") ## 首先找到每篇文章所在的相同的元素
for tag_article in list_articles: # 遍历列表
    tag_title = tag_article.find('h2',class_ = "entry-title") # 找文章标题 我发现只输入最外层也可以，里面标签的text也算是外层的
    tag_url = tag_article.find('a',rel = "bookmark")  # 找文章链接 我发现只要名字是唯一的，就不要层层标签都输入，直接输需要调用的标签也可以
    tag_date = tag_article.find('time',class_="entry-date published") # 找文章发布时间 这里也是的，突然感觉还是很方便的
    print(tag_title.text,'发布于：',tag_date.text) # 打印文章标题与发布时间
    print(tag_url['href'])  # 换行打印文章链接，需要使用属性名提取属性值

# import requests
# from bs4 import BeautifulSoup

# html = requests.get('https://spidermen.cn/')
# soup = BeautifulSoup(html.text,'html.parser')
# items = soup.find_all(class_="entry-header")
# for item in items:
#     title = item.find('h2').find('a')
#     time = item.find('div',class_="entry-meta").find('a').find('time')
#     http = item.find('h2').find('a')
#     print(title.text)
#     print('发布时间：',time.text)
#     print('文章链接：',http['href'],end='\n'+'------'+'\n')