import requests
#引入requests
headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
#封装headers
url='https://www.zhihu.com/api/v4/members/zhang-jia-wei/articles?'
#写入网址
params={
    'include':'data[*].comment_count,suggest_edit,is_normal,thumbnail_extra_info,thumbnail,can_comment,comment_permission,admin_closed_comment,content,voteup_count,created,updated,upvoted_followees,voting,review_info,is_labeled,label_info;data[*].author.badge[?(type=best_answerer)].topics',
    'offset':'10',
    'limit':'20',
    'sort_by':'voteups',
    }
#封装参数
res=requests.get(url,headers=headers,params=params)
#发送请求，并把响应内容赋值到变量res里面
print(res.status_code)
#确认请求成功