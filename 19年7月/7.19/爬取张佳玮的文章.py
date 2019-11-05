import requests,bs4,json,re,csv,sys
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
with open(sys.path[0] + '\\张佳玮.csv','w',newline='',encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerow(['标题','链接','内容'])
    for i in range(1):
        url = 'https://www.zhihu.com/api/v4/members/zhang-jia-wei/articles'
        params = {'include': 'data[*].comment_count,suggest_edit,is_normal,thumbnail_extra_info,thumbnail,can_comment,comment_permission,admin_closed_comment,content,voteup_count,created,updated,upvoted_followees,voting,review_info,is_labeled,label_info;data[*].author.badge[?(type=best_answerer)].topics', 'offset': 20*i, 'limit': '20', 'sort_by': 'voteups'}
        # 这里有个小问题，不过问题不大，多了个'='号，导致有一部分作为[2]索引直接就没取到
        res = requests.get(url,headers=headers,params=params)
        json_articles = json.loads(res.text)
        articles_list = json_articles['data']
        for i in articles_list:
            title = i['title']
            href =  i['url']
            content = i['content']
            article = re.sub('\n','',content).replace(' ','')
            article = re.sub('</p>','\n',article)
            article = re.sub('[a-z\d\<>/="--";:._]','',article)
            article = re.sub('[\n]{2,}','\n',article)
            writer.writerow([title,href,article])