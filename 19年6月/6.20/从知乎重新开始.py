# import requests
# from bs4 import BeautifulSoup
# #引入request和bs
# url='https://www.zhihu.com/people/zhang-jia-wei/posts/posts_by_votes?page=1'
# headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
# #使用headers是一种默认的习惯，默认你已经掌握啦~
# res=requests.get(url,headers=headers)
# #发起请求，将响应的结果赋值给变量res
# print(res.url)
# print(res.status_code)
# #检查状态码
# bstitle=BeautifulSoup(res.text,'html.parser')
# #用bs进行解析
# title=bstitle.findAll(class_='ContentItem-title')
# #提取我们想要的标签和里面的内容
# print(title)
# #打印title


import requests,openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = 'articles'
sheet['A1'] = '文章'
sheet['B1'] = '摘要'
sheet['C1'] = '链接'
num = 0
while True:
    url = 'https://www.zhihu.com/api/v4/members/zhang-jia-wei/articles?'
    headers = { 'referer': 'https://www.zhihu.com/people/zhang-jia-wei/posts/posts_by_votes',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
    params = 'include=data%5B*%5D.comment_count%2Csuggest_edit%2Cis_normal%2Cthumbnail_extra_info%2Cthumbnail%2Ccan_comment%2Ccomment_permission%2Cadmin_closed_comment%2Ccontent%2Cvoteup_count%2Ccreated%2Cupdated%2Cupvoted_followees%2Cvoting%2Creview_info%2Cis_labeled%2Clabel_info%3Bdata%5B*%5D.author.badge%5B%3F(type%3Dbest_answerer)%5D.topics&offset='+str(num)+'&limit=20&sort_by=voteups'
    res = requests.get(url,headers=headers,params=params)  # 这一招真得巨管用，不然又要400了
    # print(res.status_code)
    json_articles = res.json()
    list_articles = json_articles['data']
    for articles in list_articles:
        title = articles['title']
        excerpt = articles['excerpt']
        href = articles['url']
        sheet.append([title,excerpt,href])
    num = num + 20
    if num > 40:
        break
    
wb.save(r'c:/Users/asus/Desktop/Python/风变Python爬虫精进/爬虫阶段练习/6.20/articles1.xlsx')

# 太明显了，一个limit搞死你了啊，而offset就是起始文章序号的意思
