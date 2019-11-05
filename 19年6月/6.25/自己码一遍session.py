###
# session是会话过程中，服务器用来记录特定用户会话的信息。
# session和cookies的关系：cookies里带有session的编码信息，服务器可以通过cookies辨别用户，
# 同时返回和这个用户相关的特定编码的session。

import requests
session = requests.session()
#用requests.session()创建session对象，相当于创建了一个特定的会话，帮我们自动保持了cookies。
url_1 = 'https://wordpress-edu-3autumn.localprod.forc.work/wp-login.php'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
data_1 = {
    'log': input('请输入用户名：'),
    'pwd': input('请输入用户密码：'),
    'wp-submit': '登录',
    'redirect_to': 'https://wordpress-edu-3autumn.localprod.forc.work',
    'testcookie': '1'
}
res_login = session.post(url_1,headers=headers,data=data_1)
cookies = res_login.cookies
#提取cookies的方法：调用requests对象（login_in）的cookies属性获得登录的cookies，并赋值给变量cookies。
print(cookies)

url_2 = 'https://wordpress-edu-3autumn.localprod.forc.work/wp-comments-post.php'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
data_2 = {
    'comment': input('请输入你想评论的内容：'),
    'submit': '发表评论',
    'comment_post_ID': '13',
    'comment_parent': '39',
}
res_comment = session.post(url_2,headers=headers,data=data_2) #加一个(cookies=cookies)作为调用 #调用cookies的方法就是在post请求中传入cookies=cookies的参数)
print(res_comment.status_code)


