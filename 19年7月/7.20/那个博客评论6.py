# 所以，更完整以及面向对象的代码应该是下面这样的：
# 这里主要还是关于session的理解

# 优化这个代码的话，我们需要理解一个新的概念——session（会话）
# 所谓的会话，你可以理解成我们用浏览器上网到关闭浏览器的这一过程。session是会话过程中，服务器用来记录特定用户会话的信息。
# 比如你打开浏览器逛购物网页的整个过程中，浏览了哪些商品，在购物车里放了多少件物品，这些记录都会被服务器保存在session中。
# 如果没有session，可能会出现这样搞笑的情况：你加购了很多商品在购物车，打算结算时，发现购物车空无一物Σ(っ°Д°;)っ
# ，因为服务器根本没有帮你记录你想买的商品。
# 对了，session和cookies的关系还非常密切——cookies中存储着session的编码信息，session中又存储了cookies的信息。
# 当浏览器第一次访问购物网页时，服务器会返回set cookies的字段给浏览器，而浏览器会把cookies保存到本地。
# 等浏览器第二次访问这个购物网页时，就会带着cookies去请求，而因为cookies里带有会话的编码信息，服务器立马就能辨认出
# 这个用户，同时返回和这个用户相关的特定编码的session。
# 这也是为什么你每次重新登录购物网站后，你之前在购物车放入的商品并不会消失的原因。因为你在登录时，服务器可以通过浏览器
# 携带的cookies，找到保存了你购物车信息的session。
# 既然cookies和session的关系如此密切，那我们可不可以通过创建一个session来处理cookies？
# 不知道。那就翻阅requests的官方文档找找看有没有这样的方法，能让我们创建session来处理cookies。

import requests,json,sys
session = requests.session()
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
def cookies_read():
    with open(sys.path[0] + '\\cookies.txt','r') as f:
        cookies_str = f.read()
        cookies_dict = json.loads(cookies_str)
        cookies = requests.utils.cookiejar_from_dict(cookies_dict)
        return cookies

def sign_in():
    url = 'https://wordpress-edu-3autumn.localprod.forc.work/wp-login.php'  
    data = {
    'log':'spiderman', #用input函数填写账号和密码，这样代码更优雅，而不是直接把账号密码填上去。
    'pwd':'crawler334566',
    'wp-submit':'登录',
    'redirect_to':'https://wordpress-edu-3autumn.localprod.forc.work',
    'testcookie':'1'
    }
    session.post(url,headers=headers,data=data)
    cookies = session.cookies
    cookies_dict = requests.utils.dict_from_cookiejar(cookies)
    cookise_str = json.dumps(cookies_dict)
    with open(sys.path[0] + '\\cookies.txt','w') as f:       
        f.write(cookise_str)

def write_message():
    url_1 = 'https://wordpress-edu-3autumn.localprod.forc.work/wp-comments-post.php'
    data_1 = {
    'comment': input('请输入你想评论的内容：'),
    'submit': '发表评论',
    'comment_post_ID': '13',
    'comment_parent': '0'
    }
    return session.post(url_1,headers=headers,data=data_1)

try:
    session.cookies = cookies_read()
except FileNotFoundError:
    sign_in()
    session.cookies = cookies_read()

num = write_message()
if num.status_code == 200:
    print('评论发表成功啦！')
else:
    sign_in()
    session.cookies = cookies_read()
    num = write_message()

# 下面，是这一关的复习：
# cookies是服务器为了标记用户，存储在用户本地的数据，它里面也保存了用户的登录信息，同时它有一定的时效性，过期就会失效。
# session是会话过程中，服务器用来记录特定用户会话的信息。
# session和cookies的关系：cookies里带有session的编码信息，服务器可以通过cookies辨别用户，同时返回和这个用户相关的
# 特定编码的session。

# 最后，还想和你多说几句——
# 其实，计算机之所以需要cookies和session，是因为HTTP协议是无状态的协议。
# 何为无状态？就是一旦浏览器和服务器之间的请求和响应完毕后，两者会立马断开连接，也就是恢复成无状态。
# 这样会导致：服务器永远无法辨认，也记不住用户的信息，像一条只有7秒记忆的金鱼。是cookies和session的出现，
# 才破除了web发展史上的这个难题。
# cookies不仅仅能实现自动登录，因为它本身携带了session的编码信息，网站还能根据cookies，记录你的浏览足迹，
# 从而知道你的偏好，只要再加以推荐算法，就可以实现给你推送定制化的内容。
# 比如，淘宝会根据你搜索和浏览商品的记录，给你推送符合你偏好的商品，增加你的购买率。
# cookies和session在这其中起到的作用，可谓举足轻重。
# 看来一块小饼干的作用，也不可小觑。

        

