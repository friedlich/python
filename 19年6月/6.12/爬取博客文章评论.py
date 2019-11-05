import requests # 调用requests库
from bs4 import BeautifulSoup # 调用BeautifulSoup库

url_destnation = 'https://wordpress-edu-3autumn.localprod.forc.work/all-about-the-future_04/'
# 把网址复制给变量destnation_url
res_comment = requests.get (url_destnation) # 返回一个response对象，赋值给destnation
res_comment.encoding='utf-8'

bs_comment = BeautifulSoup(res_comment.text,'html.parser') # 把网页解析为BeautifulSoup对象
list_comments = bs_comment.find_all('div',class_= 'comment-content') #通过匹配属性提取出我们想要的元素
#for tag_comment in list_comments: # 遍历列表，取出列表中的每一个值
#    print(tag_comment.text) # 打印评论的文本

with open('博客评论.txt','a',encoding='utf-8') as f:
    for tag_comment in list_comments:
        f.write(tag_comment.text)
