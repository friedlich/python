###
# session是会话过程中，服务器用来记录特定用户会话的信息。
# session和cookies的关系：cookies里带有session的编码信息，服务器可以通过cookies辨别用户，
# 同时返回和这个用户相关的特定编码的session。

import requests,json
session = requests.session()
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}

def cookies_read():
    cookies_txt = open(r'c:/Users/asus/Desktop/Python/风变Python爬虫精进/爬虫阶段练习/6.25/cookies.txt','r') #以reader读取模式，打开名为cookies.txt的文件。
    cookies_dic = json.loads(cookies_txt.read()) #调用json模块的loads函数，把字符串转成字典。
    cookies = requests.utils.cookiejar_from_dict(cookies_dic) #把转成字典的cookies再转成cookies本来的格式。
    session.cookies = cookies #获取cookies：就是调用requests对象（session）的cookies属性。
    return session.cookies

def login_in():
    url_1 = 'https://wordpress-edu-3autumn.localprod.forc.work/wp-login.php'
    data_1 = {
    'log': input('请输入用户名：'),
    'pwd': input('请输入用户密码：'),
    'wp-submit': '登录',
    'redirect_to': 'https://wordpress-edu-3autumn.localprod.forc.work',
    'testcookie': '1'
    }
    session.post(url_1,headers=headers,data=data_1)

    cookies = session.cookies
    cookies_dic = requests.utils.dict_from_cookiejar(cookies)
    cookies_str = json.dumps(cookies_dic)
    f = open(r'c:/Users/asus/Desktop/Python/风变Python爬虫精进/爬虫阶段练习/6.25/cookies.txt','w')
    f.write(cookies_str)
    f.close()

def write_message():
    url_2 = 'https://wordpress-edu-3autumn.localprod.forc.work/wp-comments-post.php'
    data_2 = {
        'comment': input('请输入你想评论的内容：'),
        'submit': '发表评论',
        'comment_post_ID': '13',
        'comment_parent': '39',
    }
    res_comment = session.post(url_2,headers=headers,data=data_2)
    return res_comment

try:
    session.cookies = cookies_read()
except:
    login_in()
    session.cookies = cookies_read()

num = write_message()
if num.status_code == 200:
    print('成功啦')
else:
    login_in()
    session.cookies = cookies_read()
    num = write_message()




